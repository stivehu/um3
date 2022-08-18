# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sendresult.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sendresultForm(object):
    def setupUi(self, sendresultForm):
        sendresultForm.setObjectName("sendresultForm")
        sendresultForm.setWindowModality(QtCore.Qt.WindowModal)
        sendresultForm.resize(900, 261)
        sendresultForm.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(sendresultForm)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.startnumLineEdit = QtWidgets.QLineEdit(sendresultForm)
        self.startnumLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startnumLineEdit.sizePolicy().hasHeightForWidth())
        self.startnumLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.startnumLineEdit.setFont(font)
        self.startnumLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.startnumLineEdit.setObjectName("startnumLineEdit")
        self.gridLayout.addWidget(self.startnumLineEdit, 0, 1, 1, 1)
        self.firstnameLineEdit = QtWidgets.QLineEdit(sendresultForm)
        self.firstnameLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstnameLineEdit.sizePolicy().hasHeightForWidth())
        self.firstnameLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.firstnameLineEdit.setFont(font)
        self.firstnameLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.firstnameLineEdit.setObjectName("firstnameLineEdit")
        self.gridLayout.addWidget(self.firstnameLineEdit, 3, 1, 1, 1)
        self.lastnameLineEdit = QtWidgets.QLineEdit(sendresultForm)
        self.lastnameLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastnameLineEdit.sizePolicy().hasHeightForWidth())
        self.lastnameLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lastnameLineEdit.setFont(font)
        self.lastnameLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.lastnameLineEdit.setObjectName("lastnameLineEdit")
        self.gridLayout.addWidget(self.lastnameLineEdit, 2, 1, 1, 1)
        self.lastnameLabel = QtWidgets.QLabel(sendresultForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastnameLabel.sizePolicy().hasHeightForWidth())
        self.lastnameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lastnameLabel.setFont(font)
        self.lastnameLabel.setObjectName("lastnameLabel")
        self.gridLayout.addWidget(self.lastnameLabel, 2, 0, 1, 1)
        self.timestampLabel = QtWidgets.QLabel(sendresultForm)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.timestampLabel.setFont(font)
        self.timestampLabel.setObjectName("timestampLabel")
        self.gridLayout.addWidget(self.timestampLabel, 5, 0, 1, 1)
        self.firstnameLabel = QtWidgets.QLabel(sendresultForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstnameLabel.sizePolicy().hasHeightForWidth())
        self.firstnameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.firstnameLabel.setFont(font)
        self.firstnameLabel.setObjectName("firstnameLabel")
        self.gridLayout.addWidget(self.firstnameLabel, 3, 0, 1, 1)
        self.startNumLabel = QtWidgets.QLabel(sendresultForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startNumLabel.sizePolicy().hasHeightForWidth())
        self.startNumLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.startNumLabel.setFont(font)
        self.startNumLabel.setObjectName("startNumLabel")
        self.gridLayout.addWidget(self.startNumLabel, 0, 0, 1, 1)
        self.timestampLineEdit = QtWidgets.QLineEdit(sendresultForm)
        self.timestampLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.timestampLineEdit.setFont(font)
        self.timestampLineEdit.setReadOnly(False)
        self.timestampLineEdit.setObjectName("timestampLineEdit")
        self.gridLayout.addWidget(self.timestampLineEdit, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.statusBar = QtWidgets.QLabel(sendresultForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.statusBar.setFont(font)
        self.statusBar.setText("")
        self.statusBar.setObjectName("statusBar")
        self.verticalLayout.addWidget(self.statusBar)

        self.retranslateUi(sendresultForm)
        QtCore.QMetaObject.connectSlotsByName(sendresultForm)

    def retranslateUi(self, sendresultForm):
        _translate = QtCore.QCoreApplication.translate
        sendresultForm.setWindowTitle(_translate("sendresultForm", "send result"))
        self.lastnameLabel.setText(_translate("sendresultForm", "Lastname"))
        self.timestampLabel.setText(_translate("sendresultForm", "Timestamp"))
        self.firstnameLabel.setText(_translate("sendresultForm", "First name"))
        self.startNumLabel.setText(_translate("sendresultForm", "Start num"))
