# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serverIpLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.serverIpLabel.setFont(font)
        self.serverIpLabel.setObjectName("serverIpLabel")
        self.horizontalLayout.addWidget(self.serverIpLabel)
        self.serverIpLineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverIpLineEdit.sizePolicy().hasHeightForWidth())
        self.serverIpLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.serverIpLineEdit.setFont(font)
        self.serverIpLineEdit.setObjectName("serverIpLineEdit")
        self.horizontalLayout.addWidget(self.serverIpLineEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chipcontrollIntervalLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chipcontrollIntervalLabel.sizePolicy().hasHeightForWidth())
        self.chipcontrollIntervalLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chipcontrollIntervalLabel.setFont(font)
        self.chipcontrollIntervalLabel.setObjectName("chipcontrollIntervalLabel")
        self.horizontalLayout_3.addWidget(self.chipcontrollIntervalLabel)
        self.chipcontrollIntervalLineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chipcontrollIntervalLineEdit.sizePolicy().hasHeightForWidth())
        self.chipcontrollIntervalLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chipcontrollIntervalLineEdit.setFont(font)
        self.chipcontrollIntervalLineEdit.setObjectName("chipcontrollIntervalLineEdit")
        self.horizontalLayout_3.addWidget(self.chipcontrollIntervalLineEdit)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chipcontrollWaitAfterReadlLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chipcontrollWaitAfterReadlLabel.sizePolicy().hasHeightForWidth())
        self.chipcontrollWaitAfterReadlLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chipcontrollWaitAfterReadlLabel.setFont(font)
        self.chipcontrollWaitAfterReadlLabel.setObjectName("chipcontrollWaitAfterReadlLabel")
        self.horizontalLayout_4.addWidget(self.chipcontrollWaitAfterReadlLabel)
        self.chipcontrollWaitAfterReadlineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chipcontrollWaitAfterReadlineEdit.sizePolicy().hasHeightForWidth())
        self.chipcontrollWaitAfterReadlineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chipcontrollWaitAfterReadlineEdit.setFont(font)
        self.chipcontrollWaitAfterReadlineEdit.setObjectName("chipcontrollWaitAfterReadlineEdit")
        self.horizontalLayout_4.addWidget(self.chipcontrollWaitAfterReadlineEdit)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.autoMaximizeOpeningWindowLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoMaximizeOpeningWindowLabel.sizePolicy().hasHeightForWidth())
        self.autoMaximizeOpeningWindowLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.autoMaximizeOpeningWindowLabel.setFont(font)
        self.autoMaximizeOpeningWindowLabel.setObjectName("autoMaximizeOpeningWindowLabel")
        self.horizontalLayout_5.addWidget(self.autoMaximizeOpeningWindowLabel)
        self.autoMaximizeOpeningWindowCheckBox = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.autoMaximizeOpeningWindowCheckBox.setFont(font)
        self.autoMaximizeOpeningWindowCheckBox.setText("")
        self.autoMaximizeOpeningWindowCheckBox.setObjectName("autoMaximizeOpeningWindowCheckBox")
        self.horizontalLayout_5.addWidget(self.autoMaximizeOpeningWindowCheckBox)
        self.horizontalLayout_5.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.autoResizeWindowLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoResizeWindowLabel.sizePolicy().hasHeightForWidth())
        self.autoResizeWindowLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.autoResizeWindowLabel.setFont(font)
        self.autoResizeWindowLabel.setObjectName("autoResizeWindowLabel")
        self.horizontalLayout_6.addWidget(self.autoResizeWindowLabel)
        self.autoResizeWindowCheckBox = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.autoResizeWindowCheckBox.setFont(font)
        self.autoResizeWindowCheckBox.setText("")
        self.autoResizeWindowCheckBox.setObjectName("autoResizeWindowCheckBox")
        self.horizontalLayout_6.addWidget(self.autoResizeWindowCheckBox)
        self.horizontalLayout_6.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.commPortLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commPortLabel.sizePolicy().hasHeightForWidth())
        self.commPortLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.commPortLabel.setFont(font)
        self.commPortLabel.setObjectName("commPortLabel")
        self.horizontalLayout_2.addWidget(self.commPortLabel)
        self.commPortComboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commPortComboBox.sizePolicy().hasHeightForWidth())
        self.commPortComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.commPortComboBox.setFont(font)
        self.commPortComboBox.setObjectName("commPortComboBox")
        self.horizontalLayout_2.addWidget(self.commPortComboBox)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.savePushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.savePushButton.setFont(font)
        self.savePushButton.setObjectName("savePushButton")
        self.verticalLayout_2.addWidget(self.savePushButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.statusBar = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.statusBar.setFont(font)
        self.statusBar.setText("")
        self.statusBar.setObjectName("statusBar")
        self.gridLayout.addWidget(self.statusBar, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.serverIpLabel.setText(_translate("Form", "Server Ip"))
        self.chipcontrollIntervalLabel.setText(_translate("Form", "Chipcontroll Interval"))
        self.chipcontrollWaitAfterReadlLabel.setText(_translate("Form", "Chipcontroll Wait After Read"))
        self.autoMaximizeOpeningWindowLabel.setText(_translate("Form", "Auto Maximize Opening Window"))
        self.autoResizeWindowLabel.setText(_translate("Form", "Auto Resize Window"))
        self.commPortLabel.setText(_translate("Form", "Comm Port"))
        self.savePushButton.setText(_translate("Form", "save"))
