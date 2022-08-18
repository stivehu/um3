from src.controller.ApplicationWindow import ApplicationWindow
from PyQt5 import QtCore


def test_ShowReadInTheBoxesWindow(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.inTheBoxesPushButton, QtCore.Qt.LeftButton)
    widget.showInTheBoxes.ui.startnumLineEdit.setText('5105')