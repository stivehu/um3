from src.controller.ApplicationWindow import ApplicationWindow
from PyQt5 import QtCore


def test_setting_window(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.settingPushButton, QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.settingsWindow.ui.savePushButton, QtCore.Qt.LeftButton)
