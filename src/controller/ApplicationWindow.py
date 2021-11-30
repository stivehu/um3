from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

from src.chafonrfid.Chafonrfid import Chafonrfid
from src.controller.ChipControllWindow import ChipControllWindow
from src.controller.EntrypickupWindow import EntrypickupWindow
from src.controller.LocalentryWindow import LocalentryWindow
from src.controller.SettingsWindow import SettingsWindow
from src.models.SettingsModel import SettingsModel
from src.views.mainwindow.mainwindow import Ui_UserMangerUi


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_UserMangerUi()
        self.ui.setupUi(self)
        self.connectSignalsSlots()
        self.__settings = SettingsModel()
        self.initResize()
        self.__rfid = None

    def connectSignalsSlots(self):
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.rfidPushButton.clicked.connect(self.actionRfidPushButton)
        self.ui.entryPickupPushButton.clicked.connect(self.actionEntryPickupPushButton)
        self.ui.chipControllPushButton.clicked.connect(self.actionChipControllPushButton)
        self.ui.localEntrypushButton.clicked.connect(self.actionLocalentryPushButton)
        self.ui.settingPushButton.clicked.connect(self.actionSettingsPushButton)

    def initResize(self):
        if self.__settings.get_auto_resize_window():
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


    def actionSettingsPushButton(self):
        self.hide()
        self.settingsWindow = SettingsWindow(self, settingsModel)
        self.settingsWindow.show()

    def actionChipControllPushButton(self):
        self.hide()
        self.chipControllWindow = ChipControllWindow(self)
        self.chipControllWindow.show()

    def actionLocalentryPushButton(self):
        self.hide()
        self.localentry = LocalentryWindow(self)
        self.localentry.show()

    def actionRfidPushButton(self):
        self.readRfid()
        self.ui.rfidLineEdit.setText(self.__rfid)

    def readRfid(self):
        self.__settings = SettingsModel()
        __chafonrfid = Chafonrfid(self.__settings.get_comm_port())
        self.__rfid = __chafonrfid.get_tid()
        if __chafonrfid.error is not None:
            self.ui.statusbar.showMessage(__chafonrfid.error)
        else:
            self.ui.statusbar.showMessage(None)
