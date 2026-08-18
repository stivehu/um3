import sys

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

from src.controller.WindowMixin import RfidReaderMixin
from src.models.EnrtyModel import EntryModel
from src.models.IntheboxModel import IntheboxModel
from src.models.SettingsModel import SettingsModel
from src.views.showinthebox.showinthebox import Ui_ShowintheboxForm


class ShowInTheBoxesWindow(QDialog, RfidReaderMixin):
    def __init__(self, parent=None):
        super(ShowInTheBoxesWindow, self).__init__(parent)
        self.ui = Ui_ShowintheboxForm()
        self.ui.setupUi(self)
        self.__rfid = None
        self.__reading_rfid = False
        self.__read_worker = None
        self.__closing = False
        self.__settings = SettingsModel()
        self.__intheboxmodel = IntheboxModel()
        self.__entryModel = EntryModel()
        self.ui.startnumTableView.setModel(self.__intheboxmodel)
        self.initTimer()
        self.connectSignalsSlots()
        self.updateCounter()

    def updateCounter(self):
        self.ui.counterValuelabel.setText(str(self.__intheboxmodel.count_all_record()))

    def connectSignalsSlots(self):
        self.ui.startnumLineEdit.returnPressed.connect(self.actionStartnumLineEditReturnPressed)
        self.ui.closePushButton.clicked.connect(self.close)

    def actionStartnumLineEditReturnPressed(self):
        self.__entryModel.setinthebox('startnum', self.ui.startnumLineEdit.text())
        self.__intheboxmodel.set_inserting_item(self.ui.startnumLineEdit.text())
        self.__intheboxmodel.list()
        self.ui.startnumLineEdit.setText(None)
        self.updateCounter()


    def initTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.scanrfid)
        self.timer.start(self.__settings.get_chipcontroll_interval())

    def scanrfid(self):
        if self.__reading_rfid:
            return
        self.__reading_rfid = True
        self.__read_worker = self._readTidAsync(self.__settings.get_comm_port(), self.__onRfidRead)

    def __onRfidRead(self, rfid, error):
        self.__reading_rfid = False
        self.__read_worker = None
        if self.__closing:
            return
        self.ui.statusBar.setText(error)
        self.__rfid = rfid
        if self.__rfid is not None:
            self.__entryModel.setinthebox('rfid', self.__rfid)
            self.__intheboxmodel.list()
            self.updateCounter()

    def closeEvent(self, event):
        self.__closing = True
        self.timer.stop()
        if self.__read_worker is not None and self.__read_worker.isRunning():
            self.__read_worker.wait(6000)
        self.parent().show()
        self.close()
