import time

import pytest, pytest_mock
from PyQt6 import QtCore

from src.controller.ApplicationWindow import ApplicationWindow


@pytest.fixture(autouse=True)
def isolated_conf(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)


def test_shows_result_list_on_open(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)

    assert widget.showResultWindow.ui.webView.url().toString() == 'http://192.168.0.115/entry/result'
    widget.showResultWindow.close()


def test_shows_scoreboard_on_rfid_read(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEFGIJKLMOPQ")
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.showResultWindow.scanrfid()

    qtbot.waitUntil(lambda: widget.showResultWindow.ui.webView.url().toString() ==
                             'http://192.168.0.115/entry/scoreboard?rfid=ABCDEFGIJKLMOPQ', timeout=2000)
    widget.showResultWindow.close()


def test_restores_result_list_after_read(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEFGIJKLMOPQ")
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.showResultWindow.scanrfid()
    qtbot.waitUntil(lambda: widget.showResultWindow.ui.webView.url().toString() ==
                             'http://192.168.0.115/entry/scoreboard?rfid=ABCDEFGIJKLMOPQ', timeout=2000)
    widget.showResultWindow.restore_timer()

    assert widget.showResultWindow.ui.webView.url().toString() == 'http://192.168.0.115/entry/result'
    widget.showResultWindow.close()


def test_no_scoreboard_without_chip(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value=None)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)
    spy = mocker.spy(widget.showResultWindow, '_ShowResultWindow__onRfidRead')

    widget.showResultWindow.scanrfid()
    qtbot.waitUntil(lambda: spy.called, timeout=2000)

    assert widget.showResultWindow.ui.webView.url().toString() == 'http://192.168.0.115/entry/result'
    widget.showResultWindow.close()


def test_scanrfid_ignores_overlapping_calls_while_reading(qtbot, mocker):
    call_count = {'n': 0}

    def slow_get_tid(self):
        call_count['n'] += 1
        time.sleep(0.3)
        return "ABCDEFGIJKLMOPQ"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.showResultWindow.timer.stop()

    widget.showResultWindow.scanrfid()
    widget.showResultWindow.scanrfid()
    qtbot.waitUntil(lambda: widget.showResultWindow.ui.webView.url().toString() ==
                             'http://192.168.0.115/entry/scoreboard?rfid=ABCDEFGIJKLMOPQ', timeout=2000)

    assert call_count['n'] == 1
    widget.showResultWindow.close()


def test_close_event_while_read_in_flight_does_not_crash(qtbot, mocker):
    def slow_get_tid(self):
        time.sleep(0.2)
        return "ABCDEFGIJKLMOPQ"

    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)

    widget.showResultWindow.scanrfid()
    widget.showResultWindow.close()


def test_resize_text(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.showResultWindow.resize(640, 480)
    widget.showResultWindow.resize(320, 240)
    widget.showResultWindow.resize(160, 80)
    widget.showResultWindow.close()


def test_close_event(qtbot):
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.showResultWindow.close()

    assert widget.isHidden() == False
