from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox

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
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.LeftButton)
    widget.preentry.resize(640, 480)
    widget.preentry.resize(320, 240)
    widget.preentry.resize(160, 80)


def test_close_event(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.LeftButton)
    widget.preentry.close()


def test_set_entry_startnum(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.LeftButton)
    widget.preentry.ui.startnumHeaderlineEdit.setText("20002")
    qtbot.keyPress(widget.preentry.ui.startnumHeaderlineEdit, QtCore.Qt.Key_Return)
    qtbot.mouseClick(widget.preentry.ui.nextpushButton, QtCore.Qt.LeftButton)
    assert widget.preentry.ui.startnumHeaderlineEdit.text() == "20003"
    qtbot.mouseClick(widget.preentry.ui.prevpushButton, QtCore.Qt.LeftButton)
    assert widget.preentry.ui.startnumHeaderlineEdit.text() == "20002"


def test_login(qtbot, mocker):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.LeftButton)
    mocker.patch('src.models.EnrtyModel.EntryModel.loginSite', return_value=True)
    qtbot.mouseClick(widget.preentry.ui.loginpushButton, QtCore.Qt.LeftButton)
    mocker.patch('src.models.EnrtyModel.EntryModel.loginSite', return_value=False)
    qtbot.mouseClick(widget.preentry.ui.loginpushButton, QtCore.Qt.LeftButton)


def test_action_insert_save_nextpush_button(qtbot, mocker):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.preEntryPushButton, QtCore.Qt.LeftButton)
    mocker.patch('src.models.EnrtyModel.EntryModel.loginSite', return_value=True)
    qtbot.mouseClick(widget.preentry.ui.nextpushButton, QtCore.Qt.LeftButton)
