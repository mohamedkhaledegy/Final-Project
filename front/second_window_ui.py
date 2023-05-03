# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 560)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 160, 111, 31))
        self.pushButton.setFocusPolicy(Qt.TabFocus)
        self.lineEdit_user_log = QLineEdit(self.frame)
        self.lineEdit_user_log.setObjectName(u"lineEdit_user_log")
        self.lineEdit_user_log.setGeometry(QRect(40, 40, 113, 20))
        self.lineEdit_password_log = QLineEdit(self.frame)
        self.lineEdit_password_log.setObjectName(u"lineEdit_password_log")
        self.lineEdit_password_log.setGeometry(QRect(40, 90, 113, 20))
        self.lineEdit_password_log.setEchoMode(QLineEdit.Password)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 51, 21))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 51, 21))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 819, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton, self.lineEdit_user_log)
        QWidget.setTabOrder(self.lineEdit_user_log, self.lineEdit_password_log)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit_password_log.setInputMask("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
    # retranslateUi

