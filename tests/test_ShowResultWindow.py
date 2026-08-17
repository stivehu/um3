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

    assert widget.showResultWindow.ui.webView.url().toString() == \
           'http://192.168.0.115/entry/scoreboard?rfid=ABCDEFGIJKLMOPQ'
    widget.showResultWindow.close()


def test_restores_result_list_after_read(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEFGIJKLMOPQ")
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.showResultWindow.scanrfid()
    widget.showResultWindow.restore_timer()

    assert widget.showResultWindow.ui.webView.url().toString() == 'http://192.168.0.115/entry/result'
    widget.showResultWindow.close()


def test_no_scoreboard_without_chip(qtbot, mocker):
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value=None)
    widget = ApplicationWindow()

    qtbot.mouseClick(widget.ui.showResultPushButton, QtCore.Qt.MouseButton.LeftButton)
    widget.showResultWindow.scanrfid()

    assert widget.showResultWindow.ui.webView.url().toString() == 'http://192.168.0.115/entry/result'
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
