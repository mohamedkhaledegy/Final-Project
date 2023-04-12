# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database.ui'
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
        MainWindow.resize(849, 648)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_5 = QLineEdit(self.frame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.lineEdit_5, 0, 3, 1, 1)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.lineEdit_6, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 1, 5, 1, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 5, 1, 1)


        self.gridLayout_3.addWidget(self.frame_4, 1, 3, 2, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.frame_3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 849, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ip", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mac address", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"My Device", None))
    # retranslateUi

