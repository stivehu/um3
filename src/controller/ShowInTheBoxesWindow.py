import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from src.chafonrfid.Chafonrfid import Chafonrfid
from src.models.EnrtyModel import EntryModel
from src.models.IntheboxModel import IntheboxModel
from src.models.SettingsModel import SettingsModel
from src.views.showinthebox.showinthebox import Ui_ShowintheboxForm


class ShowInTheBoxesWindow(QDialog):
    def __init__(self, parent=None):
        super(ShowInTheBoxesWindow, self).__init__(parent)
        self.ui = Ui_ShowintheboxForm()
        self.ui.setupUi(self)
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
        self.readRfid()
        if self.__rfid is not None:
            self.__entryModel.setinthebox('rfid',self.__rfid)
            self.__intheboxmodel.list()
            self.updateCounter()

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
