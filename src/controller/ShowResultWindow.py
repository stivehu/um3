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
        self.__reading_rfid = False
        self.__read_worker = None
        self.__closing = False
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

    def closeEvent(self, event):
        self.__closing = True
        self.timer.stop()
        if self.__read_worker is not None and self.__read_worker.isRunning():
            self.__read_worker.wait(6000)
        self.parent().show()
        self.close()
