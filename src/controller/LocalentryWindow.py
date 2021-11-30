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
from src.views.localentry.localentry import Ui_Form


class LocalentryWindow(QDialog):
    def __init__(self, parent=None):
        super(LocalentryWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connectSignalsSlots()
        self.__rfid = None
        self.__entrypickupModel = EntrypickupModel()
        self.__settings = SettingsModel()
        self.initResize()
        self.maximizeWindow()
        self.__initComboboxes()
        self.__init_widget_dict()

    def __init_widget_dict(self):
        self.__widget_dict = {'labels': {}, 'comboBoxes': {}, 'lineEdits': {}, 'pushButtons': {}, 'dateEdits': {}}
        self.__widget_dict['labels']["startnum"] = self.ui.startNumLabel
        self.__widget_dict['labels']["distance"] = self.ui.distanceLabel
        self.__widget_dict['labels']["birthday"] = self.ui.birthdayLabel
        self.__widget_dict['labels']["agegroup"] = self.ui.agegroupLabel
        self.__widget_dict['labels']["lastname"] = self.ui.lastnameLabel
        self.__widget_dict['labels']["firstname"] = self.ui.firstnameLabel
        self.__widget_dict['labels']["category0_id"] = self.ui.genderLabel
        self.__widget_dict['labels']["settlement"] = self.ui.settlementLabel
        self.__widget_dict['labels']["status"] = self.ui.statusBarLabel

        self.__widget_dict['comboBoxes']["distance"] = self.ui.distanceComboBox
        self.__widget_dict['comboBoxes']["category1_id"] = self.ui.agegroupComboBox
        self.__widget_dict['comboBoxes']["category0_id"] = self.ui.genderComboBox

        self.__widget_dict['lineEdits']["lastname"] = self.ui.lastnameLineEdit
        self.__widget_dict['lineEdits']["startnum"] = self.ui.startnumLineEdit
        self.__widget_dict['lineEdits']["firstname"] = self.ui.firstnameLineEdit
        self.__widget_dict['lineEdits']["rfid"] = self.ui.rfidLineEdit
        self.__widget_dict['lineEdits']["settlement"] = self.ui.settlementLineEdit

        self.__widget_dict['pushButtons']["rfid"] = self.ui.readRfidPushButton
        self.__widget_dict['pushButtons']["new"] = self.ui.newPushButton
        self.__widget_dict['pushButtons']["save"] = self.ui.savePushButton

        self.__widget_dict['dateEdits']["birthday"] = self.ui.birthdayDateEdit

    def __initComboboxes(self):
        self.__distances = DistanceModel()
        self.__agegroup = AgegroupModel()
        self.__gender = GenderModel()

        self.ui.distanceComboBox.clear()
        self.ui.distanceComboBox.addItems(self.__distances.get_distance_names())
        self.ui.distanceComboBox.setCurrentIndex(-1)
        self.printErrorMessage(self.__distances.error)

        self.ui.agegroupComboBox.clear()
        self.ui.agegroupComboBox.addItems(self.__agegroup.get_agegroup_names())
        self.ui.agegroupComboBox.setCurrentIndex(-1)
        self.printErrorMessage(self.__agegroup.error)

        self.ui.genderComboBox.clear()
        self.ui.genderComboBox.addItems(self.__gender.get_gender_names())
        self.ui.genderComboBox.setCurrentIndex(-1)
        self.printErrorMessage(self.__gender.error)

    def printErrorMessage(self, error):
        if (isinstance(error, str)):
            self.ui.statusBarLabel.setText(error)

    def maximizeWindow(self):
        if self.__settings.get_auto_maximize_opening_window() == True:
            self.showMaximized()

    def connectSignalsSlots(self):
        self.ui.readRfidPushButton.clicked.connect(self.actionReadRfidPushButton)
        self.ui.newPushButton.clicked.connect(self.actionNewPushButton)
        self.ui.savePushButton.clicked.connect(self.actionSavePushButton)
        self.ui.birthdayDateEdit.dateChanged.connect(self.birthdayChange)

    def birthdayChange(self):
        birthday = self.ui.birthdayDateEdit.date().toPyDate().isoformat()
        age = self.__distances.get_age_from_birthday(birthday)
        agegroup_id = self.__agegroup.get_agegroup_from_age(age)
        if (agegroup_id != None):
            agegroup_index = self.__agegroup.get_agegroup_from_index(agegroup_id)
            self.ui.agegroupComboBox.setCurrentIndex(agegroup_index)
        else:
            self.ui.agegroupComboBox.setCurrentIndex(-1)

    def get_entry_field(self):
        result = {}
        result['birthsday'] = self.ui.birthdayDateEdit.date().toString('yyyy-MM-dd')
        result['category1_id'] = str(self.__agegroup.get_agegroup_index()[int(self.ui.agegroupComboBox.currentIndex())])
        # result['category0_id'] = str(self.ui.genderComboBox.currentIndex())
        result['category0_id'] = str(self.__gender.get_gender_index()[int(self.ui.genderComboBox.currentIndex())])
        result['startnum'] = str(self.ui.startnumLineEdit.text())
        result['distance_id'] = str(self.__distances.get_distance_index()[int(self.ui.distanceComboBox.currentIndex())])
        result['lastname'] = self.ui.lastnameLineEdit.text()
        result['firstname'] = self.ui.firstnameLineEdit.text()
        result['settlement'] = self.ui.settlementLineEdit.text()
        result['rfid'] = self.ui.rfidLineEdit.text()
        for i in range(2, 10):
            result['category{}_id'.format(i)] = None
        return result

    def __check_dependies(self):
        result = True
        for widget in self.__widget_dict['lineEdits'].values():
            if widget.text() == '':
                widget.setToolTip(QCoreApplication.translate("Form", "This field required  "))
                widget.setStyleSheet('background-color: rgb(239, 0, 0);')  # piros
                result = False
            else:
                widget.setStyleSheet(None)
                widget.setToolTip(None)
        for widget in self.__widget_dict['comboBoxes'].values():
            if widget.currentIndex() == -1:
                widget.setToolTip(QCoreApplication.translate("Form", "This field must be select "))
                widget.setStyleSheet('background-color: rgb(239, 0, 0);')  # piros
                result = False
            else:
                widget.setStyleSheet(None)
                widget.setToolTip(None)
        if self.ui.startnumLineEdit.text().isnumeric() == False:
            self.ui.startnumLineEdit.setToolTip(QCoreApplication.translate("Form", "Startnum is required field "))
            self.ui.startnumLineEdit.setStyleSheet('background-color: rgb(239, 0, 0);')  # piros
            result = False
        else:
            widget.setStyleSheet(None)
            widget.setToolTip(None)
        if self.ui.birthdayDateEdit.text() == '1800-01-01':
            self.ui.birthdayDateEdit.setToolTip(QCoreApplication.translate("Form", "Invalid birthday"))
            self.ui.birthdayDateEdit.setStyleSheet('background-color: rgb(239, 0, 0);')  # piros
        else:
            self.ui.birthdayDateEdit.setStyleSheet(None)
            self.ui.birthdayDateEdit.setToolTip(None)
        return result

    def actionSavePushButton(self):
        self.entry = EntryModel()
        if self.__check_dependies():
            send_data = self.get_entry_field()
            self.newentry = self.entry.create_new_entry(send_data)
            if self.newentry == send_data:
                self.cleanFields()
                _translate=QCoreApplication.translate
                self.ui.statusBarLabel.setText(_translate("Form", "New entry added"))
            elif self.newentry == None:
                self.printErrors()

    def printErrors(self):
        errors = []
        for error in self.entry.get_error_messages():
            errors.append(error)
        self.ui.statusBarLabel.setText("\n".join(errors))

    def actionNewPushButton(self):
        _translate = QCoreApplication.translate
        confirmDialog = QMessageBox()
        confirmDialog.setIcon(QMessageBox.Information)
        confirmDialog.setText(_translate("Form", "Are you sure? This page will be destroyed"))
        confirmDialog.setWindowTitle(_translate("Form", "Create new entry"))
        confirmDialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if confirmDialog.exec() == QMessageBox.Ok:
            self.cleanFields()

    def actionReadRfidPushButton(self):
        self.readRfid()
        self.ui.rfidLineEdit.setText(self.__rfid)

    def cleanFields(self):
        self.ui.birthdayDateEdit.setDate(QDate(1800, 1, 1))
        for widget in self.__widget_dict['lineEdits'].values():
            widget.setStyleSheet(None)
            widget.setText(None)
        for widget in self.__widget_dict['comboBoxes'].values():
            widget.setStyleSheet(None)
            widget.setCurrentIndex(-1)

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
        else:
            self.ui.statusBarLabel.setText(None)

    def closeEvent(self, event):
        self.parent().show()
        self.close()
