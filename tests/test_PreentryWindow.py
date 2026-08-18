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
    assert widget.preentry.timer.isActive()


def test_scanrfid_pauses_timer_after_read(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.preentry.scanrfid()

    assert widget.preentry.ui.rfidHeaderlineEdit.text() == "ABCDEF"
    assert not widget.preentry.timer.isActive()


def test_scanrfid_resumes_timer_after_restore(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.preentry.scanrfid()
    widget.preentry.restore_timer()

    assert widget.preentry.timer.isActive()
