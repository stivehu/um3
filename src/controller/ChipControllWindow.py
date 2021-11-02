# from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import (QDialog)

from src.views.chipcontroll.chipcontroll import Ui_Form


class ChipControllWindow(QDialog):
    def __init__(self, parent=None):
        super(ChipControllWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        pass

    def closeEvent(self, event):
        self.parent().show()
        self.close()
