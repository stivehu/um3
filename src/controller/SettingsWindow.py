from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QDialog)

from src.models.SettingsModel import SettingsModel
from src.views.settings.settings import Ui_Form


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__settings = SettingsModel()
        self.fillComports()
        self.initValues()
        self.initResize()
        self.maximizeWindow()
        self.connectSignalsSlots()

    def fillComports(self):
        for port_num in range(0, 18):
            self.ui.commPortComboBox.addItem("{}{}".format(self.__settings.get_default_com_port(False), port_num))

    def connectSignalsSlots(self):
        self.ui.savePushButton.clicked.connect(self.actionSavePushButton)

    def actionSavePushButton(self):
        self.collectSettings()
        self.__settings.save_config()

    def collectSettings(self):
        self.__settings.set_server_ip(self.ui.serverIpLineEdit.text())
        self.__settings.set_chipcontroll_interval(self.ui.chipcontrollIntervalLineEdit.text())
        self.__settings.set_chipcontroll_wait_after_read(self.ui.chipcontrollWaitAfterReadlineEdit.text())
        self.__settings.set_auto_maximize_opening_window(self.ui.autoMaximizeOpeningWindowCheckBox.isChecked())
        self.__settings.set_auto_resize_window(self.ui.autoResizeWindowCheckBox.isChecked())
        self.__settings.set_comm_port(self.ui.commPortComboBox.itemText(self.ui.commPortComboBox.currentIndex()))
        self.__settings.set_entry_site_url(self.ui.entrySiteUrllLineEdit.text())

    def initValues(self):
        self.ui.serverIpLineEdit.setText(self.__settings.get_server_ip())
        self.ui.chipcontrollIntervalLineEdit.setText(str(self.__settings.get_chipcontroll_interval()))
        self.ui.chipcontrollWaitAfterReadlineEdit.setText(str(self.__settings.get_chipcontroll_wait_after_read()))
        self.ui.autoMaximizeOpeningWindowCheckBox.setChecked(self.__settings.get_auto_maximize_opening_window())
        self.ui.autoResizeWindowCheckBox.setChecked(self.__settings.get_auto_resize_window())
        self.ui.entrySiteUrllLineEdit.setText(self.__settings.get_entry_site_url())
        index = self.ui.commPortComboBox.findText(self.__settings.get_comm_port())
        if index >= 0:
            self.ui.commPortComboBox.setCurrentIndex(index)

    def maximizeWindow(self):
        if self.__settings.get_auto_maximize_opening_window() == True:
            self.showMaximized()

    def resizeText(self, event):
        defaultSize = 14
        if self.rect().width() // 40 > defaultSize:
            font = QFont('', self.rect().width() // 40)
        else:
            font = QFont('', defaultSize)
        self.ui.serverIpLineEdit.setFont(font)
        self.ui.serverIpLabel.setFont(font)
        self.ui.chipcontrollIntervalLineEdit.setFont(font)
        self.ui.chipcontrollWaitAfterReadlineEdit.setFont(font)
        self.ui.chipcontrollIntervalLabel.setFont(font)
        self.ui.chipcontrollWaitAfterReadlLabel.setFont(font)
        self.ui.autoMaximizeOpeningWindowLabel.setFont(font)
        self.ui.autoResizeWindowLabel.setFont(font)
        # self.ui.commPortComboBox.setFont(font)
        # self.ui.commPortLabel.setFont(font)
        self.ui.savePushButton.setFont(font)

    def initResize(self):
        if self.__settings.get_auto_resize_window():
            self.ui.serverIpLineEdit.resizeEvent = self.resizeText
            self.ui.serverIpLabel.resizeEvent = self.resizeText
            self.ui.chipcontrollIntervalLineEdit.resizeEvent = self.resizeText
            self.ui.chipcontrollWaitAfterReadlineEdit.resizeEvent = self.resizeText
            self.ui.chipcontrollIntervalLabel.resizeEvent = self.resizeText
            self.ui.chipcontrollWaitAfterReadlLabel.resizeEvent = self.resizeText
            self.ui.autoMaximizeOpeningWindowLabel.resizeEvent = self.resizeText
            self.ui.autoResizeWindowLabel.resizeEvent = self.resizeText
            self.ui.savePushButton.resizeEvent = self.resizeText
            # self.ui.commPortLabel = self.resizeText
            # self.ui.commPortComboBox = self.resizeText

    def closeEvent(self, event):
        self.parent().show()
        self.close()
