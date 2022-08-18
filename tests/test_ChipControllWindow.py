import pytest, pytest_mock
from PyQt5 import QtCore
from PyQt5.QtTest import QTest

import src.controller.ApplicationWindow
from src.controller.ApplicationWindow import ApplicationWindow
from src.models.EntrypickupModel import EntrypickupModel
from tests.fixtures.jsons import *


def test_resize_text(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.LeftButton)
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

    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.LeftButton)
    mocker.patch('src.controller.ChipControllWindow.EntrypickupModel.get_entry_from_rfid', return_value='{}')
    all_field_is_empty(widget)


def test_clean_fields(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.LeftButton)
    widget.chipControllWindow.cleanFields()
    all_field_is_empty(widget)


def test_close_event(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.chipControllPushButton, QtCore.Qt.LeftButton)
    widget.chipControllWindow.close()
