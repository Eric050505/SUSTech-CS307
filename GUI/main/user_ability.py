# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_ability.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modify_L(object):
    def setupUi(self, modify_L):
        modify_L.setObjectName("modify_L")
        modify_L.resize(800, 601)
        self.user = QtWidgets.QLabel(modify_L)
        self.user.setGeometry(QtCore.QRect(40, 40, 111, 16))
        self.user.setObjectName("user")
        self.OK = QtWidgets.QPushButton(modify_L)
        self.OK.setGeometry(QtCore.QRect(640, 480, 150, 46))
        self.OK.setObjectName("OK")
        self.Exit = QtWidgets.QPushButton(modify_L)
        self.Exit.setGeometry(QtCore.QRect(640, 540, 150, 46))
        self.Exit.setObjectName("Exit")
        self.textBrowser = QtWidgets.QTextBrowser(modify_L)
        self.textBrowser.setGeometry(QtCore.QRect(40, 400, 500, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.user_input = QtWidgets.QLineEdit(modify_L)
        self.user_input.setGeometry(QtCore.QRect(190, 40, 291, 20))
        self.user_input.setObjectName("user_input")
        self.ability_input = QtWidgets.QLineEdit(modify_L)
        self.ability_input.setGeometry(QtCore.QRect(190, 80, 291, 20))
        self.ability_input.setText("")
        self.ability_input.setObjectName("ability_input")
        self.permission = QtWidgets.QLabel(modify_L)
        self.permission.setGeometry(QtCore.QRect(40, 80, 111, 16))
        self.permission.setObjectName("ability")
        self.password_input = QtWidgets.QLineEdit(modify_L)
        self.password_input.setGeometry(QtCore.QRect(190, 120, 291, 20))
        self.password_input.setText("")
        self.password_input.setObjectName("password_input")
        self.password = QtWidgets.QLabel(modify_L)
        self.password.setGeometry(QtCore.QRect(40, 120, 111, 16))
        self.password.setObjectName("password")

        self.retranslateUi(modify_L)
        QtCore.QMetaObject.connectSlotsByName(modify_L)

    def retranslateUi(self, modify_L):
        _translate = QtCore.QCoreApplication.translate
        modify_L.setWindowTitle(_translate("modify_L", "Form"))
        self.user.setText(_translate("modify_L", "User:"))
        self.OK.setText(_translate("modify_L", "OK"))
        self.Exit.setText(_translate("modify_L", "Exit"))
        self.permission.setText(_translate("modify_L", "permission:"))
        self.password.setText(_translate("modify_L", "password:"))
