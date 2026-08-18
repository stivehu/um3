import time

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
    qtbot.waitUntil(lambda: widget.ui.rfidLineEdit.text() == "ABCDEFGIJKLMOPQ", timeout=2000)


def test_action_rfid_push_button_no_chip(qtbot, mocker):
    mocker.patch('src.controller.ApplicationWindow.Chafonrfid.get_tid', return_value=None)
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.rfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.waitUntil(lambda: widget._ApplicationWindow__reading_rfid == False, timeout=2000)
    assert widget.ui.rfidLineEdit.text() == ""


def test_scanrfid_does_not_block_ui_thread(qtbot, mocker):
    def slow_get_tid(self):
        time.sleep(0.3)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.rfidPushButton, QtCore.Qt.MouseButton.LeftButton)

    assert widget.ui.rfidLineEdit.text() == ""
    qtbot.waitUntil(lambda: widget.ui.rfidLineEdit.text() == "ABCDEF", timeout=2000)


def test_action_rfid_push_button_ignores_overlapping_calls_while_reading(qtbot, mocker):
    call_count = {'n': 0}

    def slow_get_tid(self):
        call_count['n'] += 1
        time.sleep(0.3)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.rfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.ui.rfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.waitUntil(lambda: widget.ui.rfidLineEdit.text() == "ABCDEF", timeout=2000)

    assert call_count['n'] == 1


def test_resize_text(qtbot):
    widget = ApplicationWindow()
    
    widget.resize(640, 480)
    widget.resize(320, 240)
    widget.resize(160, 80)
