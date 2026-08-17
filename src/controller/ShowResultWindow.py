from PyQt6.QtCore import QTimer, QUrl
from PyQt6.QtWidgets import QDialog

from src.controller.WindowMixin import RfidReaderMixin, ResizeFontMixin
from src.models.ResultModel import ResultModel
from src.models.SettingsModel import SettingsModel
from src.views.showresult.showresult import Ui_Form


class ShowResultWindow(QDialog, RfidReaderMixin, ResizeFontMixin):
    def __init__(self, parent=None):
        super(ShowResultWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__rfid = None
        self.__resultModel = ResultModel()
        self.__settings = SettingsModel()
        self.connectSignalsSlots()
        self.initResize()
        self.initTimer()
        self.maximizeWindow()
        self.showResultList()

    def connectSignalsSlots(self):
        self.ui.closePushButton.clicked.connect(self.close)

    def initTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.scanrfid)
        self.timer.start(self.__settings.get_chipcontroll_interval())

    def maximizeWindow(self):
        if self.__settings.get_auto_maximize_opening_window() == True:
            self.showMaximized()

    def resizeText(self, event):
        font = self._resizeFont()
        self.ui.statusBar.setFont(font)
        self.ui.closePushButton.setFont(font)

    def initResize(self):
        if self.__settings.get_auto_resize_window():
            self.ui.statusBar.resizeEvent = self.resizeText
            self.ui.closePushButton.resizeEvent = self.resizeText

    def scanrfid(self):
        self.readRfid()
        if self.__rfid is not None:
            self.showScoreboard(self.__rfid)

    def showResultList(self):
        self.ui.webView.setUrl(QUrl(self.__resultModel.get_result_url()))

    def showScoreboard(self, rfid):
        self.ui.webView.setUrl(QUrl(self.__resultModel.get_scoreboard_url(rfid)))
        self.timer.stop()
        self.timer.singleShot(self.__settings.get_chipcontroll_wait_after_read(), self.restore_timer)

    def restore_timer(self):
        self.showResultList()
        self.timer.start(self.__settings.get_chipcontroll_interval())

    def readRfid(self):
        self.__rfid = self._readTid(self.__settings.get_comm_port(), self.ui.statusBar.setText)

    def closeEvent(self, event):
        self.timer.stop()
        self.parent().show()
        self.close()
