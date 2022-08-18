from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QDialog)

from src.chafonrfid.Chafonrfid import Chafonrfid
from src.models.EntrypickupModel import EntrypickupModel
from src.models.MyJson import MyJson
from src.models.SettingsModel import SettingsModel
from src.views.sendresult.sendresult import Ui_sendresultForm


class SendresultWindow(QDialog):
    def __init__(self, parent=None):
        super(SendresultWindow, self).__init__(parent)
        self.ui = Ui_sendresultForm()
        self.ui.setupUi(self)
        self.__rfid = None
        self.__entrypickupModel = EntrypickupModel()
        self.__settings = SettingsModel()
        self.initResize()
        self.initTimer()
        self.maximizeWindow()

    def initTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.scanrfid)

        self.timer.start(self.__settings.get_chipcontroll_interval())

    def maximizeWindow(self):
        if self.__settings.get_auto_maximize_opening_window():
            self.showMaximized()

    def resizeText(self, event):
        defaultSize = 14
        if self.rect().width() // 40 > defaultSize:
            font = QFont('', self.rect().width() // 40)
        else:
            font = QFont('', defaultSize)
        self.ui.startnumLineEdit.setFont(font)
        self.ui.startNumLabel.setFont(font)
        self.ui.firstnameLabel.setFont(font)
        self.ui.firstnameLineEdit.setFont(font)
        self.ui.lastnameLabel.setFont(font)
        self.ui.distanceLabel.setFont(font)
        self.ui.timestampLineEdit.setFont(font)
        self.ui.timestampLabel.setFont(font)
        self.ui.statusBar.setFont(font)

    def initResize(self):
        if self.__settings.get_auto_resize_window():
            self.ui.startnumLineEdit.resizeEvent = self.resizeText
            self.ui.startNumLabel.resizeEvent = self.resizeText
            self.ui.firstnameLabel.resizeEvent = self.resizeText
            self.ui.firstnameLineEdit.resizeEvent = self.resizeText
            self.ui.lastnameLineEdit.resizeEvent = self.resizeText
            self.ui.lastnameLabel.resizeEvent = self.resizeText
            self.ui.statusBar.resizeEvent = self.resizeText
            self.ui.timestampLineEdit.resizeEvent = self.resizeText
            self.ui.timestampLabel.resizeEvent = self.resizeText

    def scanrfid(self):
        self.readRfid()
        entry = None
        if self.__rfid is not None:
            entry = MyJson.loads(self.__entrypickupModel.create_entry_timestamp_from_rfid(self.__rfid))
        if EntrypickupModel.checkFormat(entry):
            self.fillFields(entry)
        # else:
        #     self.cleanFields()

    def fillFields(self, entry: dict):
        self.ui.startnumLineEdit.setText(str(entry['startnum']))
        self.ui.firstnameLineEdit.setText(entry['firstname'])
        self.ui.lastnameLineEdit.setText(entry['lastname'])
        self.ui.timestampLineEdit.setText(entry['timestamp'])

    def readRfid(self):
        __chafonrfid = Chafonrfid(self.__settings.get_comm_port())
        self.__rfid = __chafonrfid.get_tid()
        if __chafonrfid.error is not None:
            self.ui.statusBar.setText(__chafonrfid.error)
        else:
            self.ui.statusBar.setText(None)

    def closeEvent(self, event):
        self.timer.stop()
        self.parent().show()
        self.close()
