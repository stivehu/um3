import time

from PyQt6 import QtCore

from src.controller.ApplicationWindow import ApplicationWindow


def open_window(qtbot, mocker):
    mocker.patch('src.models.RemoteApiModel.RemoteApiModel.sendAjaxRequest', return_value=[])
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.inTheBoxesPushButton, QtCore.Qt.MouseButton.LeftButton)
    return widget


def test_close_event(qtbot, mocker):
    widget = open_window(qtbot, mocker)
    widget.showInTheBoxes.close()


def test_scanrfid_transient_error_does_not_stop_timer(qtbot, mocker):
    widget = open_window(qtbot, mocker)
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', side_effect=Exception('port error'))

    widget.showInTheBoxes.scanrfid()
    qtbot.waitUntil(lambda: widget.showInTheBoxes.ui.statusBar.text() == 'port error', timeout=2000)

    assert widget.showInTheBoxes.timer.isActive()


def test_scanrfid_success_updates_boxes(qtbot, mocker):
    widget = open_window(qtbot, mocker)
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', return_value="ABCDEF")
    setinthebox = mocker.patch('src.controller.ShowInTheBoxesWindow.EntryModel.setinthebox')
    intheboxlist = mocker.patch('src.controller.ShowInTheBoxesWindow.IntheboxModel.list')

    widget.showInTheBoxes.scanrfid()
    qtbot.waitUntil(lambda: setinthebox.called, timeout=2000)

    setinthebox.assert_called_once_with('rfid', 'ABCDEF')
    assert intheboxlist.call_count >= 1


def test_scanrfid_does_not_block_ui_thread(qtbot, mocker):
    # A soros port olvasása másodpercekig blokkolhat (SerialTransport
    # timeout=5s) -- ha a scanrfid szinkron lenne, ez lefagyasztaná a teljes
    # ablakot. Ez a teszt azt igazolja, hogy a scanrfid() azonnal visszatér,
    # a tényleges olvasás háttérszálon fut.
    def slow_get_tid(self):
        time.sleep(0.3)
        return "ABCDEF"

    widget = open_window(qtbot, mocker)
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    setinthebox = mocker.patch('src.controller.ShowInTheBoxesWindow.EntryModel.setinthebox')

    widget.showInTheBoxes.scanrfid()

    assert not setinthebox.called
    qtbot.waitUntil(lambda: setinthebox.called, timeout=2000)


def test_scanrfid_ignores_overlapping_calls_while_reading(qtbot, mocker):
    call_count = {'n': 0}

    def slow_get_tid(self):
        call_count['n'] += 1
        time.sleep(0.3)
        return "ABCDEF"

    widget = open_window(qtbot, mocker)
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)
    setinthebox = mocker.patch('src.controller.ShowInTheBoxesWindow.EntryModel.setinthebox')
    widget.showInTheBoxes.timer.stop()

    widget.showInTheBoxes.scanrfid()
    widget.showInTheBoxes.scanrfid()
    qtbot.waitUntil(lambda: setinthebox.called, timeout=2000)

    assert call_count['n'] == 1


def test_close_event_while_read_in_flight_does_not_crash(qtbot, mocker):
    def slow_get_tid(self):
        time.sleep(0.2)
        return "ABCDEF"

    widget = open_window(qtbot, mocker)
    mocker.patch('src.chafonrfid.Chafonrfid.Chafonrfid.get_tid', slow_get_tid)

    widget.showInTheBoxes.scanrfid()
    widget.showInTheBoxes.close()
