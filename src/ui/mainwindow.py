# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserMangerUi(object):
    def setupUi(self, UserMangerUi):
        UserMangerUi.setObjectName("UserMangerUi")
        UserMangerUi.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(UserMangerUi)
        self.centralwidget.setObjectName("centralwidget")
        UserMangerUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UserMangerUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        UserMangerUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UserMangerUi)
        self.statusbar.setObjectName("statusbar")
        UserMangerUi.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(UserMangerUi)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(UserMangerUi)
        QtCore.QMetaObject.connectSlotsByName(UserMangerUi)

    def retranslateUi(self, UserMangerUi):
        _translate = QtCore.QCoreApplication.translate
        UserMangerUi.setWindowTitle(_translate("UserMangerUi", "User manager"))
        self.menuFile.setTitle(_translate("UserMangerUi", "File"))
        self.actionExit.setText(_translate("UserMangerUi", "E&xit"))
