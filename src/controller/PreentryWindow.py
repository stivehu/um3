import logging
import os

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from src.controller.WindowMixin import RfidReaderMixin, ResizeFontMixin
from src.models.AgegroupModel import AgegroupModel
from src.models.DistanceModel import DistanceModel
from src.models.EnrtyModel import EntryModel
from src.models.EntrypickupModel import EntrypickupModel
from src.models.GenderModel import GenderModel
from src.models.SettingsModel import SettingsModel
from src.views.preentry.preentry import Ui_PreentryForm
from datetime import datetime

# Ideiglenes debug naplózás a "gyors végrehajtás" megakadás / dupla-lépés hiba
# felderítéséhez. Csak akkor ír fájlba, ha az UM3_DEBUG_RFID környezeti változó
# be van állítva -- alap esetben (pl. teszteknél) nincs mellékhatása.
_debug_logger = logging.getLogger('preentry_debug')
if os.environ.get('UM3_DEBUG_RFID') and not _debug_logger.handlers:
    _debug_log_path = os.path.abspath('preentry_debug.log')
    _debug_handler = logging.FileHandler(_debug_log_path, mode='w')
    _debug_handler.setFormatter(logging.Formatter('%(asctime)s.%(msecs)03d %(message)s', datefmt='%H:%M:%S'))
    _debug_logger.addHandler(_debug_handler)
    _debug_logger.setLevel(logging.DEBUG)
    _debug_logger.propagate = False
    print("[UM3_DEBUG_RFID] PreentryWindow debug log active -> %s" % _debug_log_path, flush=True)
    _debug_logger.debug("=== debug log started, pid=%s ===", os.getpid())


class PreentryWindow(QDialog, RfidReaderMixin, ResizeFontMixin):
    def __init__(self, parent=None):
        super(PreentryWindow, self).__init__(parent)
        self.ui = Ui_PreentryForm()
        self.ui.setupUi(self)
        self.connectSignalsSlots()
        self.__startnum_is_updating = False
        self.__rfid = None
        self.__last_consumed_rfid = None
        self.__reading_rfid = False
        self.__read_worker = None
        self.__closing = False
        self.__entryModel = EntryModel()
        self.__settings = SettingsModel()
        self.__init_entry_site_url()
        self.__init_widget_dict()
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

    def __init_widget_dict(self):
        self.__widget_dict = {'labels': {}, 'lineEdits': {}, 'pushButtons': {}}
        self.__widget_dict['labels']["startnum"] = self.ui.label
        self.__widget_dict['labels']["distance"] = self.ui.distancelabel
        self.__widget_dict['labels']["rfid"] = self.ui.rfidLabel
        self.__widget_dict['labels']["lastname"] = self.ui.lastnamelabel
        self.__widget_dict['labels']["firstname"] = self.ui.firstnamelabel
        self.__widget_dict['labels']["status"] = self.ui.statusBar

        self.__widget_dict['lineEdits']["url"] = self.ui.urllineEdit
        self.__widget_dict['lineEdits']["username"] = self.ui.usernamelineEdit
        self.__widget_dict['lineEdits']["password"] = self.ui.passwordlineEdit
        self.__widget_dict['lineEdits']["lastname"] = self.ui.lastnamelineEdit
        self.__widget_dict['lineEdits']["rfid"] = self.ui.rfidlineEdit
        self.__widget_dict['lineEdits']["startnum"] = self.ui.startnumlineEdit
        self.__widget_dict['lineEdits']["firstname"] = self.ui.firstnamelineEdit
        self.__widget_dict['lineEdits']["distance"] = self.ui.distancelineEdit
        self.__widget_dict['lineEdits']["startnumHeader"] = self.ui.startnumHeaderlineEdit
        self.__widget_dict['lineEdits']["rfidHeader"] = self.ui.rfidHeaderlineEdit

        self.__widget_dict['pushButtons']["login"] = self.ui.loginpushButton
        self.__widget_dict['pushButtons']["read"] = self.ui.readpushButton
        self.__widget_dict['pushButtons']["prev"] = self.ui.prevpushButton
        self.__widget_dict['pushButtons']["next"] = self.ui.nextpushButton
        self.__widget_dict['pushButtons']["insert"] = self.ui.insertpushButton
        self.__widget_dict['pushButtons']["save"] = self.ui.savepushButton
        self.__widget_dict['pushButtons']["insertSaveNext"] = self.ui.insertSaveNextpushButton
        self.__widget_dict['pushButtons']["close"] = self.ui.closepushButton

    def connectSignalsSlots(self):
        self.ui.prevpushButton.clicked.connect(self.actionPrevButton)
        self.ui.nextpushButton.clicked.connect(self.actionNextButton)
        self.ui.readpushButton.clicked.connect(self.actionStartnumHeaderlineEdit)
        self.ui.insertpushButton.clicked.connect(self.actioninsertpushButton)
        self.ui.loginpushButton.clicked.connect(self.actionLoginForm)
        self.ui.savepushButton.clicked.connect(self.actionSavepushButton)
        self.ui.insertSaveNextpushButton.clicked.connect(self.actionInsertSaveNextpushButton)
        self.ui.closepushButton.clicked.connect(self.close)

    def actionInsertSaveNextpushButton(self):
        oldrfid = self.ui.rfidHeaderlineEdit.text()
        _debug_logger.debug("InsertSaveNext: start oldrfid=%r startnum=%r", oldrfid,
                             self.ui.startnumHeaderlineEdit.text())
        self.actioninsertpushButton()
        if self.ui.rfidHeaderlineEdit.text() == None or self.ui.rfidHeaderlineEdit.text() != oldrfid:
            if self.actionSavepushButton() == True:
                _debug_logger.debug("InsertSaveNext: save OK, calling actionNextButton")
                self.actionNextButton()
            else:
                _debug_logger.debug("InsertSaveNext: save FAILED, next not called")
        else:
            _debug_logger.debug("InsertSaveNext: skipped save/next, header unchanged (%r)", oldrfid)

    def actionSavepushButton(self):
        startnum = self.ui.startnumlineEdit.text()
        rfid = self.ui.rfidlineEdit.text()
        self.__entryModel.update_rfid_from_startnum(startnum, rfid)
        _debug_logger.debug("actionSavepushButton: startnum=%r rfid=%r status_code=%r", startnum, rfid,
                             self.__entryModel.status_code)
        if self.__entryModel.status_code != 200:
            self.ui.statusBar.setText(self.__entryModel.error)
            self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form", "%s Can't  save %s to %s") % (
            datetime.now().strftime("%H:%M:%S"), rfid, startnum))
            return False
        self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form", "%s Saved %s to %s") % (
            datetime.now().strftime("%H:%M:%S"), rfid, startnum))
        return True

    def actioninsertpushButton(self):
        self.__last_consumed_rfid = self.ui.rfidHeaderlineEdit.text()
        _debug_logger.debug("actioninsertpushButton: consuming rfid=%r for startnum=%r",
                             self.__last_consumed_rfid, self.ui.startnumlineEdit.text())
        self.ui.rfidlineEdit.setText(self.ui.rfidHeaderlineEdit.text())
        self.ui.rfidHeaderlineEdit.setText(None)
        self.ui.historylistWidget.insertItem(0, QCoreApplication.translate("Form",
                                                                           "%s Insert %s to startnum %s") % (
                                                 datetime.now().strftime(
                                                     "%H:%M:%S"),
                                                 self.ui.rfidHeaderlineEdit.text(),
                                                 self.ui.startnumlineEdit.text()))

    def actionNextButton(self):
        _debug_logger.debug("actionNextButton: called, current header=%r startnum_is_updating=%r",
                             self.ui.startnumHeaderlineEdit.text(), self.__startnum_is_updating)
        if not self.ui.startnumHeaderlineEdit.text().isdigit():
            _debug_logger.debug("actionNextButton: header not digit, returning")
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
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
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
            self.ui.label.resizeEvent = self.resizeText

    def resizeText(self, event):
        font = self._resizeFont()
        for widgetTypes in self.__widget_dict.values():
            for widget in widgetTypes.values():
                widget.setFont(font)

    def initTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.scanrfid)
        self.timer.start(self.__settings.get_chipcontroll_interval())

    def scanrfid(self):
        # A soros port olvasása (SerialTransport timeout=5s, több frame is
        # lehet) másodpercekig blokkolhatna a GUI szálon -- ezért háttérszálon
        # fut (_readTidAsync), a scanrfid csak elindítja és azonnal visszatér.
        if self.__reading_rfid:
            return
        self.__reading_rfid = True
        self.__read_worker = self._readTidAsync(self.__settings.get_comm_port(), self.__onRfidRead)

    def __onRfidRead(self, rfid, error):
        self.__reading_rfid = False
        self.__read_worker = None
        if self.__closing:
            return
        if error is not None:
            self.ui.statusBar.setText(error)
        else:
            self.ui.statusBar.setText(None)
        self.__rfid = rfid
        if self.__rfid is not None and self.__rfid == self.__last_consumed_rfid:
            _debug_logger.debug("scanrfid: ignoring lingering consumed chip %r", self.__rfid)
            return
        if self.__rfid is not None:
            _debug_logger.debug("scanrfid: accepted chip %r into header (was %r)", self.__rfid,
                                 self.ui.rfidHeaderlineEdit.text())
            self.ui.rfidHeaderlineEdit.setText(self.__rfid)
            self.timer.stop()
            self.timer.singleShot(self.__settings.get_chipcontroll_wait_after_read(), self.restore_timer)

    def restore_timer(self):
        _debug_logger.debug("restore_timer: restarting timer")
        self.timer.stop()
        self.timer.start(self.__settings.get_chipcontroll_interval())

    def closeEvent(self, event):
        self.__closing = True
        self.timer.stop()
        if self.__read_worker is not None and self.__read_worker.isRunning():
            self.__read_worker.wait(6000)
        self.parent().show()
        self.close()
