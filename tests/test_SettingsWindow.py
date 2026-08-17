from src.controller.ApplicationWindow import ApplicationWindow
from PyQt6 import QtCore


def test_setting_window(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.settingPushButton, QtCore.Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.settingsWindow.ui.savePushButton, QtCore.Qt.MouseButton.LeftButton)
