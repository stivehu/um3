from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.chafonrfid.Chafonrfid import Chafonrfid
from src.models.AgegroupModel import AgegroupModel
from src.models.DistanceModel import DistanceModel
from src.models.EnrtyModel import EntryModel
from src.models.EntrypickupModel import EntrypickupModel
from src.models.GenderModel import GenderModel
from src.models.SettingsModel import SettingsModel
from src.views.preentry.preentry import Ui_PreentryForm
from datetime import datetime


class PreentryWindow(QDialog):
    def __init__(self, parent=None):
        super(PreentryWindow, self).__init__(parent)
        self.ui = Ui_PreentryForm()
        self.ui.setupUi(self)
        self.connectSignalsSlots()
        self.__startnum_is_updating = False
        self.__rfid = None
        self.__saved_rfid = False
        self.__entryModel = EntryModel()
        self.__settings = SettingsModel()
        self.__init_entry_site_url()
        self.initResize()
        self.maximizeWindow()
        self.try_auto_login()
        self.initTimer()
        self.ui.statusBar.setStyleSheet("font-weight: bold; color: red")

    def printErrorMessage(self, error):
        if (isinstance(error, str)):
            self.ui.statusBarLabel.setText(error)

    def maximizeWindow(self):
        if self.__settings.get_auto_maximize_opening_window() == True:
            self.showMaximized()

    def __init_entry_site_url(self):
        self.ui.urllineEdit.setText(self.__settings.get_entry_site_url())

    def connectSignalsSlots(self):
        self.ui.prevpushButton.clicked.connect(self.actionPrevButton)
        self.ui.nextpushButton.clicked.connect(self.actionNextButton)
        self.ui.readpushButton.clicked.connect(self.actionStartnumHeaderlineEdit)
        self.ui.insertpushButton.clicked.connect(self.actioninsertpushButton)
        self.ui.loginpushButton.clicked.connect(self.actionLoginForm)
        self.ui.savepushButton.clicked.connect(self.actionSavepushButton)
        self.ui.insertSaveNextpushButton.clicked.connect(self.actionInsertSaveNextpushButton)

    def actionInsertSaveNextpushButton(self):
        oldrfid = self.ui.rfidHeaderlineEdit.text()
        self.actioninsertpushButton()
        if self.ui.rfidHeaderlineEdit.text() == None or self.ui.rfidHeaderlineEdit.text() != oldrfid:
            if self.actionSavepushButton() == True:
                self.actionNextButton()

    def actionSavepushButton(self):
        startnum = self.ui.startnumlineEdit.text()
        rfid = self.ui.rfidlineEdit.text()
        self.__entryModel.update_rfid_from_startnum(startnum, rfid)
        if self.__entryModel.status_code != 200:
            self.ui.statusBar.setText(self.__entryModel.error)
            self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form", "%s Can't  save %s to %s") % (
            datetime.now().strftime("%H:%M:%S"), rfid, startnum))
            return False
        self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form", "%s Saved %s to %s") % (
            datetime.now().strftime("%H:%M:%S"), rfid, startnum))
        return True

    def actioninsertpushButton(self):
        self.ui.rfidlineEdit.setText(self.ui.rfidHeaderlineEdit.text())
        self.ui.rfidHeaderlineEdit.setText(None)
        self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form",
                                                                           "%s Insert %s to startnum %s") % (
                                                 datetime.now().strftime(
                                                     "%H:%M:%S"),
                                                 self.ui.rfidHeaderlineEdit.text(),
                                                 self.ui.startnumlineEdit.text()))

    def actionNextButton(self):
        if not self.ui.startnumHeaderlineEdit.text().isdigit():
            return
        self.__startnum_is_updating = True
        currentStartnum = int(self.ui.startnumHeaderlineEdit.text())
        nextStartnum = currentStartnum + 1
        self.ui.startnumHeaderlineEdit.setText(str(nextStartnum))
        self.readStartnum(str(nextStartnum))
        self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form",
                                                                           "%s Jump to %s") % (
                                                 datetime.now().strftime(
                                                     "%H:%M:%S"), nextStartnum))
        self.__startnum_is_updating = False

    def actionPrevButton(self):
        if not self.ui.startnumHeaderlineEdit.text().isdigit():
            return
        self.__startnum_is_updating = True
        currentStartnum = int(self.ui.startnumHeaderlineEdit.text())
        prevStartnum = currentStartnum - 1
        self.ui.startnumHeaderlineEdit.setText(str(prevStartnum))
        self.readStartnum(str(prevStartnum))
        self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form",
                                                                           "%s Jump to %s") % (
                                                 datetime.now().strftime(
                                                     "%H:%M:%S"), prevStartnum))
        self.__startnum_is_updating = False

    def actionLoginForm(self):
        username = self.ui.usernamelineEdit.text()
        password = self.ui.passwordlineEdit.text()
        if self.__entryModel.loginSite(username, password):
            self.setLoginButtonColor('green')
            self.storepassword(username, password)
            self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form",
                                                                               "%s logged id as %s") % (
                                                     datetime.now().strftime(
                                                         "%H:%M:%S"), username))
        else:
            self.setLoginButtonColor('red')

    def storepassword(self, username, password):
        if self.ui.storePasswordcheckBox.isChecked() == True:
            self.__settings.set_entry_site_username(username).set_entry_site_password(password)
            self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form",
                                                                               "%s Save password to %s") % (
                                                     datetime.now().strftime(
                                                         "%H:%M:%S"), username))
            self.__settings.save_config()

    def try_auto_login(self):
        username = self.__settings.get_entry_site_username()
        password = self.__settings.get_entry_site_password()
        if (username != False and password != False):
            self.ui.usernamelineEdit.setText(username)
            self.ui.passwordlineEdit.setText(password)
            self.actionLoginForm()
            self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form",
                                                                               "%s Autologin ") % (
                                                     datetime.now().strftime("%H:%M:%S")))

    def setLoginButtonColor(self, color):
        if color == 'red':
            brush = QBrush(QColor(255, 0, 0))
        else:
            brush = QBrush(QColor(0, 255, 0))
        palette = QPalette()
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        self.ui.loginpushButton.setPalette(palette)

    def actionStartnumHeaderlineEdit(self):
        if not self.__startnum_is_updating:
            self.readStartnum(self.ui.startnumHeaderlineEdit.text())

    def readStartnum(self, startnum):
        result = self.__entryModel.read_entry_from_startnum(startnum)
        if result == None and self.__entryModel.status_code == 302:
            self.setLoginButtonColor('red')
        elif self.__entryModel.status_code == 404:
            self.ui.firstnamelineEdit.setText('')
            self.ui.lastnamelineEdit.setText('')
            self.ui.rfidlineEdit.setText('')
            self.ui.distancelineEdit.setText('')
            self.ui.startnumlineEdit.setText('')
            self.ui.statusBar.setText(QCoreApplication.translate("Form", "Not exists startnum"))
        elif self.__entryModel.status_code == 200 and self.__entryModel.checkentryResult(result):
            self.ui.statusBar.setText(None)
            self.ui.firstnamelineEdit.setText(result['response']['firstname'])
            self.ui.lastnamelineEdit.setText(result['response']['lastname'])
            self.ui.rfidlineEdit.setText(result['response']['rfid'])
            self.ui.distancelineEdit.setText(result['response']['distance'])
            self.ui.startnumlineEdit.setText(result['response']['startnum'])
            self.checkPayedStatus(result)
            self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form", "%s Read %s")
                                                 % (datetime.now().strftime("%H:%M:%S"), startnum))

    def checkPayedStatus(self, result):
        if result['response']['payed'] != True:
            self.ui.statusBar.setText(QCoreApplication.translate("Form", "Not payed"))

    def initResize(self):
        if self.__settings.get_auto_resize_window():
            self.ui.startNumLabel.resizeEvent = self.resizeText

    def resizeText(self, event):
        defaultSize = 14
        if self.rect().width() // 40 > defaultSize:
            font = QFont('', self.rect().width() // 40)
        else:
            font = QFont('', defaultSize)

        for widgetTypes in self.__widget_dict.values():
            for widget in widgetTypes.values():
                widget.setFont(font)

    def readRfid(self):
        __chafonrfid = Chafonrfid(self.__settings.get_comm_port())
        self.__rfid = __chafonrfid.get_tid()
        if __chafonrfid.error is not None:
            self.ui.statusBarLabel.setText(__chafonrfid.error)

    def initTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.scanrfid)
        self.timer.start(self.__settings.get_chipcontroll_interval())

    def readRfid(self):
        try:
            __chafonrfid = Chafonrfid(self.__settings.get_comm_port())
            self.__rfid = __chafonrfid.get_tid()
            if __chafonrfid.error is not None:
                self.ui.statusBar.setText(__chafonrfid.error)
        except:
            self.ui.statusBar.setText(QCoreApplication.translate("Form", "rfid reader connect error"))
            self.__rfid = QCoreApplication.translate("Form", "Error")
            self.timer.stop()

    def scanrfid(self):
        self.readRfid()
        if self.__rfid is not None:
            self.ui.rfidHeaderlineEdit.setText(self.__rfid)

    def closeEvent(self, event):
        self.parent().show()
        self.timer.stop()
        self.close()
