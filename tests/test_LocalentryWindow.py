import pytest, pytest_mock

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox

import src.models.EnrtyModel
from src.chafonrfid.Chafonrfid import Chafonrfid
from src.controller.ApplicationWindow import ApplicationWindow
from src.models.EnrtyModel import EntryModel
from src.models.EntrypickupModel import EntrypickupModel
from src.models.RemoteApiModel import RemoteApiModel
from tests.fixtures.jsons import entry_save_result, distances


def test_resize_text(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.localEntrypushButton, QtCore.Qt.LeftButton)
    widget.localentry.resize(640, 480)
    widget.localentry.resize(320, 240)
    widget.localentry.resize(160, 80)


def test_close_event(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.localEntrypushButton, QtCore.Qt.LeftButton)
    widget.localentry.close()


def test_action_read_rfid_push_button(qtbot, mocker):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.localEntrypushButton, QtCore.Qt.LeftButton)
    mocker.patch('src.controller.ApplicationWindow.Chafonrfid.get_tid', return_value="GENATED_RFID")
    qtbot.mouseClick(widget.localentry.ui.readRfidPushButton, QtCore.Qt.LeftButton)
    assert widget.localentry.ui.rfidLineEdit.text() == 'GENATED_RFID'


def test_action_new_push_button(qtbot,mocker):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.localEntrypushButton, QtCore.Qt.LeftButton)
    mocker.patch('PyQt5.QtWidgets.QMessageBox.exec', return_value=QMessageBox.Ok)
    qtbot.mouseClick(widget.localentry.ui.newPushButton, QtCore.Qt.LeftButton)
    all_field_is_empty(widget)


def fill_fields():
    self.ui.startnumLineEdit.setText('100')
    self.ui.distanceLineEdit.setText('')
    self.ui.birthdayDateEdit.setDate(QDate(1800, 1, 1))
    self.ui.agegroupLineEdit.setText(None)
    self.ui.lastnameLineEdit.setText(None)
    self.ui.firstnameLineEdit.setText(None)
    self.ui.genderComboBox.setCurrentIndex(-1)
    self.ui.settlementLineEdit.setText(None)



def test_get_items():
    inputvar = [{'id': 1, 'name': '2,5 km', 'starttime': None, 'startlen': None, 'laplen': None, 'stoptime': None,
                 'started': False, 'followUpStart': False, 'lengthbase': False},
                {'id': 2, 'name': '5 km', 'starttime': None, 'startlen': None, 'laplen': None, 'stoptime': None,
                 'started': False, 'followUpStart': False, 'lengthbase': False},
                {'id': 3, 'name': '10 km', 'starttime': None, 'startlen': None, 'laplen': None, 'stoptime': None,
                 'started': False, 'followUpStart': False, 'lengthbase': False}]
    result = []
    for distance in inputvar:
        result.append(distance['name'])


def test_birthday_change(qtbot,mocker):
    widget = ApplicationWindow()
    mocker.patch('src.models.RemoteApiModel.RemoteApiModel.sendAjaxRequest', return_value=distances)
    qtbot.mouseClick(widget.ui.localEntrypushButton, QtCore.Qt.LeftButton)
    widget.localentry.ui.birthdayDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1978, 2, 8), QtCore.QTime(0, 0, 0)))
    assert widget.localentry.ui.agegroupComboBox.currentIndex() == 5
    widget.localentry.ui.birthdayDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 2, 8), QtCore.QTime(0, 0, 0)))
    assert widget.localentry.ui.agegroupComboBox.currentIndex() == -1


def test_action_save_push_button(qtbot,mocker):
    widget = ApplicationWindow()
    mocker.patch('src.models.RemoteApiModel.RemoteApiModel.sendAjaxRequest', return_value=distances)
    qtbot.mouseClick(widget.ui.localEntrypushButton, QtCore.Qt.LeftButton)
    widget.localentry.ui.startnumLineEdit.setText("100")
    widget.localentry.ui.distanceComboBox.setCurrentIndex(2)
    widget.localentry.ui.birthdayDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1978, 2, 8), QtCore.QTime(0, 0, 0)))
    widget.localentry.ui.lastnameLineEdit.setText('Teszt')
    widget.localentry.ui.firstnameLineEdit.setText('Elek')
    widget.localentry.ui.genderComboBox.setCurrentIndex(2)
    widget.localentry.ui.settlementLineEdit.setText("Békéscsaba")
    widget.localentry.ui.rfidLineEdit.setText('ABG3652AE')
    mocker.patch('src.models.EnrtyModel.EntryModel.create_new_entry', return_value=entry_save_result)
    sent_data = widget.localentry.get_entry_field()
    qtbot.mouseClick(widget.localentry.ui.savePushButton, QtCore.Qt.LeftButton)
    result = widget.localentry.newentry
    assert result == sent_data


def all_field_is_empty(widget):
    assert widget.localentry.ui.startnumLineEdit.text() == ''
    assert widget.localentry.ui.distanceComboBox.currentIndex() == -1
    assert widget.localentry.ui.birthdayDateEdit.text() == '1800-01-01'
    assert widget.localentry.ui.agegroupComboBox.currentIndex() == -1
    assert widget.localentry.ui.lastnameLineEdit.text() == ''
    assert widget.localentry.ui.firstnameLineEdit.text() == ''
    assert widget.localentry.ui.genderComboBox.currentIndex() == -1
    assert widget.localentry.ui.settlementLineEdit.text() == ''
    assert widget.localentry.ui.rfidLineEdit.text() == ''


def test_clean_fields(qtbot):
    widget = ApplicationWindow()
    qtbot.mouseClick(widget.ui.localEntrypushButton, QtCore.Qt.LeftButton)
    widget.localentry.cleanFields()
    all_field_is_empty(widget)
