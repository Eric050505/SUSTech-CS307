# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RigesterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RigesterWindow(object):
    def setupUi0(self, LogWindow):
        LogWindow.setObjectName("LogWindow")
        LogWindow.resize(800, 600)
        self.UserName = QtWidgets.QLineEdit(LogWindow)
        self.UserName.setGeometry(QtCore.QRect(280, 180, 226, 40))
        self.UserName.setObjectName("UserName")

        self.Password_2 = QtWidgets.QLineEdit(LogWindow)
        self.Password_2.setGeometry(QtCore.QRect(280, 240, 226, 40))
        self.Password_2.setObjectName("Password_2")

        self.identityInput = QtWidgets.QLineEdit(LogWindow)
        self.identityInput.setGeometry(QtCore.QRect(280, 300, 226, 40))
        self.identityInput.setObjectName("identityInput")

        self.USer = QtWidgets.QLabel(LogWindow)
        self.USer.setGeometry(QtCore.QRect(200, 180, 62, 40))
        self.USer.setObjectName("USer")

        self.Password = QtWidgets.QLabel(LogWindow)
        self.Password.setGeometry(QtCore.QRect(160, 240, 108, 32))
        self.Password.setObjectName("Password")

        self.RegisterLable = QtWidgets.QLabel(LogWindow)
        self.RegisterLable.setGeometry(QtCore.QRect(360, 120, 102, 32))
        self.RegisterLable.setObjectName("RegisterLable")

        self.identity = QtWidgets.QLabel(LogWindow)
        self.identity.setGeometry(QtCore.QRect(160, 300, 108, 32))
        self.identity.setObjectName("Identity")



        self.Register_2 = QtWidgets.QPushButton(LogWindow)
        self.Register_2.setGeometry(QtCore.QRect(260, 400, 122, 46))
        self.Register_2.setObjectName("Register_2")

        self.UserTips = QtWidgets.QLabel(LogWindow)
        self.UserTips.setGeometry(QtCore.QRect(520, 180, 200, 32))
        self.UserTips.setText("This is user tips")
        self.UserTips.setObjectName("UserTips")

        self.PasswordTips = QtWidgets.QLabel(LogWindow)
        self.PasswordTips.setGeometry(QtCore.QRect(520, 240, 200, 32))
        self.PasswordTips.setText("This is password tips")
        self.PasswordTips.setObjectName("PasswordTips")

        self.IdentityTips = QtWidgets.QLabel(LogWindow)
        self.IdentityTips.setGeometry(QtCore.QRect(520, 300, 300, 32))
        self.IdentityTips.setText("This is identity tips")
        self.IdentityTips.setObjectName("IdentityTips")

        self.Back = QtWidgets.QPushButton(LogWindow)
        self.Back.setGeometry(QtCore.QRect(400, 400, 122, 46))
        self.Back.setObjectName("Back")

        self.retranslateUi(LogWindow)
        QtCore.QMetaObject.connectSlotsByName(LogWindow)

    def retranslateUi(self, LogWindow):
        _translate = QtCore.QCoreApplication.translate
        LogWindow.setWindowTitle(_translate("LogWindow", "Form"))
        self.USer.setText(_translate("LogWindow", "User:"))
        self.Password.setText(_translate("LogWindow", "Password:"))
        self.RegisterLable.setText(_translate("LogWindow", "Register"))
        self.Register_2.setText(_translate("LogWindow", "Register"))
        self.Back.setText(_translate("LogWindow", "Back"))
        self.identity.setText(_translate("LogWindow","identity:"))
        self.IdentityTips.setText(_translate("LogWindow","IdentityTips"))
