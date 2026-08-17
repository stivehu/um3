import pytest,pytest_mock
from PyQt6 import QtCore

from src.chafonrfid.Chafonrfid import Chafonrfid
from src.controller.ApplicationWindow import ApplicationWindow


def test_action_entry_pickup_push_button(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    assert widget.isHidden() == True


def test_action_show_result_push_button(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)
    assert widget.isHidden() == True
    widget.showResultWindow.close()


def test_application_window(qtbot,mocker):
    mocker.patch('src.controller.ApplicationWindow.Chafonrfid.get_tid', return_value="ABCDEFGIJKLMOPQ")
    widget = ApplicationWindow()
    
    qtbot.mouseClick(widget.ui.rfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    assert widget.ui.rfidLineEdit.text() == "ABCDEFGIJKLMOPQ"


def test_action_rfid_push_button_no_chip(qtbot, mocker):
    mocker.patch('src.controller.ApplicationWindow.Chafonrfid.get_tid', return_value=None)
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.rfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    assert widget.ui.rfidLineEdit.text() == ""


def test_resize_text(qtbot):
    widget = ApplicationWindow()
    
    widget.resize(640, 480)
    widget.resize(320, 240)
    widget.resize(160, 80)
