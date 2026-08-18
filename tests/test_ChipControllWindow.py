import time

import pytest, pytest_mock
from PyQt6 import QtCore
from PyQt6.QtTest import QTest

import src.controller.ApplicationWindow
from src.controller.ApplicationWindow import ApplicationWindow
from src.models.EntrypickupModel import EntrypickupModel
from tests.fixtures.jsons import *


def test_resize_text(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.chipControllWindow.resize(640, 480)
    widget.chipControllWindow.resize(320, 240)
    widget.chipControllWindow.resize(160, 80)


def all_field_is_empty(widget):
    assert widget.chipControllWindow.ui.startnumLineEdit.text() == ''
    assert widget.chipControllWindow.ui.distanceLineEdit.text() == ''
    assert widget.chipControllWindow.ui.firstnameLineEdit.text() == ''
    assert widget.chipControllWindow.ui.lastnameLineEdit.text() == ''
    assert widget.chipControllWindow.ui.genderLineEdit.text() == ''
    assert widget.chipControllWindow.ui.agegroupLineEdit.text() == ''
    assert widget.chipControllWindow.ui.pickedupLineEdit.text() == ''


def test_empty_fields(qtbot, mocker):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid', return_value='{}')
    all_field_is_empty(widget)


def test_clean_fields(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.chipControllWindow.cleanFields()
    all_field_is_empty(widget)


def test_close_event(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.chipControllWindow.close()


def test_scanrfid_transient_error_does_not_stop_timer(qtbot, mocker):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', side_effect=Exception('port error'))

    widget.chipControllWindow.scanrfid()
    qtbot.waitUntil(lambda: widget.chipControllWindow.ui.statusBar.text() == 'port error', timeout=2000)

    assert widget.chipControllWindow.timer.isActive()


def test_scanrfid_pauses_timer_after_read(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                  return_value=entries_pickedup)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.chipControllWindow.scanrfid()
    qtbot.waitUntil(lambda: widget.chipControllWindow.ui.startnumLineEdit.text() == "100", timeout=2000)

    assert not widget.chipControllWindow.timer.isActive()


def test_scanrfid_does_not_block_ui_thread(qtbot, mocker):
    # A soros port olvasása másodpercekig blokkolhat (SerialTransport
    # timeout=5s) -- ha a scanrfid szinkron lenne, ez lefagyasztaná a teljes
    # ablakot. Ez a teszt azt igazolja, hogy a scanrfid() azonnal visszatér,
    # a tényleges olvasás háttérszálon fut.
    def slow_get_tid(self):
        time.sleep(0.3)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                  return_value=entries_pickedup)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.chipControllWindow.scanrfid()

    assert widget.chipControllWindow.ui.startnumLineEdit.text() == ""
    qtbot.waitUntil(lambda: widget.chipControllWindow.ui.startnumLineEdit.text() == "100", timeout=2000)


def test_scanrfid_ignores_overlapping_calls_while_reading(qtbot, mocker):
    call_count = {'n': 0}

    def slow_get_tid(self):
        call_count['n'] += 1
        time.sleep(0.3)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                  return_value=entries_pickedup)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.chipControllWindow.timer.stop()

    widget.chipControllWindow.scanrfid()
    widget.chipControllWindow.scanrfid()
    qtbot.waitUntil(lambda: widget.chipControllWindow.ui.startnumLineEdit.text() == "100", timeout=2000)

    assert call_count['n'] == 1


def test_close_event_while_read_in_flight_does_not_crash(qtbot, mocker):
    def slow_get_tid(self):
        time.sleep(0.2)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.chipControllWindow.scanrfid()
    widget.chipControllWindow.close()
