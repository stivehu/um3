from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QDialog)

from src.chafonrfid.Chafonrfid import Chafonrfid
from src.models.EntrypickupModel import EntrypickupModel
from src.models.MyJson import MyJson
from src.models.SettingsModel import SettingsModel
from src.views.chipcontroll.chipcontroll import Ui_Form


class ChipControllWindow(QDialog):
    def __init__(self, parent=None):
        super(ChipControllWindow, self).__init__(parent)
        self.ui = Ui_Form()
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
        if self.__settings.get_auto_maximize_opening_window() == True:
            self.showMaximized()

    def resizeText(self, event):
        defaultSize = 14
        if self.rect().width() // 40 > defaultSize:
            font = QFont('', self.rect().width() // 40)
        else:
            font = QFont('', defaultSize)
        self.ui.startnumLineEdit.setFont(font)
        self.ui.genderLabel.setFont(font)
        self.ui.startNumLabel.setFont(font)
        self.ui.firstnameLabel.setFont(font)
        self.ui.firstnameLineEdit.setFont(font)
        self.ui.agegroupLineEdit.setFont(font)
        self.ui.lastnameLineEdit.setFont(font)
        self.ui.genderLineEdit.setFont(font)
        self.ui.pickedupLabel.setFont(font)
        self.ui.pickedupLineEdit.setFont(font)
        self.ui.lastnameLabel.setFont(font)
        self.ui.distanceLabel.setFont(font)
        self.ui.distanceLineEdit.setFont(font)
        self.ui.agegroupLabel.setFont(font)
        self.ui.statusBar.setFont(font)

    def initResize(self):
        self.ui.startnumLineEdit.resizeEvent = self.resizeText
        self.ui.genderLabel.resizeEvent = self.resizeText
        self.ui.startNumLabel.resizeEvent = self.resizeText
        self.ui.firstnameLabel.resizeEvent = self.resizeText
        self.ui.firstnameLineEdit.resizeEvent = self.resizeText
        self.ui.agegroupLineEdit.resizeEvent = self.resizeText
        self.ui.lastnameLineEdit.resizeEvent = self.resizeText
        self.ui.genderLineEdit.resizeEvent = self.resizeText
        self.ui.pickedupLabel.resizeEvent = self.resizeText
        self.ui.pickedupLineEdit.resizeEvent = self.resizeText
        self.ui.lastnameLabel.resizeEvent = self.resizeText
        self.ui.distanceLabel.resizeEvent = self.resizeText
        self.ui.distanceLineEdit.resizeEvent = self.resizeText
        self.ui.agegroupLabel.resizeEvent = self.resizeText
        self.ui.statusBar.resizeEvent = self.resizeText

    def scanrfid(self):
        self.readRfid()
        entry = None
        if self.__rfid is not None:
            entry = MyJson.loads(self.__entrypickupModel.get_entry_from_rfid(self.__rfid))
        if EntrypickupModel.checkFormat(entry):
            self.fillFields(entry)
        else:
            self.cleanFields()


    def fillFields(self, entry: dict):
        self.ui.distanceLineEdit.setText(entry['distance'])
        self.ui.startnumLineEdit.setText(str(entry['startnum']))
        self.ui.firstnameLineEdit.setText(entry['firstname'])
        self.ui.lastnameLineEdit.setText(entry['lastname'])
        self.ui.genderLineEdit.setText(entry['gender'])
        self.ui.agegroupLineEdit.setText(entry['agegroup'])
        self.ui.pickedupLineEdit.setText(entry['pickedupstate'])
        if str(entry['pickedUp']) == 'True':
            self.ui.distanceLineEdit.parent().setStyleSheet(None)
        else:
            self.ui.distanceLineEdit.parent().setStyleSheet('background-color: rgb(239, 41, 41);')  # piros

    def cleanFields(self):
        self.ui.startnumLineEdit.setText(None)
        self.ui.distanceLineEdit.setText(None)
        self.ui.firstnameLineEdit.setText(None)
        self.ui.lastnameLineEdit.setText(None)
        self.ui.genderLineEdit.setText(None)
        self.ui.agegroupLineEdit.setText(None)
        self.ui.pickedupLineEdit.setText(None)
        self.ui.distanceLineEdit.parent().setStyleSheet(None)

    def readRfid(self):
        __chafonrfid = Chafonrfid()
        self.__rfid = __chafonrfid.get_tid()
        if __chafonrfid.error is not None:
            self.ui.statusBar.setText(__chafonrfid.error)
        else:
            self.ui.statusBar.setText(None)

    def closeEvent(self, event):
        self.timer.stop()
        self.parent().show()
        self.close()
