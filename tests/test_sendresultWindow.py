import time

import pytest, pytest_mock
from PyQt6 import QtCore
from PyQt6.QtTest import QTest

import src.controller.ApplicationWindow
from src.controller.ApplicationWindow import ApplicationWindow
from src.models.EntrypickupModel import EntrypickupModel
from tests.fixtures.jsons import *

entry_with_timestamp = '{  "startnum": "100",  "distance": "10 km",  "firstname": "Teszt",  "lastname": "Elek",  "gender": "Nő",  "gender_id": "2",  "agegroup": "7-15 Év",  "pickedUp": "True",  "pickedupstate": "Felvette",  "timestamp": "2026-08-18 12:00:00"}'


def test_resize_text(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.sendresultPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.sendresultWindow.resize(640, 480)
    widget.sendresultWindow.resize(320, 240)
    widget.sendresultWindow.resize(160, 80)


def all_field_is_empty(widget):
    assert widget.sendresultWindow.ui.startnumLineEdit.text() == ''
    assert widget.sendresultWindow.ui.firstnameLineEdit.text() == ''
    assert widget.sendresultWindow.ui.lastnameLineEdit.text() == ''


def test_empty_fields(qtbot, mocker):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.sendresultPushButton, QtCore.Qt.MouseButton.LeftButton)
    mocker.patch('src.controller.SendresultWindow.EntrypickupModel.create_entry_timestamp_from_rfid',
                  return_value='{}')
    all_field_is_empty(widget)


def test_close_event(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.sendresultPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.sendresultWindow.close()


def test_scanrfid_does_not_block_ui_thread(qtbot, mocker):
    # A soros port olvasása másodpercekig blokkolhat (SerialTransport
    # timeout=5s) -- ha a scanrfid szinkron lenne, ez lefagyasztaná a teljes
    # ablakot. Ez a teszt azt igazolja, hogy a scanrfid() azonnal visszatér,
    # a tényleges olvasás háttérszálon fut.
    def slow_get_tid(self):
        time.sleep(0.3)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    mocker.patch('src.controller.SendresultWindow.EntrypickupModel.create_entry_timestamp_from_rfid',
                  return_value=entry_with_timestamp)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.sendresultPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.sendresultWindow.scanrfid()

    assert widget.sendresultWindow.ui.startnumLineEdit.text() == ""
    qtbot.waitUntil(lambda: widget.sendresultWindow.ui.startnumLineEdit.text() == "100", timeout=2000)


def test_scanrfid_ignores_overlapping_calls_while_reading(qtbot, mocker):
    call_count = {'n': 0}

    def slow_get_tid(self):
        call_count['n'] += 1
        time.sleep(0.3)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    mocker.patch('src.controller.SendresultWindow.EntrypickupModel.create_entry_timestamp_from_rfid',
                  return_value=entry_with_timestamp)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.sendresultPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.sendresultWindow.timer.stop()

    widget.sendresultWindow.scanrfid()
    widget.sendresultWindow.scanrfid()
    qtbot.waitUntil(lambda: widget.sendresultWindow.ui.startnumLineEdit.text() == "100", timeout=2000)

    assert call_count['n'] == 1


def test_close_event_while_read_in_flight_does_not_crash(qtbot, mocker):
    def slow_get_tid(self):
        time.sleep(0.2)
        return "ABCDEF"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.sendresultPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.sendresultWindow.scanrfid()
    widget.sendresultWindow.close()
