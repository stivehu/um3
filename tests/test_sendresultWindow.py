import pytest, pytest_mock
from PyQt5 import QtCore
from PyQt5.QtTest import QTest

import src.controller.ApplicationWindow
from src.controller.ApplicationWindow import ApplicationWindow
from src.models.EntrypickupModel import EntrypickupModel
from tests.fixtures.jsons import *


def test_resize_text(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.sendresultPushButton, QtCore.Qt.LeftButton)
    widget.sendresultWindow.resize(640, 480)
    widget.sendresultWindow.resize(320, 240)
    widget.sendresultWindow.resize(160, 80)


def all_field_is_empty(widget):
    assert widget.sendresultWindow.ui.startnumLineEdit.text() == ''
    assert widget.sendresultWindow.ui.firstnameLineEdit.text() == ''
    assert widget.sendresultWindow.ui.lastnameLineEdit.text() == ''


def test_empty_fields(qtbot, mocker):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.sendresultPushButton, QtCore.Qt.LeftButton)
    mocker.patch('src.controller.SendresultWindow.EntrypickupModel.get_entry_from_rfid', return_value='{}')
    all_field_is_empty(widget)


def test_close_event(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.sendresultPushButton, QtCore.Qt.LeftButton)
    widget.sendresultWindow.close()
