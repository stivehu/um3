import pyperclip
from PyQt6 import QtWidgets

from src.chafonrfid.Chafonrfid import Chafonrfid
from src.controller.ChipControllWindow import ChipControllWindow
from src.controller.EntrypickupWindow import EntrypickupWindow
from src.controller.LocalentryWindow import LocalentryWindow
from src.controller.PreentryWindow import PreentryWindow
from src.controller.SendresultWindow import SendresultWindow
from src.controller.SettingsWindow import SettingsWindow
from src.controller.ShowInTheBoxesWindow import ShowInTheBoxesWindow
from src.controller.ShowResultWindow import ShowResultWindow
from src.controller.WindowMixin import RfidReaderMixin, ResizeFontMixin
from src.models.SettingsModel import SettingsModel
from src.views.mainwindow.mainwindow import Ui_UserMangerUi


class ApplicationWindow(QtWidgets.QMainWindow, RfidReaderMixin, ResizeFontMixin):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_UserMangerUi()
        self.ui.setupUi(self)
        self.connectSignalsSlots()
        self.__settings = SettingsModel()
        self.initResize()
        self.__rfid = None
        self.__reading_rfid = False
        self.__read_worker = None

    def connectSignalsSlots(self):
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.rfidPushButton.clicked.connect(self.actionRfidPushButton)
        self.ui.entryPickupPushButton.clicked.connect(self.actionEntryPickupPushButton)
        self.ui.chipControllPushButton.clicked.connect(self.actionChipControllPushButton)
        self.ui.localEntrypushButton.clicked.connect(self.actionLocalentryPushButton)
        self.ui.settingPushButton.clicked.connect(self.actionSettingsPushButton)
        self.ui.inTheBoxesPushButton.clicked.connect(self.actionInTheBoxesPushButton)
        self.ui.preEntryPushButton.clicked.connect(self.actionPreentryPushButton)
        self.ui.sendresultPushButton.clicked.connect(self.actionSendresultPushButton)
        self.ui.showResultPushButton.clicked.connect(self.actionShowResultPushButton)
        self.ui.timesyncPushButton.clicked.connect(self.actionTimesync)
        self.ui.exitPushButton.clicked.connect(self.close)

    def actionSendresultPushButton(self):
        self.hide()
        self.sendresultWindow = SendresultWindow(self)
        self.sendresultWindow.show()
        self.sendresultWindow.activateWindow()

    def actionShowResultPushButton(self):
        self.hide()
        self.showResultWindow = ShowResultWindow(self)
        self.showResultWindow.show()
        self.showResultWindow.activateWindow()

    def actionInTheBoxesPushButton(self):
        self.hide()
        self.showInTheBoxes = ShowInTheBoxesWindow(self)
        self.showInTheBoxes.show()
        self.showInTheBoxes.activateWindow()

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
            self.ui.exitPushButton.resizeEvent = self.resizeText

    def resizeText(self, event):
        font = self._resizeFont(divisor=14)
        self.ui.localEntrypushButton.setFont(font)
        self.ui.entryPickupPushButton.setFont(font)
        self.ui.chipControllPushButton.setFont(font)
        self.ui.showResultPushButton.setFont(font)
        self.ui.rfidPushButton.setFont(font)
        self.ui.rfidLineEdit.setFont(font)
        self.ui.preEntryPushButton.setFont(font)
        self.ui.settingPushButton.setFont(font)
        self.ui.exitPushButton.setFont(font)

    def actionEntryPickupPushButton(self):
        self.hide()
        self.entrypickupWindow = EntrypickupWindow(self)
        self.entrypickupWindow.show()

    def actionSettingsPushButton(self):
        self.hide()
        self.settingsWindow = SettingsWindow(self)
        self.settingsWindow.show()

    def actionChipControllPushButton(self):
        self.hide()
        self.chipControllWindow = ChipControllWindow(self)
        self.chipControllWindow.show()
        self.chipControllWindow.activateWindow()

    def actionLocalentryPushButton(self):
        self.hide()
        self.localentry = LocalentryWindow(self)
        self.localentry.show()

    def actionPreentryPushButton(self):
        self.hide()
        self.preentry = PreentryWindow(self)
        self.preentry.show()

    def actionRfidPushButton(self):
        self.readRfid()

    def actionTimesync(self):
        from src.Timesync.src.TimeClient import TimeClient
        timeClient = TimeClient(self.__settings.get_server_ip())
        timeClient.run()
        if timeClient.error==None:
            self.ui.statusbar.showMessage(timeClient.servertime,3000)
        else:
            self.ui.statusbar.showMessage(timeClient.error, 3000)

    def readRfid(self):
        if self.__reading_rfid:
            return
        self.__reading_rfid = True
        self.__settings = SettingsModel()
        self.__read_worker = self._readTidAsync(self.__settings.get_comm_port(), self.__onRfidRead)

    def __onRfidRead(self, rfid, error):
        self.__reading_rfid = False
        self.__read_worker = None
        self.ui.statusbar.showMessage(error)
        self.__rfid = rfid
        if isinstance(self.__rfid, str):
            pyperclip.copy(self.__rfid)
            self.ui.rfidLineEdit.setText(self.__rfid)

    def closeEvent(self, event):
        exit()

