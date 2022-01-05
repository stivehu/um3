from unittest import TestCase
from src.controller.ApplicationWindow import ApplicationWindow
from PyQt5 import QtCore


def test_ShowReadInTheBoxesWindow(qtbot):
    widget = ApplicationWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.ui.inTheBoxesPushButton, QtCore.Qt.LeftButton)
    widget.showInTheBoxes.ui.startnumLineEdit.setText('5105')


