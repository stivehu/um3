# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'localentry.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(600, 493)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(True)
        Form.setInputMethodHints(QtCore.Qt.ImhDate)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startNumLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startNumLabel.sizePolicy().hasHeightForWidth())
        self.startNumLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.startNumLabel.setFont(font)
        self.startNumLabel.setObjectName("startNumLabel")
        self.horizontalLayout.addWidget(self.startNumLabel)
        self.startnumLineEdit = QtWidgets.QLineEdit(Form)
        self.startnumLineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startnumLineEdit.sizePolicy().hasHeightForWidth())
        self.startnumLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.startnumLineEdit.setFont(font)
        self.startnumLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.startnumLineEdit.setObjectName("startnumLineEdit")
        self.horizontalLayout.addWidget(self.startnumLineEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.distanceLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceLabel.sizePolicy().hasHeightForWidth())
        self.distanceLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.distanceLabel.setFont(font)
        self.distanceLabel.setObjectName("distanceLabel")
        self.horizontalLayout_2.addWidget(self.distanceLabel)
        self.distanceComboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceComboBox.sizePolicy().hasHeightForWidth())
        self.distanceComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.distanceComboBox.setFont(font)
        self.distanceComboBox.setObjectName("distanceComboBox")
        self.horizontalLayout_2.addWidget(self.distanceComboBox)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.birthdayLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.birthdayLabel.sizePolicy().hasHeightForWidth())
        self.birthdayLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.birthdayLabel.setFont(font)
        self.birthdayLabel.setObjectName("birthdayLabel")
        self.horizontalLayout_3.addWidget(self.birthdayLabel)
        self.birthdayDateEdit = QtWidgets.QDateEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.birthdayDateEdit.sizePolicy().hasHeightForWidth())
        self.birthdayDateEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.birthdayDateEdit.setFont(font)
        self.birthdayDateEdit.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.birthdayDateEdit.setAcceptDrops(True)
        self.birthdayDateEdit.setAutoFillBackground(True)
        self.birthdayDateEdit.setInputMethodHints(QtCore.Qt.ImhDate)
        self.birthdayDateEdit.setWrapping(False)
        self.birthdayDateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.birthdayDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1800, 1, 1), QtCore.QTime(0, 0, 0)))
        self.birthdayDateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.birthdayDateEdit.setCalendarPopup(True)
        self.birthdayDateEdit.setCurrentSectionIndex(0)
        self.birthdayDateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.birthdayDateEdit.setObjectName("birthdayDateEdit")
        self.horizontalLayout_3.addWidget(self.birthdayDateEdit)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.agegroupLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agegroupLabel.sizePolicy().hasHeightForWidth())
        self.agegroupLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.agegroupLabel.setFont(font)
        self.agegroupLabel.setObjectName("agegroupLabel")
        self.horizontalLayout_4.addWidget(self.agegroupLabel)
        self.agegroupComboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agegroupComboBox.sizePolicy().hasHeightForWidth())
        self.agegroupComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.agegroupComboBox.setFont(font)
        self.agegroupComboBox.setObjectName("agegroupComboBox")
        self.horizontalLayout_4.addWidget(self.agegroupComboBox)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lastnameLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastnameLabel.sizePolicy().hasHeightForWidth())
        self.lastnameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lastnameLabel.setFont(font)
        self.lastnameLabel.setObjectName("lastnameLabel")
        self.horizontalLayout_5.addWidget(self.lastnameLabel)
        self.lastnameLineEdit = QtWidgets.QLineEdit(Form)
        self.lastnameLineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.lastnameLineEdit.sizePolicy().hasHeightForWidth())
        self.lastnameLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lastnameLineEdit.setFont(font)
        self.lastnameLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.lastnameLineEdit.setObjectName("lastnameLineEdit")
        self.horizontalLayout_5.addWidget(self.lastnameLineEdit)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.firstnameLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstnameLabel.sizePolicy().hasHeightForWidth())
        self.firstnameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.firstnameLabel.setFont(font)
        self.firstnameLabel.setObjectName("firstnameLabel")
        self.horizontalLayout_6.addWidget(self.firstnameLabel)
        self.firstnameLineEdit = QtWidgets.QLineEdit(Form)
        self.firstnameLineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstnameLineEdit.sizePolicy().hasHeightForWidth())
        self.firstnameLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.firstnameLineEdit.setFont(font)
        self.firstnameLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.firstnameLineEdit.setObjectName("firstnameLineEdit")
        self.horizontalLayout_6.addWidget(self.firstnameLineEdit)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.genderLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genderLabel.sizePolicy().hasHeightForWidth())
        self.genderLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.genderLabel.setFont(font)
        self.genderLabel.setObjectName("genderLabel")
        self.horizontalLayout_7.addWidget(self.genderLabel)
        self.genderComboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genderComboBox.sizePolicy().hasHeightForWidth())
        self.genderComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.genderComboBox.setFont(font)
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.setItemText(0, "")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.genderComboBox)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.settlementLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settlementLabel.sizePolicy().hasHeightForWidth())
        self.settlementLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.settlementLabel.setFont(font)
        self.settlementLabel.setObjectName("settlementLabel")
        self.horizontalLayout_8.addWidget(self.settlementLabel)
        self.settlementLineEdit = QtWidgets.QLineEdit(Form)
        self.settlementLineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settlementLineEdit.sizePolicy().hasHeightForWidth())
        self.settlementLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.settlementLineEdit.setFont(font)
        self.settlementLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.settlementLineEdit.setObjectName("settlementLineEdit")
        self.horizontalLayout_8.addWidget(self.settlementLineEdit)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.readRfidPushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readRfidPushButton.sizePolicy().hasHeightForWidth())
        self.readRfidPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.readRfidPushButton.setFont(font)
        self.readRfidPushButton.setObjectName("readRfidPushButton")
        self.horizontalLayout_9.addWidget(self.readRfidPushButton)
        self.rfidLineEdit = QtWidgets.QLineEdit(Form)
        self.rfidLineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rfidLineEdit.sizePolicy().hasHeightForWidth())
        self.rfidLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.rfidLineEdit.setFont(font)
        self.rfidLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.rfidLineEdit.setObjectName("rfidLineEdit")
        self.horizontalLayout_9.addWidget(self.rfidLineEdit)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.newPushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newPushButton.sizePolicy().hasHeightForWidth())
        self.newPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.newPushButton.setFont(font)
        self.newPushButton.setObjectName("newPushButton")
        self.horizontalLayout_10.addWidget(self.newPushButton)
        self.savePushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePushButton.sizePolicy().hasHeightForWidth())
        self.savePushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.savePushButton.setFont(font)
        self.savePushButton.setStatusTip("")
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_10.addWidget(self.savePushButton)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.statusBarLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBarLabel.sizePolicy().hasHeightForWidth())
        self.statusBarLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.statusBarLabel.setFont(font)
        self.statusBarLabel.setText("")
        self.statusBarLabel.setObjectName("statusBarLabel")
        self.verticalLayout_3.addWidget(self.statusBarLabel)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.genderComboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "startnum pickup"))
        self.startNumLabel.setText(_translate("Form", "Start num"))
        self.distanceLabel.setText(_translate("Form", "distance"))
        self.birthdayLabel.setText(_translate("Form", "Birthday"))
        self.birthdayDateEdit.setSpecialValueText(_translate("Form", "\" \""))
        self.birthdayDateEdit.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
        self.agegroupLabel.setText(_translate("Form", "Age group"))
        self.lastnameLabel.setText(_translate("Form", "Lastname"))
        self.firstnameLabel.setText(_translate("Form", "First name"))
        self.genderLabel.setText(_translate("Form", "Gender"))
        self.genderComboBox.setItemText(1, _translate("Form", "Man"))
        self.genderComboBox.setItemText(2, _translate("Form", "Woman"))
        self.settlementLabel.setText(_translate("Form", "Settlement"))
        self.readRfidPushButton.setText(_translate("Form", "Read rfid"))
        self.newPushButton.setText(_translate("Form", "New entry"))
        self.savePushButton.setText(_translate("Form", "Save entry"))
