from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

from src.chafonrfid.Chafonrfid import Chafonrfid
from src.controller.ChipControllWindow import ChipControllWindow
from src.controller.EntrypickupWindow import EntrypickupWindow
from src.views.mainwindow.mainwindow import Ui_UserMangerUi


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_UserMangerUi()
        self.ui.setupUi(self)
        self.connectSignalsSlots()
        self.initResize()
        self.__rfid = None

    def connectSignalsSlots(self):
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.rfidPushButton.clicked.connect(self.actionRfidPushButton)
        self.ui.entryPickupPushButton.clicked.connect(self.actionEntryPickupPushButton)
        self.ui.chipControllPushButton.clicked.connect(self.actionChipControllPushButton)

    def initResize(self):
        self.ui.localEntrypushButton.resizeEvent = self.resizeText
        self.ui.entryPickupPushButton.resizeEvent = self.resizeText
        self.ui.chipControllPushButton.resizeEvent = self.resizeText
        self.ui.showResultPushButton.resizeEvent = self.resizeText
        self.ui.rfidPushButton.resizeEvent = self.resizeText
        self.ui.rfidLineEdit.resizeEvent = self.resizeText
        self.ui.preEntryPushButton.resizeEvent = self.resizeText
        self.ui.settingPushButton.resizeEvent = self.resizeText

    def resizeText(self, event):
        defaultSize = 14
        if self.rect().width() // 14 > defaultSize:
            font = QFont('', self.rect().width() // 14)
        else:
            font = QFont('', defaultSize)
        self.ui.localEntrypushButton.setFont(font)
        self.ui.entryPickupPushButton.setFont(font)
        self.ui.chipControllPushButton.setFont(font)
        self.ui.showResultPushButton.setFont(font)
        self.ui.rfidPushButton.setFont(font)
        self.ui.rfidLineEdit.setFont(font)
        self.ui.preEntryPushButton.setFont(font)
        self.ui.settingPushButton.setFont(font)

    def actionEntryPickupPushButton(self):
        self.hide()
        self.entrypickupWindow = EntrypickupWindow(self)
        self.entrypickupWindow.show()

    def actionChipControllPushButton(self):
        self.hide()
        otherview = ChipControllWindow(self)
        otherview.show()

    def actionRfidPushButton(self):
        self.readRfid()
        self.ui.rfidLineEdit.setText(self.__rfid)

    def readRfid(self):
        __chafonrfid = Chafonrfid()
        self.__rfid = __chafonrfid.get_tid()
        if __chafonrfid.error is not None:
            self.ui.statusbar.showMessage(__chafonrfid.error)
        else:
            self.ui.statusbar.showMessage(None)
