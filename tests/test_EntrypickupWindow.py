import time

import pytest, pytest_mock
from PyQt6 import QtCore

from src.controller.ApplicationWindow import ApplicationWindow
from src.models.EntrypickupModel import EntrypickupModel
from tests.fixtures.jsons import *


def test_action_read_rfid_push_button_picked_down(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickdownPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                 return_value=entries_pickedup)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.waitUntil(lambda: widget.entrypickupWindow.ui.startnumLineEdit.text() != '', timeout=2000)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickdownPushButton, QtCore.Qt.MouseButton.LeftButton)


def test_action_read_rfid_push_button_picked_up(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                 return_value=entries_pickeddown)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.waitUntil(lambda: widget.entrypickupWindow.ui.startnumLineEdit.text() != '', timeout=2000)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)


def test_action_read_rfid_push_button_picked_up_and_down(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                 return_value=entries_pickeddown)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.waitUntil(lambda: widget.entrypickupWindow.ui.startnumLineEdit.text() != '', timeout=2000)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                 return_value=entries_pickedup)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.waitUntil(lambda: widget.entrypickupWindow.ui.pickedupLineEdit.text() != '', timeout=2000)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickdownPushButton, QtCore.Qt.MouseButton.LeftButton)


def test_action_read_rfid_push_button_empty(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                 return_value='{}')
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.wait(300)


def test_action_read_rfid_push_badformat_result(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                 return_value=entries_badformat)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.wait(300)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickdownPushButton, QtCore.Qt.MouseButton.LeftButton)


def test_close_event(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.entrypickupWindow.close()


def test_resize_text(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.entrypickupWindow.resize(640, 480)
    widget.entrypickupWindow.resize(320, 240)
    widget.entrypickupWindow.resize(160, 80)


def test_clean_fields(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.entrypickupWindow.cleanFields()
    assert widget.entrypickupWindow.ui.startnumLineEdit.text() == ''
    assert widget.entrypickupWindow.ui.distanceLineEdit.text() == ''
    assert widget.entrypickupWindow.ui.firstnameLineEdit.text() == ''
    assert widget.entrypickupWindow.ui.lastnameLineEdit.text() == ''
    assert widget.entrypickupWindow.ui.genderLineEdit.text() == ''
    assert widget.entrypickupWindow.ui.agegroupLineEdit.text() == ''
    assert widget.entrypickupWindow.ui.pickedupLineEdit.text() == ''


def test_action_entry_pickup_push_button(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)


def test_action_entry_pickdown_push_button(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)


def test_action_read_rfid_push_button_does_not_block_ui_thread(qtbot, mocker):
    def slow_get_tid(self):
        time.sleep(0.3)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                 return_value=entries_pickedup)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)

    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.MouseButton.LeftButton)

    assert widget.entrypickupWindow.ui.startnumLineEdit.text() == ''
    qtbot.waitUntil(lambda: widget.entrypickupWindow.ui.startnumLineEdit.text() != '', timeout=2000)


def test_action_read_rfid_push_button_ignores_overlapping_calls_while_reading(qtbot, mocker):
    call_count = {'n': 0}

    def slow_get_tid(self):
        call_count['n'] += 1
        time.sleep(0.3)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid',
                 return_value=entries_pickedup)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)

    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.waitUntil(lambda: widget.entrypickupWindow.ui.startnumLineEdit.text() != '', timeout=2000)

    assert call_count['n'] == 1


def test_close_event_while_read_in_flight_does_not_crash(qtbot, mocker):
    def slow_get_tid(self):
        time.sleep(0.2)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.MouseButton.LeftButton)

    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.entrypickupWindow.close()
