from PyQt5 import QtWidgets
from src.ui.mainwindow import Ui_UserMangerUi


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_UserMangerUi()
        self.ui.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.ui.actionExit.triggered.connect(self.close)
        # self.ui.action_Parse.triggered.connect(self.action_Parse)

    def action_Parse(self):
        pass
        # self.parser(self.ui.textEdit.toPlainText())
