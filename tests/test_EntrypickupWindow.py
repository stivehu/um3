from unittest.mock import MagicMock

from PyQt5 import QtCore

from src.controller.ApplicationWindow import ApplicationWindow
from src.models.EntrypickupModel import EntrypickupModel
from tests.fixtures.jsons import *


def test_action_read_rfid_push_button_picked_down(qtbot):
    widget = ApplicationWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickdownPushButton, QtCore.Qt.LeftButton)

    EntrypickupModel.get_entry_from_rfid = MagicMock(return_value=entries_pickedup)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickdownPushButton, QtCore.Qt.LeftButton)


def test_action_read_rfid_push_button_picked_up(qtbot):
    widget = ApplicationWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickupPushButton, QtCore.Qt.LeftButton)

    EntrypickupModel.get_entry_from_rfid = MagicMock(return_value=entries_pickeddown)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickupPushButton, QtCore.Qt.LeftButton)

def test_action_read_rfid_push_button_picked_up_and_down(qtbot):
    widget = ApplicationWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickupPushButton, QtCore.Qt.LeftButton)

    EntrypickupModel.get_entry_from_rfid = MagicMock(return_value=entries_pickeddown)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
    EntrypickupModel.get_entry_from_rfid = MagicMock(return_value=entries_pickedup)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickdownPushButton, QtCore.Qt.LeftButton)

def test_action_read_rfid_push_button_empty(qtbot):
    widget = ApplicationWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
    EntrypickupModel.get_entry_from_rfid = MagicMock(return_value='{}')
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.LeftButton)


def test_action_read_rfid_push_badformat_result(qtbot):
    widget = ApplicationWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
    EntrypickupModel.get_entry_from_rfid = MagicMock(return_value=entries_badformat)
    qtbot.mouseClick(widget.entrypickupWindow.ui.readRfidPushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.entrypickupWindow.ui.entryPickdownPushButton, QtCore.Qt.LeftButton)


def test_close_event(qtbot):
    widget = ApplicationWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
    widget.entrypickupWindow.close()


def test_resize_text(qtbot):
    widget = ApplicationWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
    widget.entrypickupWindow.resize(640, 480)
    widget.entrypickupWindow.resize(320, 240)
    widget.entrypickupWindow.resize(160, 80)


def test_clean_fields(qtbot):
    widget = ApplicationWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
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
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.LeftButton)


def test_action_entry_pickdown_push_button(qtbot):
    widget = ApplicationWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.entryPickupPushButton, QtCore.Qt.LeftButton)
