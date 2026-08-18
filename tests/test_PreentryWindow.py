import time

from PyQt6 import QtCore
from PyQt6.QtWidgets import QMessageBox

import src.models.EnrtyModel
from src.chafonrfid.Chafonrfid import Chafonrfid
from src.controller.ApplicationWindow import ApplicationWindow
from src.models.EnrtyModel import EntryModel
from src.models.EntrypickupModel import EntrypickupModel
from src.models.RemoteApiModel import RemoteApiModel
from src.controller.PreentryWindow import PreentryWindow
from tests.fixtures.jsons import entry_save_result, distances
import pytest, pytest_mock


def test_resize_text(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.preentry.resize(640, 480)
    widget.preentry.resize(320, 240)
    widget.preentry.resize(160, 80)


def test_resize_text_with_auto_resize_enabled(qtbot, mocker):
    mocker.patch('src.models.SettingsModel.SettingsModel.get_auto_resize_window', return_value=True)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.preentry.resize(640, 480)
    widget.preentry.resize(320, 240)
    widget.preentry.resize(160, 80)


def test_close_event(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.preentry.close()


def test_set_entry_startnum(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.preentry.ui.startnumHeaderlineEdit.setText("20002")
    qtbot.keyPress(widget.preentry.ui.startnumHeaderlineEdit, QtCore.Qt.Key.Key_Return)
    qtbot.mouseClick(widget.preentry.ui.nextpushButton, QtCore.Qt.MouseButton.LeftButton)
    assert widget.preentry.ui.startnumHeaderlineEdit.text() == "20003"
    qtbot.mouseClick(widget.preentry.ui.prevpushButton, QtCore.Qt.MouseButton.LeftButton)
    assert widget.preentry.ui.startnumHeaderlineEdit.text() == "20002"


def test_login(qtbot, mocker):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.models.EnrtyModel.EntryModel.loginSite', return_value=True)
    qtbot.mouseClick(widget.preentry.ui.loginpushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.models.EnrtyModel.EntryModel.loginSite', return_value=False)
    qtbot.mouseClick(widget.preentry.ui.loginpushButton, QtCore.Qt.MouseButton.LeftButton)


def test_action_insert_save_nextpush_button(qtbot, mocker):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.models.EnrtyModel.EntryModel.loginSite', return_value=True)
    qtbot.mouseClick(widget.preentry.ui.nextpushButton, QtCore.Qt.MouseButton.LeftButton)


def test_scanrfid_transient_error_does_not_stop_timer(qtbot, mocker):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', side_effect=Exception('port error'))

    widget.preentry.scanrfid()
    qtbot.waitUntil(lambda: widget.preentry.ui.statusBar.text() == 'port error', timeout=2000)

    assert widget.preentry.timer.isActive()


def test_scanrfid_pauses_timer_after_read(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.preentry.scanrfid()
    qtbot.waitUntil(lambda: widget.preentry.ui.rfidHeaderlineEdit.text() == "ABCDEF", timeout=2000)

    assert not widget.preentry.timer.isActive()


def test_scanrfid_resumes_timer_after_restore(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.preentry.scanrfid()
    qtbot.waitUntil(lambda: widget.preentry.ui.rfidHeaderlineEdit.text() == "ABCDEF", timeout=2000)
    widget.preentry.restore_timer()

    assert widget.preentry.timer.isActive()


def test_scanrfid_ignores_lingering_consumed_chip(qtbot, mocker):
    get_tid = mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.preentry.scanrfid()
    qtbot.waitUntil(lambda: widget.preentry.ui.rfidHeaderlineEdit.text() == "ABCDEF", timeout=2000)
    widget.preentry.actioninsertpushButton()
    widget.preentry.restore_timer()
    widget.preentry.scanrfid()
    qtbot.wait(300)

    assert widget.preentry.ui.rfidHeaderlineEdit.text() == ""


def test_scanrfid_accepts_new_chip_after_consuming_previous(qtbot, mocker):
    get_tid = mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.preentry.scanrfid()
    qtbot.waitUntil(lambda: widget.preentry.ui.rfidHeaderlineEdit.text() == "ABCDEF", timeout=2000)
    widget.preentry.actioninsertpushButton()
    widget.preentry.restore_timer()

    get_tid.return_value = "123456"
    widget.preentry.scanrfid()

    qtbot.waitUntil(lambda: widget.preentry.ui.rfidHeaderlineEdit.text() == "123456", timeout=2000)


def test_scanrfid_does_not_block_ui_thread(qtbot, mocker):
    # A soros port olvasása másodpercekig blokkolhat (SerialTransport
    # timeout=5s) -- ha a scanrfid szinkron lenne, ez lefagyasztaná a teljes
    # ablakot, és a fagyás alatt beérkező kattintások a feloldódáskor
    # egyszerre, duplán sülnének el. Ez a teszt azt igazolja, hogy a
    # scanrfid() azonnal visszatér, a tényleges olvasás háttérszálon fut.
    def slow_get_tid(self):
        time.sleep(0.3)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.preentry.scanrfid()

    assert widget.preentry.ui.rfidHeaderlineEdit.text() == ""
    qtbot.waitUntil(lambda: widget.preentry.ui.rfidHeaderlineEdit.text() == "ABCDEF", timeout=2000)


def test_scanrfid_ignores_overlapping_calls_while_reading(qtbot, mocker):
    call_count = {'n': 0}

    def slow_get_tid(self):
        call_count['n'] += 1
        time.sleep(0.3)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)
    # a saját poll-timerét leállítjuk, hogy csak a két explicit scanrfid()
    # hívás olvasson -- korábbi (le nem zárt) tesztek háttérben futó ablakai
    # egyébként is triggerelhetnek egy-egy plusz olvasást ugyanerre a
    # globálisan patch-elt get_tid-re, ami itt nem a vizsgált eset.
    widget.preentry.timer.stop()

    widget.preentry.scanrfid()
    widget.preentry.scanrfid()
    qtbot.waitUntil(lambda: widget.preentry.ui.rfidHeaderlineEdit.text() == "ABCDEF", timeout=2000)

    assert call_count['n'] == 1


def test_close_event_while_read_in_flight_does_not_crash(qtbot, mocker):
    def slow_get_tid(self):
        time.sleep(0.2)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.preentry.scanrfid()
    widget.preentry.close()
