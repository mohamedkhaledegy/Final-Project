# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1076, 771)
        MainWindow.setStyleSheet(u"#menu_widget, #toolBox {\n"
"	background-color: #3333FF;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_11 = QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.gridLayout_4 = QGridLayout(self.main_widget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.search_widget = QWidget(self.main_widget)
        self.search_widget.setObjectName(u"search_widget")
        self.search_widget.setStyleSheet(u"#search_widget {background-color: #ABB2B9;}")
        self.horizontalLayout = QHBoxLayout(self.search_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_8 = QPushButton(self.search_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(30, 30))
        self.pushButton_8.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icon/icon/arrow-96-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon/icon/arrow-31-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(15, 15))
        self.pushButton_8.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.search_frame = QFrame(self.search_widget)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(300, 30))
        self.search_frame.setMaximumSize(QSize(300, 30))
        font = QFont()
        font.setPointSize(10)
        self.search_frame.setFont(font)
        self.search_frame.setAutoFillBackground(False)
        self.search_frame.setStyleSheet(u"#search_frame {\n"
"	border:  1px solid #aa7e6f;\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#search_btn {\n"
"	padding:5px 5px;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#search_btn:pressed {\n"
"	padding-left: 10px;\n"
"}")
        self.search_frame.setFrameShape(QFrame.NoFrame)
        self.search_frame.setFrameShadow(QFrame.Plain)
        self.search_frame.setLineWidth(0)
        self.horizontalLayout_10 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(15, 0, 5, 0)
        self.label_52 = QLabel(self.search_frame)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setEnabled(False)
        self.label_52.setAcceptDrops(False)
        self.label_52.setAutoFillBackground(True)
        self.label_52.setScaledContents(False)

        self.horizontalLayout_10.addWidget(self.label_52)

        self.lcdNumber = QLCDNumber(self.search_frame)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setEnabled(False)
        self.lcdNumber.setAutoFillBackground(True)
        self.lcdNumber.setFrameShape(QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QFrame.Sunken)
        self.lcdNumber.setLineWidth(4)
        self.lcdNumber.setMidLineWidth(3)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber.setProperty("intValue", 0)

        self.horizontalLayout_10.addWidget(self.lcdNumber)


        self.horizontalLayout.addWidget(self.search_frame)

        self.horizontalSpacer_2 = QSpacerItem(209, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_details_new_window = QPushButton(self.search_widget)
        self.pushButton_details_new_window.setObjectName(u"pushButton_details_new_window")
        self.pushButton_details_new_window.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.pushButton_details_new_window)


        self.gridLayout_4.addWidget(self.search_widget, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.main_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(800, 600))
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"#tabWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"	margin-left: 3px;\n"
"	image: url(:/icon/icon/x-mark-4-32.ico)\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"	\n"
"	image: url(:/icon/icon/x-mark-4-48.ico);\n"
"}")
        self.tabWidget.setIconSize(QSize(10, 10))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"tab_home")
        self.gridLayout_5 = QGridLayout(self.tab_home)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(self.tab_home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.splitter_17 = QSplitter(self.frame)
        self.splitter_17.setObjectName(u"splitter_17")
        self.splitter_17.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_17.setOrientation(Qt.Vertical)
        self.splitter_16 = QSplitter(self.splitter_17)
        self.splitter_16.setObjectName(u"splitter_16")
        self.splitter_16.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_16.setOrientation(Qt.Horizontal)
        self.splitter_14 = QSplitter(self.splitter_16)
        self.splitter_14.setObjectName(u"splitter_14")
        sizePolicy.setHeightForWidth(self.splitter_14.sizePolicy().hasHeightForWidth())
        self.splitter_14.setSizePolicy(sizePolicy)
        self.splitter_14.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_14.setOrientation(Qt.Vertical)
        self.frame_5 = QFrame(self.splitter_14)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.splitter_12 = QSplitter(self.frame_5)
        self.splitter_12.setObjectName(u"splitter_12")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter_12.sizePolicy().hasHeightForWidth())
        self.splitter_12.setSizePolicy(sizePolicy1)
        self.splitter_12.setOrientation(Qt.Horizontal)
        self.label_22 = QLabel(self.splitter_12)
        self.label_22.setObjectName(u"label_22")
        self.splitter_12.addWidget(self.label_22)
        self.lineEdit_interface = QLineEdit(self.splitter_12)
        self.lineEdit_interface.setObjectName(u"lineEdit_interface")
        self.splitter_12.addWidget(self.lineEdit_interface)

        self.gridLayout_13.addWidget(self.splitter_12, 0, 0, 1, 1)

        self.pushButton_test_speed = QPushButton(self.frame_5)
        self.pushButton_test_speed.setObjectName(u"pushButton_test_speed")
        self.pushButton_test_speed.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_test_speed.sizePolicy().hasHeightForWidth())
        self.pushButton_test_speed.setSizePolicy(sizePolicy2)

        self.gridLayout_13.addWidget(self.pushButton_test_speed, 0, 4, 1, 1)

        self.pushButton_start_cap = QPushButton(self.frame_5)
        self.pushButton_start_cap.setObjectName(u"pushButton_start_cap")
        sizePolicy2.setHeightForWidth(self.pushButton_start_cap.sizePolicy().hasHeightForWidth())
        self.pushButton_start_cap.setSizePolicy(sizePolicy2)

        self.gridLayout_13.addWidget(self.pushButton_start_cap, 1, 5, 1, 1)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_13.addWidget(self.label_18, 1, 0, 1, 1)

        self.pushButton_stop_cap = QPushButton(self.frame_5)
        self.pushButton_stop_cap.setObjectName(u"pushButton_stop_cap")
        sizePolicy2.setHeightForWidth(self.pushButton_stop_cap.sizePolicy().hasHeightForWidth())
        self.pushButton_stop_cap.setSizePolicy(sizePolicy2)

        self.gridLayout_13.addWidget(self.pushButton_stop_cap, 1, 4, 1, 1)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_13.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_75 = QLabel(self.frame_5)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_13.addWidget(self.label_75, 1, 2, 1, 1)

        self.spinBox_pkt_count_by = QSpinBox(self.frame_5)
        self.spinBox_pkt_count_by.setObjectName(u"spinBox_pkt_count_by")
        self.spinBox_pkt_count_by.setMaximum(1000)
        self.spinBox_pkt_count_by.setValue(4)

        self.gridLayout_13.addWidget(self.spinBox_pkt_count_by, 1, 3, 1, 1)

        self.spinBox_pkt_limit = QSpinBox(self.frame_5)
        self.spinBox_pkt_limit.setObjectName(u"spinBox_pkt_limit")
        self.spinBox_pkt_limit.setMaximum(10000)

        self.gridLayout_13.addWidget(self.spinBox_pkt_limit, 0, 3, 1, 1)

        self.splitter_14.addWidget(self.frame_5)
        self.groupBox_ip_discovered = QGroupBox(self.splitter_14)
        self.groupBox_ip_discovered.setObjectName(u"groupBox_ip_discovered")
        self.groupBox_ip_discovered.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_ip_discovered.sizePolicy().hasHeightForWidth())
        self.groupBox_ip_discovered.setSizePolicy(sizePolicy3)
        self.gridLayout_8 = QGridLayout(self.groupBox_ip_discovered)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.splitter_5 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setMinimumSize(QSize(180, 0))
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.label_21 = QLabel(self.splitter_5)
        self.label_21.setObjectName(u"label_21")
        self.splitter_5.addWidget(self.label_21)
        self.lineEdit_mac2 = QLineEdit(self.splitter_5)
        self.lineEdit_mac2.setObjectName(u"lineEdit_mac2")
        sizePolicy.setHeightForWidth(self.lineEdit_mac2.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac2.setSizePolicy(sizePolicy)
        self.splitter_5.addWidget(self.lineEdit_mac2)

        self.gridLayout_8.addWidget(self.splitter_5, 2, 1, 1, 1)

        self.splitter_2 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_12 = QLabel(self.splitter_2)
        self.label_12.setObjectName(u"label_12")
        self.splitter_2.addWidget(self.label_12)
        self.lineEdit_ip1 = QLineEdit(self.splitter_2)
        self.lineEdit_ip1.setObjectName(u"lineEdit_ip1")
        sizePolicy.setHeightForWidth(self.lineEdit_ip1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip1.setSizePolicy(sizePolicy)
        self.splitter_2.addWidget(self.lineEdit_ip1)

        self.gridLayout_8.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.splitter_6 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_6.setObjectName(u"splitter_6")
        sizePolicy.setHeightForWidth(self.splitter_6.sizePolicy().hasHeightForWidth())
        self.splitter_6.setSizePolicy(sizePolicy)
        self.splitter_6.setMinimumSize(QSize(180, 0))
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.label_24 = QLabel(self.splitter_6)
        self.label_24.setObjectName(u"label_24")
        self.splitter_6.addWidget(self.label_24)
        self.lineEdit_mac3 = QLineEdit(self.splitter_6)
        self.lineEdit_mac3.setObjectName(u"lineEdit_mac3")
        sizePolicy.setHeightForWidth(self.lineEdit_mac3.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac3.setSizePolicy(sizePolicy)
        self.lineEdit_mac3.setMaximumSize(QSize(16777215, 23))
        self.splitter_6.addWidget(self.lineEdit_mac3)

        self.gridLayout_8.addWidget(self.splitter_6, 3, 1, 1, 1)

        self.splitter_4 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_4.setObjectName(u"splitter_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.splitter_4.sizePolicy().hasHeightForWidth())
        self.splitter_4.setSizePolicy(sizePolicy4)
        self.splitter_4.setMinimumSize(QSize(180, 0))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label_20 = QLabel(self.splitter_4)
        self.label_20.setObjectName(u"label_20")
        self.splitter_4.addWidget(self.label_20)
        self.lineEdit_mac1 = QLineEdit(self.splitter_4)
        self.lineEdit_mac1.setObjectName(u"lineEdit_mac1")
        sizePolicy.setHeightForWidth(self.lineEdit_mac1.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac1.setSizePolicy(sizePolicy)
        self.splitter_4.addWidget(self.lineEdit_mac1)

        self.gridLayout_8.addWidget(self.splitter_4, 1, 1, 1, 1)

        self.splitter_3 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_19 = QLabel(self.splitter_3)
        self.label_19.setObjectName(u"label_19")
        self.splitter_3.addWidget(self.label_19)
        self.lineEdit_ip2 = QLineEdit(self.splitter_3)
        self.lineEdit_ip2.setObjectName(u"lineEdit_ip2")
        sizePolicy.setHeightForWidth(self.lineEdit_ip2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip2.setSizePolicy(sizePolicy)
        self.splitter_3.addWidget(self.lineEdit_ip2)

        self.gridLayout_8.addWidget(self.splitter_3, 2, 0, 1, 1)

        self.splitter_7 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.label_25 = QLabel(self.splitter_7)
        self.label_25.setObjectName(u"label_25")
        self.splitter_7.addWidget(self.label_25)
        self.lineEdit_ip3 = QLineEdit(self.splitter_7)
        self.lineEdit_ip3.setObjectName(u"lineEdit_ip3")
        sizePolicy.setHeightForWidth(self.lineEdit_ip3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip3.setSizePolicy(sizePolicy)
        self.splitter_7.addWidget(self.lineEdit_ip3)

        self.gridLayout_8.addWidget(self.splitter_7, 3, 0, 1, 1)

        self.splitter_8 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setMinimumSize(QSize(180, 0))
        self.splitter_8.setOrientation(Qt.Horizontal)
        self.label_26 = QLabel(self.splitter_8)
        self.label_26.setObjectName(u"label_26")
        self.splitter_8.addWidget(self.label_26)
        self.lineEdit_mac4 = QLineEdit(self.splitter_8)
        self.lineEdit_mac4.setObjectName(u"lineEdit_mac4")
        sizePolicy.setHeightForWidth(self.lineEdit_mac4.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac4.setSizePolicy(sizePolicy)
        self.splitter_8.addWidget(self.lineEdit_mac4)

        self.gridLayout_8.addWidget(self.splitter_8, 4, 1, 1, 1)

        self.splitter_11 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_11.setObjectName(u"splitter_11")
        self.splitter_11.setMinimumSize(QSize(180, 0))
        self.splitter_11.setOrientation(Qt.Horizontal)
        self.label_29 = QLabel(self.splitter_11)
        self.label_29.setObjectName(u"label_29")
        self.splitter_11.addWidget(self.label_29)
        self.lineEdit_mac5 = QLineEdit(self.splitter_11)
        self.lineEdit_mac5.setObjectName(u"lineEdit_mac5")
        sizePolicy.setHeightForWidth(self.lineEdit_mac5.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac5.setSizePolicy(sizePolicy)
        self.splitter_11.addWidget(self.lineEdit_mac5)

        self.gridLayout_8.addWidget(self.splitter_11, 5, 1, 1, 1)

        self.splitter_9 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_9.setOrientation(Qt.Horizontal)
        self.label_27 = QLabel(self.splitter_9)
        self.label_27.setObjectName(u"label_27")
        self.splitter_9.addWidget(self.label_27)
        self.lineEdit_ip4 = QLineEdit(self.splitter_9)
        self.lineEdit_ip4.setObjectName(u"lineEdit_ip4")
        sizePolicy.setHeightForWidth(self.lineEdit_ip4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip4.setSizePolicy(sizePolicy)
        self.splitter_9.addWidget(self.lineEdit_ip4)

        self.gridLayout_8.addWidget(self.splitter_9, 4, 0, 1, 1)

        self.splitter_10 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_10.setOrientation(Qt.Horizontal)
        self.label_28 = QLabel(self.splitter_10)
        self.label_28.setObjectName(u"label_28")
        self.splitter_10.addWidget(self.label_28)
        self.lineEdit_ip5 = QLineEdit(self.splitter_10)
        self.lineEdit_ip5.setObjectName(u"lineEdit_ip5")
        sizePolicy.setHeightForWidth(self.lineEdit_ip5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip5.setSizePolicy(sizePolicy)
        self.splitter_10.addWidget(self.lineEdit_ip5)

        self.gridLayout_8.addWidget(self.splitter_10, 5, 0, 1, 1)

        self.pushButton_ping3 = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_ping3.setObjectName(u"pushButton_ping3")
        self.pushButton_ping3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_ping3, 3, 3, 1, 1)

        self.pushButton_ping5 = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_ping5.setObjectName(u"pushButton_ping5")
        self.pushButton_ping5.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_ping5, 5, 3, 1, 1)

        self.pushButton_ping1 = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_ping1.setObjectName(u"pushButton_ping1")
        self.pushButton_ping1.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_ping1, 1, 3, 1, 1)

        self.pushButton_ping4 = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_ping4.setObjectName(u"pushButton_ping4")
        self.pushButton_ping4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_ping4, 4, 3, 1, 1)

        self.pushButton_ping2 = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_ping2.setObjectName(u"pushButton_ping2")
        self.pushButton_ping2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_ping2, 2, 3, 1, 1)

        self.label_ping_status_ip1 = QLabel(self.groupBox_ip_discovered)
        self.label_ping_status_ip1.setObjectName(u"label_ping_status_ip1")
        self.label_ping_status_ip1.setMinimumSize(QSize(40, 0))
        self.label_ping_status_ip1.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_ping_status_ip1, 1, 2, 1, 1)

        self.label_ping_status_ip2 = QLabel(self.groupBox_ip_discovered)
        self.label_ping_status_ip2.setObjectName(u"label_ping_status_ip2")
        self.label_ping_status_ip2.setMinimumSize(QSize(40, 0))
        self.label_ping_status_ip2.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_ping_status_ip2, 2, 2, 1, 1)

        self.label_ping_status_ip5 = QLabel(self.groupBox_ip_discovered)
        self.label_ping_status_ip5.setObjectName(u"label_ping_status_ip5")
        self.label_ping_status_ip5.setMinimumSize(QSize(40, 0))
        self.label_ping_status_ip5.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_ping_status_ip5, 5, 2, 1, 1)

        self.label_ping_status_ip4 = QLabel(self.groupBox_ip_discovered)
        self.label_ping_status_ip4.setObjectName(u"label_ping_status_ip4")
        self.label_ping_status_ip4.setMinimumSize(QSize(40, 0))
        self.label_ping_status_ip4.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_ping_status_ip4, 4, 2, 1, 1)

        self.label_ping_status_ip3 = QLabel(self.groupBox_ip_discovered)
        self.label_ping_status_ip3.setObjectName(u"label_ping_status_ip3")
        self.label_ping_status_ip3.setMinimumSize(QSize(40, 0))
        self.label_ping_status_ip3.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_ping_status_ip3, 3, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        self.pushButton_5.setMinimumSize(QSize(0, 30))

        self.gridLayout_8.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.splitter_14.addWidget(self.groupBox_ip_discovered)
        self.splitter_16.addWidget(self.splitter_14)
        self.frame_3 = QFrame(self.splitter_16)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(500, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_square_4 = roundProgressBar(self.frame_3)
        self.widget_square_4.setObjectName(u"widget_square_4")

        self.gridLayout_7.addWidget(self.widget_square_4, 0, 1, 1, 1)

        self.widget_square_3 = roundProgressBar(self.frame_3)
        self.widget_square_3.setObjectName(u"widget_square_3")

        self.gridLayout_7.addWidget(self.widget_square_3, 1, 0, 1, 1)

        self.widget_square_1 = roundProgressBar(self.frame_3)
        self.widget_square_1.setObjectName(u"widget_square_1")

        self.gridLayout_7.addWidget(self.widget_square_1, 0, 0, 1, 1)

        self.widget_square_2 = roundProgressBar(self.frame_3)
        self.widget_square_2.setObjectName(u"widget_square_2")

        self.gridLayout_7.addWidget(self.widget_square_2, 1, 1, 1, 1)

        self.splitter_16.addWidget(self.frame_3)
        self.splitter_17.addWidget(self.splitter_16)
        self.frame_4 = QFrame(self.splitter_17)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget_cap = QTableWidget(self.frame_4)
        if (self.tableWidget_cap.columnCount() < 11):
            self.tableWidget_cap.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_cap.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget_cap.setObjectName(u"tableWidget_cap")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(100)
        sizePolicy5.setHeightForWidth(self.tableWidget_cap.sizePolicy().hasHeightForWidth())
        self.tableWidget_cap.setSizePolicy(sizePolicy5)
        self.tableWidget_cap.setMinimumSize(QSize(600, 300))
        self.tableWidget_cap.setMaximumSize(QSize(12132312, 16777215))
        self.tableWidget_cap.setAutoFillBackground(True)
        self.tableWidget_cap.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_cap.setLineWidth(1)
        self.tableWidget_cap.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_cap.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        self.tableWidget_cap.setDragDropOverwriteMode(False)
        self.tableWidget_cap.setAlternatingRowColors(True)
        self.tableWidget_cap.setShowGrid(False)
        self.tableWidget_cap.setSortingEnabled(True)
        self.tableWidget_cap.setRowCount(0)
        self.tableWidget_cap.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_cap.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_cap.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_cap.verticalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tableWidget_cap, 0, 0, 1, 1)

        self.splitter_17.addWidget(self.frame_4)

        self.gridLayout_12.addWidget(self.splitter_17, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_home, "")
        self.tab_network = QWidget()
        self.tab_network.setObjectName(u"tab_network")
        self.gridLayout_40 = QGridLayout(self.tab_network)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.frame_2 = QFrame(self.tab_network)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_2)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.groupBox_network = QGroupBox(self.frame_2)
        self.groupBox_network.setObjectName(u"groupBox_network")
        self.groupBox_network.setEnabled(False)
        self.groupBox_network.setMaximumSize(QSize(500, 60))
        self.gridLayout_3 = QGridLayout(self.groupBox_network)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter_15 = QSplitter(self.groupBox_network)
        self.splitter_15.setObjectName(u"splitter_15")
        self.splitter_15.setOrientation(Qt.Horizontal)
        self.label_13 = QLabel(self.splitter_15)
        self.label_13.setObjectName(u"label_13")
        self.splitter_15.addWidget(self.label_13)
        self.lineEdit_ip_host = QLineEdit(self.splitter_15)
        self.lineEdit_ip_host.setObjectName(u"lineEdit_ip_host")
        sizePolicy.setHeightForWidth(self.lineEdit_ip_host.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip_host.setSizePolicy(sizePolicy)
        self.splitter_15.addWidget(self.lineEdit_ip_host)

        self.gridLayout_3.addWidget(self.splitter_15, 0, 0, 1, 1)

        self.splitter_13 = QSplitter(self.groupBox_network)
        self.splitter_13.setObjectName(u"splitter_13")
        self.splitter_13.setOrientation(Qt.Horizontal)
        self.label_23 = QLabel(self.splitter_13)
        self.label_23.setObjectName(u"label_23")
        self.splitter_13.addWidget(self.label_23)
        self.lineEdit_mac_host = QLineEdit(self.splitter_13)
        self.lineEdit_mac_host.setObjectName(u"lineEdit_mac_host")
        sizePolicy.setHeightForWidth(self.lineEdit_mac_host.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac_host.setSizePolicy(sizePolicy)
        self.lineEdit_mac_host.setMinimumSize(QSize(180, 0))
        self.splitter_13.addWidget(self.lineEdit_mac_host)

        self.gridLayout_3.addWidget(self.splitter_13, 0, 1, 1, 1)


        self.gridLayout_28.addWidget(self.groupBox_network, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_27 = QGridLayout(self.widget_4)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_bandwidth_services = QLabel(self.widget_4)
        self.label_bandwidth_services.setObjectName(u"label_bandwidth_services")

        self.gridLayout_27.addWidget(self.label_bandwidth_services, 2, 0, 1, 2)

        self.tableWidget_bandwidth_services = QTableWidget(self.widget_4)
        if (self.tableWidget_bandwidth_services.columnCount() < 4):
            self.tableWidget_bandwidth_services.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_bandwidth_services.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_bandwidth_services.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_bandwidth_services.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_bandwidth_services.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.tableWidget_bandwidth_services.setObjectName(u"tableWidget_bandwidth_services")

        self.gridLayout_27.addWidget(self.tableWidget_bandwidth_services, 3, 0, 1, 2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_60 = QLabel(self.widget_4)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_11.addWidget(self.label_60)

        self.spinBox_timeout_bandwidth_services = QSpinBox(self.widget_4)
        self.spinBox_timeout_bandwidth_services.setObjectName(u"spinBox_timeout_bandwidth_services")
        self.spinBox_timeout_bandwidth_services.setMaximum(100000)
        self.spinBox_timeout_bandwidth_services.setValue(10)

        self.horizontalLayout_11.addWidget(self.spinBox_timeout_bandwidth_services)

        self.label_61 = QLabel(self.widget_4)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_11.addWidget(self.label_61)


        self.gridLayout_27.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_51 = QLabel(self.widget_4)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_9.addWidget(self.label_51)

        self.doubleSpinBox_bandwidth_services = QDoubleSpinBox(self.widget_4)
        self.doubleSpinBox_bandwidth_services.setObjectName(u"doubleSpinBox_bandwidth_services")
        self.doubleSpinBox_bandwidth_services.setValue(1.000000000000000)

        self.horizontalLayout_9.addWidget(self.doubleSpinBox_bandwidth_services)

        self.label_57 = QLabel(self.widget_4)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_9.addWidget(self.label_57)


        self.gridLayout_27.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.pushButton_bandwidth_services = QPushButton(self.widget_4)
        self.pushButton_bandwidth_services.setObjectName(u"pushButton_bandwidth_services")

        self.gridLayout_27.addWidget(self.pushButton_bandwidth_services, 0, 1, 2, 1)


        self.gridLayout_28.addWidget(self.widget_4, 0, 1, 2, 1)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_13 = QFrame(self.groupBox)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_13)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.label_bandwidth_down_speed = QLabel(self.frame_13)
        self.label_bandwidth_down_speed.setObjectName(u"label_bandwidth_down_speed")

        self.gridLayout_38.addWidget(self.label_bandwidth_down_speed, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.gridLayout_38.addWidget(self.frame_15, 0, 1, 1, 1)

        self.label_bandwidth_down_speed_2 = QLabel(self.frame_13)
        self.label_bandwidth_down_speed_2.setObjectName(u"label_bandwidth_down_speed_2")

        self.gridLayout_38.addWidget(self.label_bandwidth_down_speed_2, 0, 2, 1, 1)

        self.label_bandwidth_upload_speed = QLabel(self.frame_13)
        self.label_bandwidth_upload_speed.setObjectName(u"label_bandwidth_upload_speed")

        self.gridLayout_38.addWidget(self.label_bandwidth_upload_speed, 1, 0, 1, 1)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout_38.addWidget(self.frame_14, 1, 1, 1, 1)

        self.label_bandwidth_upload_speed_2 = QLabel(self.frame_13)
        self.label_bandwidth_upload_speed_2.setObjectName(u"label_bandwidth_upload_speed_2")

        self.gridLayout_38.addWidget(self.label_bandwidth_upload_speed_2, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_13, 4, 1, 2, 3)

        self.lineEdit_bandwidth_down = QLineEdit(self.groupBox)
        self.lineEdit_bandwidth_down.setObjectName(u"lineEdit_bandwidth_down")

        self.gridLayout_2.addWidget(self.lineEdit_bandwidth_down, 1, 2, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_8.addWidget(self.label_14)

        self.doubleSpinBox_bandwidth = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_bandwidth.setObjectName(u"doubleSpinBox_bandwidth")
        self.doubleSpinBox_bandwidth.setValue(1.000000000000000)

        self.horizontalLayout_8.addWidget(self.doubleSpinBox_bandwidth)

        self.label_50 = QLabel(self.groupBox)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_8.addWidget(self.label_50)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox_timeout_bandwidth = QSpinBox(self.groupBox)
        self.spinBox_timeout_bandwidth.setObjectName(u"spinBox_timeout_bandwidth")
        self.spinBox_timeout_bandwidth.setMaximum(100000)
        self.spinBox_timeout_bandwidth.setValue(7)

        self.horizontalLayout_3.addWidget(self.spinBox_timeout_bandwidth)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 3, 1, 1)

        self.lineEdit_bandwidth_upload = QLineEdit(self.groupBox)
        self.lineEdit_bandwidth_upload.setObjectName(u"lineEdit_bandwidth_upload")

        self.gridLayout_2.addWidget(self.lineEdit_bandwidth_upload, 2, 2, 1, 1)

        self.pushButton_start_bandwidth = QPushButton(self.groupBox)
        self.pushButton_start_bandwidth.setObjectName(u"pushButton_start_bandwidth")

        self.gridLayout_2.addWidget(self.pushButton_start_bandwidth, 0, 2, 1, 1)

        self.label_bandwidth = QLabel(self.groupBox)
        self.label_bandwidth.setObjectName(u"label_bandwidth")

        self.gridLayout_2.addWidget(self.label_bandwidth, 1, 1, 1, 1)

        self.label_bandwidth_3 = QLabel(self.groupBox)
        self.label_bandwidth_3.setObjectName(u"label_bandwidth_3")

        self.gridLayout_2.addWidget(self.label_bandwidth_3, 2, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 1, 1, 3)


        self.gridLayout_28.addWidget(self.groupBox, 1, 0, 1, 1)


        self.gridLayout_40.addWidget(self.frame_2, 0, 0, 1, 3)

        self.horizontalSpacer_7 = QSpacerItem(243, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_network)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_25 = QGridLayout(self.groupBox_2)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_64 = QLabel(self.groupBox_2)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_25.addWidget(self.label_64, 2, 0, 1, 1)

        self.label_62 = QLabel(self.groupBox_2)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_25.addWidget(self.label_62, 0, 0, 1, 1)

        self.label_63 = QLabel(self.groupBox_2)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_25.addWidget(self.label_63, 1, 0, 1, 1)

        self.lineEdit_site_name1 = QLineEdit(self.groupBox_2)
        self.lineEdit_site_name1.setObjectName(u"lineEdit_site_name1")

        self.gridLayout_25.addWidget(self.lineEdit_site_name1, 0, 1, 1, 1)

        self.lineEdit_site_name2 = QLineEdit(self.groupBox_2)
        self.lineEdit_site_name2.setObjectName(u"lineEdit_site_name2")

        self.gridLayout_25.addWidget(self.lineEdit_site_name2, 1, 1, 1, 1)

        self.label_status_site2 = QLabel(self.groupBox_2)
        self.label_status_site2.setObjectName(u"label_status_site2")

        self.gridLayout_25.addWidget(self.label_status_site2, 1, 2, 1, 1)

        self.lineEdit_site_name3 = QLineEdit(self.groupBox_2)
        self.lineEdit_site_name3.setObjectName(u"lineEdit_site_name3")

        self.gridLayout_25.addWidget(self.lineEdit_site_name3, 2, 1, 1, 1)

        self.label_status_site1 = QLabel(self.groupBox_2)
        self.label_status_site1.setObjectName(u"label_status_site1")

        self.gridLayout_25.addWidget(self.label_status_site1, 0, 2, 1, 1)

        self.label_status_site3 = QLabel(self.groupBox_2)
        self.label_status_site3.setObjectName(u"label_status_site3")

        self.gridLayout_25.addWidget(self.label_status_site3, 2, 2, 1, 1)

        self.label_status_site1_2 = QLabel(self.groupBox_2)
        self.label_status_site1_2.setObjectName(u"label_status_site1_2")

        self.gridLayout_25.addWidget(self.label_status_site1_2, 0, 3, 1, 1)

        self.label_status_site3_2 = QLabel(self.groupBox_2)
        self.label_status_site3_2.setObjectName(u"label_status_site3_2")

        self.gridLayout_25.addWidget(self.label_status_site3_2, 2, 3, 1, 1)

        self.label_status_site2_2 = QLabel(self.groupBox_2)
        self.label_status_site2_2.setObjectName(u"label_status_site2_2")

        self.gridLayout_25.addWidget(self.label_status_site2_2, 1, 3, 1, 1)

        self.pushButton_site_block = QPushButton(self.groupBox_2)
        self.pushButton_site_block.setObjectName(u"pushButton_site_block")

        self.gridLayout_25.addWidget(self.pushButton_site_block, 3, 2, 1, 2)

        self.checkBox_disable_www = QCheckBox(self.groupBox_2)
        self.checkBox_disable_www.setObjectName(u"checkBox_disable_www")
        self.checkBox_disable_www.setTristate(False)

        self.gridLayout_25.addWidget(self.checkBox_disable_www, 3, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_25.addWidget(self.checkBox, 3, 0, 1, 1)


        self.gridLayout_40.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(243, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 188, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_40.addItem(self.verticalSpacer_8, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_network, "")
        self.tab_account = QWidget()
        self.tab_account.setObjectName(u"tab_account")
        self.gridLayout_26 = QGridLayout(self.tab_account)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.groupBox_5 = QGroupBox(self.tab_account)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_19 = QGridLayout(self.groupBox_5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_41 = QLabel(self.groupBox_5)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_19.addWidget(self.label_41, 0, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.groupBox_5)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setFrame(True)
        self.lineEdit_17.setClearButtonEnabled(False)

        self.gridLayout_19.addWidget(self.lineEdit_17, 0, 1, 1, 1)

        self.label_42 = QLabel(self.groupBox_5)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_19.addWidget(self.label_42, 1, 0, 1, 1)

        self.lineEdit_18 = QLineEdit(self.groupBox_5)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_19.addWidget(self.lineEdit_18, 1, 1, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_account)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_21 = QGridLayout(self.groupBox_6)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_43 = QLabel(self.groupBox_6)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_21.addWidget(self.label_43, 0, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.groupBox_6)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_21.addWidget(self.lineEdit_19, 0, 1, 1, 1)

        self.label_44 = QLabel(self.groupBox_6)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_21.addWidget(self.label_44, 1, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.groupBox_6)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout_21.addWidget(self.lineEdit_20, 1, 1, 1, 1)

        self.label_45 = QLabel(self.groupBox_6)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_21.addWidget(self.label_45, 2, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.groupBox_6)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_21.addWidget(self.lineEdit_21, 2, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.groupBox_6)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_21.addWidget(self.pushButton_12, 3, 1, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_6, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(279, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(272, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_9, 1, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(272, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_10, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(271, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.groupBox_8 = QGroupBox(self.tab_account)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_39 = QGridLayout(self.groupBox_8)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.label_71 = QLabel(self.groupBox_8)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_39.addWidget(self.label_71, 2, 0, 1, 1)

        self.label_72 = QLabel(self.groupBox_8)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_39.addWidget(self.label_72, 0, 0, 1, 1)

        self.label_73 = QLabel(self.groupBox_8)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_39.addWidget(self.label_73, 1, 0, 1, 1)

        self.lineEdit_iface_name = QLineEdit(self.groupBox_8)
        self.lineEdit_iface_name.setObjectName(u"lineEdit_iface_name")

        self.gridLayout_39.addWidget(self.lineEdit_iface_name, 0, 1, 1, 1)

        self.lineEdit_ip_router = QLineEdit(self.groupBox_8)
        self.lineEdit_ip_router.setObjectName(u"lineEdit_ip_router")

        self.gridLayout_39.addWidget(self.lineEdit_ip_router, 1, 1, 1, 1)

        self.lineEdit_ip_master = QLineEdit(self.groupBox_8)
        self.lineEdit_ip_master.setObjectName(u"lineEdit_ip_master")

        self.gridLayout_39.addWidget(self.lineEdit_ip_master, 2, 1, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_8, 2, 2, 1, 1)

        self.frame_16 = QFrame(self.tab_account)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.checkBox_save_packet = QCheckBox(self.frame_16)
        self.checkBox_save_packet.setObjectName(u"checkBox_save_packet")
        self.checkBox_save_packet.setGeometry(QRect(20, 20, 221, 21))
        self.checkBox_show_packet = QCheckBox(self.frame_16)
        self.checkBox_show_packet.setObjectName(u"checkBox_show_packet")
        self.checkBox_show_packet.setGeometry(QRect(20, 50, 221, 21))
        self.checkBox_listen_blocked_sites = QCheckBox(self.frame_16)
        self.checkBox_listen_blocked_sites.setObjectName(u"checkBox_listen_blocked_sites")
        self.checkBox_listen_blocked_sites.setGeometry(QRect(20, 80, 221, 21))

        self.gridLayout_26.addWidget(self.frame_16, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_account, "")
        self.tab_database = QWidget()
        self.tab_database.setObjectName(u"tab_database")
        self.groupBox_7 = QGroupBox(self.tab_database)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(260, 90, 301, 241))
        self.lineEdit_database_name = QLineEdit(self.groupBox_7)
        self.lineEdit_database_name.setObjectName(u"lineEdit_database_name")
        self.lineEdit_database_name.setGeometry(QRect(112, 30, 111, 20))
        self.lineEdit_database_name.setFrame(True)
        self.lineEdit_database_name.setClearButtonEnabled(False)
        self.label_53 = QLabel(self.groupBox_7)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(20, 30, 81, 21))
        self.label_54 = QLabel(self.groupBox_7)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(20, 60, 81, 21))
        self.lineEdit_count_ip = QLineEdit(self.groupBox_7)
        self.lineEdit_count_ip.setObjectName(u"lineEdit_count_ip")
        self.lineEdit_count_ip.setGeometry(QRect(110, 60, 60, 20))
        self.label_55 = QLabel(self.groupBox_7)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(20, 90, 81, 21))
        self.lineEdit_count_ping = QLineEdit(self.groupBox_7)
        self.lineEdit_count_ping.setObjectName(u"lineEdit_count_ping")
        self.lineEdit_count_ping.setGeometry(QRect(110, 90, 61, 20))
        self.lineEdit_count_ping_2 = QLineEdit(self.groupBox_7)
        self.lineEdit_count_ping_2.setObjectName(u"lineEdit_count_ping_2")
        self.lineEdit_count_ping_2.setGeometry(QRect(110, 120, 61, 20))
        self.label_74 = QLabel(self.groupBox_7)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(20, 120, 81, 21))
        self.pushButton_refresh_db = QPushButton(self.groupBox_7)
        self.pushButton_refresh_db.setObjectName(u"pushButton_refresh_db")
        self.pushButton_refresh_db.setGeometry(QRect(184, 182, 91, 31))
        self.tabWidget.addTab(self.tab_database, "")
        self.tab_ping = QWidget()
        self.tab_ping.setObjectName(u"tab_ping")
        self.frame_12 = QFrame(self.tab_ping)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 0, 861, 649))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_12)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.splitter_18 = QSplitter(self.frame_12)
        self.splitter_18.setObjectName(u"splitter_18")
        self.splitter_18.setOrientation(Qt.Horizontal)
        self.frame_8 = QFrame(self.splitter_18)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_8)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.verticalSpacer_4 = QSpacerItem(20, 147, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_37.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.tabWidget_pinger = QTabWidget(self.frame_8)
        self.tabWidget_pinger.setObjectName(u"tabWidget_pinger")
        self.char0 = QWidget()
        self.char0.setObjectName(u"char0")
        self.gridLayout_32 = QGridLayout(self.char0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.tableWidget_ping_ip1 = QTableWidget(self.char0)
        self.tableWidget_ping_ip1.setObjectName(u"tableWidget_ping_ip1")

        self.gridLayout_32.addWidget(self.tableWidget_ping_ip1, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 259, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.tableWidget_ping_ip2 = QTableWidget(self.char0)
        self.tableWidget_ping_ip2.setObjectName(u"tableWidget_ping_ip2")

        self.gridLayout_32.addWidget(self.tableWidget_ping_ip2, 0, 2, 1, 1)

        self.tabWidget_pinger.addTab(self.char0, "")
        self.char1 = QWidget()
        self.char1.setObjectName(u"char1")
        self.gridLayout_20 = QGridLayout(self.char1)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.widget = QWidget(self.char1)
        self.widget.setObjectName(u"widget")
        self.gridLayout_22 = QGridLayout(self.widget)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_10 = QFrame(self.widget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.grafica_uno = QVBoxLayout()
        self.grafica_uno.setObjectName(u"grafica_uno")

        self.verticalLayout_3.addLayout(self.grafica_uno)


        self.gridLayout_22.addWidget(self.frame_10, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.widget, 0, 0, 1, 1)

        self.tabWidget_pinger.addTab(self.char1, "")
        self.char2 = QWidget()
        self.char2.setObjectName(u"char2")
        self.gridLayout_24 = QGridLayout(self.char2)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.widget_2 = QWidget(self.char2)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_23 = QGridLayout(self.widget_2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.frame_18 = QFrame(self.widget_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_18)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.grafica_tres = QVBoxLayout()
        self.grafica_tres.setObjectName(u"grafica_tres")

        self.gridLayout_30.addLayout(self.grafica_tres, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_18, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.widget_2, 0, 0, 1, 1)

        self.tabWidget_pinger.addTab(self.char2, "")
        self.char3 = QWidget()
        self.char3.setObjectName(u"char3")
        self.gridLayout_35 = QGridLayout(self.char3)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.widget_6 = QWidget(self.char3)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_29 = QGridLayout(self.widget_6)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.frame_21 = QFrame(self.widget_6)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_21)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.grafica_cuatro = QVBoxLayout()
        self.grafica_cuatro.setObjectName(u"grafica_cuatro")

        self.gridLayout_34.addLayout(self.grafica_cuatro, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.frame_21, 0, 0, 1, 1)


        self.gridLayout_35.addWidget(self.widget_6, 0, 0, 1, 1)

        self.tabWidget_pinger.addTab(self.char3, "")
        self.char4 = QWidget()
        self.char4.setObjectName(u"char4")
        self.gridLayout_36 = QGridLayout(self.char4)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.widget_7 = QWidget(self.char4)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_31 = QGridLayout(self.widget_7)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.frame_11 = QFrame(self.widget_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.grafica_dos = QVBoxLayout()
        self.grafica_dos.setObjectName(u"grafica_dos")

        self.verticalLayout_4.addLayout(self.grafica_dos)


        self.gridLayout_31.addWidget(self.frame_11, 0, 0, 1, 1)


        self.gridLayout_36.addWidget(self.widget_7, 0, 0, 1, 1)

        self.tabWidget_pinger.addTab(self.char4, "")

        self.gridLayout_37.addWidget(self.tabWidget_pinger, 1, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 146, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_37.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.splitter_18.addWidget(self.frame_8)
        self.frame_9 = QFrame(self.splitter_18)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_9)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_38 = QLabel(self.frame_9)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_6.addWidget(self.label_38)

        self.doubleSpinBox_ping_stepby_2 = QDoubleSpinBox(self.frame_9)
        self.doubleSpinBox_ping_stepby_2.setObjectName(u"doubleSpinBox_ping_stepby_2")
        self.doubleSpinBox_ping_stepby_2.setValue(1.000000000000000)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_ping_stepby_2)

        self.label_47 = QLabel(self.frame_9)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_6.addWidget(self.label_47)


        self.gridLayout_33.addLayout(self.horizontalLayout_6, 2, 0, 1, 2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_48 = QLabel(self.frame_9)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_7.addWidget(self.label_48)

        self.spinBox_ping_timeout_2 = QSpinBox(self.frame_9)
        self.spinBox_ping_timeout_2.setObjectName(u"spinBox_ping_timeout_2")
        self.spinBox_ping_timeout_2.setValue(10)

        self.horizontalLayout_7.addWidget(self.spinBox_ping_timeout_2)

        self.label_49 = QLabel(self.frame_9)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_7.addWidget(self.label_49)


        self.gridLayout_33.addLayout(self.horizontalLayout_7, 1, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_33.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_chcker_ping_2 = QPushButton(self.frame_9)
        self.pushButton_chcker_ping_2.setObjectName(u"pushButton_chcker_ping_2")

        self.gridLayout_33.addWidget(self.pushButton_chcker_ping_2, 0, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_33.addItem(self.verticalSpacer_6, 3, 1, 1, 1)

        self.splitter_18.addWidget(self.frame_9)

        self.gridLayout_18.addWidget(self.splitter_18, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_ping, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.pushButton_capture = QPushButton(self.tab_5)
        self.pushButton_capture.setObjectName(u"pushButton_capture")
        self.pushButton_capture.setGeometry(QRect(20, 10, 101, 31))
        self.pushButton_checker_ping = QPushButton(self.tab_5)
        self.pushButton_checker_ping.setObjectName(u"pushButton_checker_ping")
        self.pushButton_checker_ping.setGeometry(QRect(20, 50, 101, 31))
        self.pushButton_save_ping = QPushButton(self.tab_5)
        self.pushButton_save_ping.setObjectName(u"pushButton_save_ping")
        self.pushButton_save_ping.setGeometry(QRect(20, 90, 101, 31))
        self.comboBox_2 = QComboBox(self.tab_5)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(130, 90, 161, 31))
        self.layoutWidget = QWidget(self.tab_5)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 50, 191, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.layoutWidget)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_4.addWidget(self.label_33)

        self.spinBox_ping_timeout = QSpinBox(self.layoutWidget)
        self.spinBox_ping_timeout.setObjectName(u"spinBox_ping_timeout")
        self.spinBox_ping_timeout.setValue(10)

        self.horizontalLayout_4.addWidget(self.spinBox_ping_timeout)

        self.label_34 = QLabel(self.layoutWidget)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_4.addWidget(self.label_34)

        self.layoutWidget_2 = QWidget(self.tab_5)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(332, 50, 161, 31))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.layoutWidget_2)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_5.addWidget(self.label_35)

        self.doubleSpinBox_ping_stepby = QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBox_ping_stepby.setObjectName(u"doubleSpinBox_ping_stepby")
        self.doubleSpinBox_ping_stepby.setValue(1.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_ping_stepby)

        self.label_36 = QLabel(self.layoutWidget_2)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_5.addWidget(self.label_36)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_10 = QGridLayout(self.tab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_infos = QFrame(self.tab)
        self.frame_infos.setObjectName(u"frame_infos")
        self.frame_infos.setFrameShape(QFrame.StyledPanel)
        self.frame_infos.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_infos)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_6 = QFrame(self.frame_infos)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_circle_3 = QFrame(self.frame_6)
        self.frame_circle_3.setObjectName(u"frame_circle_3")
        self.frame_circle_3.setMinimumSize(QSize(250, 250))
        self.frame_circle_3.setMaximumSize(QSize(250, 250))
        self.frame_circle_3.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle_3.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_circle_3)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 50, 10, 50)
        self.label_37 = QLabel(self.frame_circle_3)
        self.label_37.setObjectName(u"label_37")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(11)
        self.label_37.setFont(font1)
        self.label_37.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_37)

        self.label_upload_meter = QLabel(self.frame_circle_3)
        self.label_upload_meter.setObjectName(u"label_upload_meter")
        font2 = QFont()
        font2.setFamily(u"Roboto Thin")
        font2.setPointSize(60)
        self.label_upload_meter.setFont(font2)
        self.label_upload_meter.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_upload_meter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_upload_meter)

        self.label_40 = QLabel(self.frame_circle_3)
        self.label_40.setObjectName(u"label_40")
        sizePolicy4.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(10)
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_40)


        self.gridLayout_14.addWidget(self.frame_circle_3, 0, 2, 1, 1)

        self.frame_circle_1 = QFrame(self.frame_6)
        self.frame_circle_1.setObjectName(u"frame_circle_1")
        self.frame_circle_1.setMinimumSize(QSize(150, 150))
        self.frame_circle_1.setMaximumSize(QSize(250, 250))
        self.frame_circle_1.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle_1.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_circle_1)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 50, 10, 50)
        self.label_3 = QLabel(self.frame_circle_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_meter_ip = QLabel(self.frame_circle_1)
        self.label_meter_ip.setObjectName(u"label_meter_ip")
        font4 = QFont()
        font4.setFamily(u"Roboto")
        font4.setPointSize(8)
        self.label_meter_ip.setFont(font4)
        self.label_meter_ip.setStyleSheet(u"border: none;\n"
" color: rgb(128, 102, 168);")
        self.label_meter_ip.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_meter_ip)

        self.label_meter_ping = QLabel(self.frame_circle_1)
        self.label_meter_ping.setObjectName(u"label_meter_ping")
        self.label_meter_ping.setFont(font2)
        self.label_meter_ping.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_meter_ping.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_meter_ping)


        self.gridLayout_14.addWidget(self.frame_circle_1, 0, 0, 1, 1)

        self.frame_circle_4 = QFrame(self.frame_6)
        self.frame_circle_4.setObjectName(u"frame_circle_4")
        self.frame_circle_4.setMinimumSize(QSize(250, 250))
        self.frame_circle_4.setMaximumSize(QSize(250, 250))
        self.frame_circle_4.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle_4.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_circle_4)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 50, 10, 50)
        self.label_56 = QLabel(self.frame_circle_4)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font1)
        self.label_56.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_56)

        self.label_download_meter = QLabel(self.frame_circle_4)
        self.label_download_meter.setObjectName(u"label_download_meter")
        self.label_download_meter.setFont(font2)
        self.label_download_meter.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_download_meter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_download_meter)

        self.label_59 = QLabel(self.frame_circle_4)
        self.label_59.setObjectName(u"label_59")
        sizePolicy4.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy4)
        self.label_59.setFont(font3)
        self.label_59.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_59)


        self.gridLayout_14.addWidget(self.frame_circle_4, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.frame_6, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_infos)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.groupBox_4 = QGroupBox(self.frame_7)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 200))
        self.gridLayout_15 = QGridLayout(self.groupBox_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_15.addWidget(self.label_7, 0, 0, 1, 2)

        self.lineEdit_download = QLineEdit(self.groupBox_4)
        self.lineEdit_download.setObjectName(u"lineEdit_download")
        self.lineEdit_download.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_download.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_download, 0, 2, 1, 2)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_15.addWidget(self.label_6, 0, 4, 1, 1)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_15.addWidget(self.label_11, 0, 5, 1, 2)

        self.lineEdit_upload = QLineEdit(self.groupBox_4)
        self.lineEdit_upload.setObjectName(u"lineEdit_upload")
        self.lineEdit_upload.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_upload.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_upload, 0, 7, 1, 1)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_15.addWidget(self.label_15, 0, 8, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_15.addWidget(self.label_9, 1, 0, 1, 1)

        self.lineEdit_ping = QLineEdit(self.groupBox_4)
        self.lineEdit_ping.setObjectName(u"lineEdit_ping")
        self.lineEdit_ping.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_ping.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_ping, 1, 1, 1, 2)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_15.addWidget(self.label_8, 1, 3, 1, 2)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_15.addWidget(self.label_17, 1, 5, 1, 1)

        self.lineEdit_sponsor = QLineEdit(self.groupBox_4)
        self.lineEdit_sponsor.setObjectName(u"lineEdit_sponsor")
        self.lineEdit_sponsor.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_sponsor, 1, 6, 1, 3)

        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_15.addWidget(self.label_16, 2, 0, 1, 1)

        self.lineEdit_host = QLineEdit(self.groupBox_4)
        self.lineEdit_host.setObjectName(u"lineEdit_host")
        self.lineEdit_host.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_host, 2, 1, 1, 4)

        self.label_30 = QLabel(self.groupBox_4)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_15.addWidget(self.label_30, 2, 5, 1, 1)

        self.lineEdit_city = QLineEdit(self.groupBox_4)
        self.lineEdit_city.setObjectName(u"lineEdit_city")
        self.lineEdit_city.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_city, 2, 6, 1, 3)

        self.label_46 = QLabel(self.groupBox_4)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_15.addWidget(self.label_46, 3, 0, 1, 1)

        self.lineEdit_lon = QLineEdit(self.groupBox_4)
        self.lineEdit_lon.setObjectName(u"lineEdit_lon")
        self.lineEdit_lon.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_lon, 3, 1, 1, 4)

        self.label_31 = QLabel(self.groupBox_4)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_15.addWidget(self.label_31, 3, 5, 1, 1)

        self.lineEdit_lat = QLineEdit(self.groupBox_4)
        self.lineEdit_lat.setObjectName(u"lineEdit_lat")
        self.lineEdit_lat.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_lat, 3, 6, 1, 3)


        self.gridLayout_16.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 182, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(404, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(404, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.frame_7, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_infos, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_17 = QGridLayout(self.tab_6)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_devices = QFrame(self.tab_6)
        self.frame_devices.setObjectName(u"frame_devices")
        self.frame_devices.setFrameShape(QFrame.StyledPanel)
        self.frame_devices.setFrameShadow(QFrame.Raised)
        self.frame_17 = QFrame(self.frame_devices)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(10, 30, 841, 311))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.groupBox_3 = QGroupBox(self.frame_17)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 0, 831, 301))
        self.splitter_19 = QSplitter(self.groupBox_3)
        self.splitter_19.setObjectName(u"splitter_19")
        self.splitter_19.setGeometry(QRect(20, 30, 178, 23))
        self.splitter_19.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_19.setOrientation(Qt.Horizontal)
        self.label_32 = QLabel(self.splitter_19)
        self.label_32.setObjectName(u"label_32")
        self.splitter_19.addWidget(self.label_32)
        self.lineEdit_ip1_to_ping = QLineEdit(self.splitter_19)
        self.lineEdit_ip1_to_ping.setObjectName(u"lineEdit_ip1_to_ping")
        sizePolicy.setHeightForWidth(self.lineEdit_ip1_to_ping.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip1_to_ping.setSizePolicy(sizePolicy)
        self.splitter_19.addWidget(self.lineEdit_ip1_to_ping)
        self.splitter_20 = QSplitter(self.groupBox_3)
        self.splitter_20.setObjectName(u"splitter_20")
        self.splitter_20.setGeometry(QRect(210, 30, 111, 23))
        self.splitter_20.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_20.setOrientation(Qt.Horizontal)
        self.label_39 = QLabel(self.splitter_20)
        self.label_39.setObjectName(u"label_39")
        self.splitter_20.addWidget(self.label_39)
        self.lineEdit_ip1_ping_count = QLineEdit(self.splitter_20)
        self.lineEdit_ip1_ping_count.setObjectName(u"lineEdit_ip1_ping_count")
        sizePolicy.setHeightForWidth(self.lineEdit_ip1_ping_count.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip1_ping_count.setSizePolicy(sizePolicy)
        self.splitter_20.addWidget(self.lineEdit_ip1_ping_count)
        self.splitter_21 = QSplitter(self.groupBox_3)
        self.splitter_21.setObjectName(u"splitter_21")
        self.splitter_21.setGeometry(QRect(330, 30, 178, 23))
        self.splitter_21.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_21.setOrientation(Qt.Horizontal)
        self.label_58 = QLabel(self.splitter_21)
        self.label_58.setObjectName(u"label_58")
        self.splitter_21.addWidget(self.label_58)
        self.lineEdit_ip1_ping_last = QLineEdit(self.splitter_21)
        self.lineEdit_ip1_ping_last.setObjectName(u"lineEdit_ip1_ping_last")
        sizePolicy.setHeightForWidth(self.lineEdit_ip1_ping_last.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip1_ping_last.setSizePolicy(sizePolicy)
        self.splitter_21.addWidget(self.lineEdit_ip1_ping_last)
        self.splitter_22 = QSplitter(self.groupBox_3)
        self.splitter_22.setObjectName(u"splitter_22")
        self.splitter_22.setGeometry(QRect(330, 60, 178, 23))
        self.splitter_22.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_22.setOrientation(Qt.Horizontal)
        self.label_65 = QLabel(self.splitter_22)
        self.label_65.setObjectName(u"label_65")
        self.splitter_22.addWidget(self.label_65)
        self.lineEdit_ip1_ping_last_2 = QLineEdit(self.splitter_22)
        self.lineEdit_ip1_ping_last_2.setObjectName(u"lineEdit_ip1_ping_last_2")
        sizePolicy.setHeightForWidth(self.lineEdit_ip1_ping_last_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip1_ping_last_2.setSizePolicy(sizePolicy)
        self.splitter_22.addWidget(self.lineEdit_ip1_ping_last_2)
        self.splitter_23 = QSplitter(self.groupBox_3)
        self.splitter_23.setObjectName(u"splitter_23")
        self.splitter_23.setGeometry(QRect(210, 60, 111, 23))
        self.splitter_23.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_23.setOrientation(Qt.Horizontal)
        self.label_66 = QLabel(self.splitter_23)
        self.label_66.setObjectName(u"label_66")
        self.splitter_23.addWidget(self.label_66)
        self.lineEdit_ip1_ping_count_2 = QLineEdit(self.splitter_23)
        self.lineEdit_ip1_ping_count_2.setObjectName(u"lineEdit_ip1_ping_count_2")
        sizePolicy.setHeightForWidth(self.lineEdit_ip1_ping_count_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip1_ping_count_2.setSizePolicy(sizePolicy)
        self.splitter_23.addWidget(self.lineEdit_ip1_ping_count_2)
        self.splitter_24 = QSplitter(self.groupBox_3)
        self.splitter_24.setObjectName(u"splitter_24")
        self.splitter_24.setGeometry(QRect(20, 60, 178, 23))
        self.splitter_24.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_24.setOrientation(Qt.Horizontal)
        self.label_67 = QLabel(self.splitter_24)
        self.label_67.setObjectName(u"label_67")
        self.splitter_24.addWidget(self.label_67)
        self.lineEdit_ip1_to_ping_2 = QLineEdit(self.splitter_24)
        self.lineEdit_ip1_to_ping_2.setObjectName(u"lineEdit_ip1_to_ping_2")
        sizePolicy.setHeightForWidth(self.lineEdit_ip1_to_ping_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip1_to_ping_2.setSizePolicy(sizePolicy)
        self.splitter_24.addWidget(self.lineEdit_ip1_to_ping_2)
        self.splitter_25 = QSplitter(self.groupBox_3)
        self.splitter_25.setObjectName(u"splitter_25")
        self.splitter_25.setGeometry(QRect(330, 90, 178, 23))
        self.splitter_25.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_25.setOrientation(Qt.Horizontal)
        self.label_68 = QLabel(self.splitter_25)
        self.label_68.setObjectName(u"label_68")
        self.splitter_25.addWidget(self.label_68)
        self.lineEdit_ip1_ping_last_3 = QLineEdit(self.splitter_25)
        self.lineEdit_ip1_ping_last_3.setObjectName(u"lineEdit_ip1_ping_last_3")
        sizePolicy.setHeightForWidth(self.lineEdit_ip1_ping_last_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip1_ping_last_3.setSizePolicy(sizePolicy)
        self.splitter_25.addWidget(self.lineEdit_ip1_ping_last_3)
        self.splitter_26 = QSplitter(self.groupBox_3)
        self.splitter_26.setObjectName(u"splitter_26")
        self.splitter_26.setGeometry(QRect(210, 90, 111, 23))
        self.splitter_26.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_26.setOrientation(Qt.Horizontal)
        self.label_69 = QLabel(self.splitter_26)
        self.label_69.setObjectName(u"label_69")
        self.splitter_26.addWidget(self.label_69)
        self.lineEdit_ip1_ping_count_3 = QLineEdit(self.splitter_26)
        self.lineEdit_ip1_ping_count_3.setObjectName(u"lineEdit_ip1_ping_count_3")
        sizePolicy.setHeightForWidth(self.lineEdit_ip1_ping_count_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip1_ping_count_3.setSizePolicy(sizePolicy)
        self.splitter_26.addWidget(self.lineEdit_ip1_ping_count_3)
        self.splitter_27 = QSplitter(self.groupBox_3)
        self.splitter_27.setObjectName(u"splitter_27")
        self.splitter_27.setGeometry(QRect(20, 90, 178, 23))
        self.splitter_27.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_27.setOrientation(Qt.Horizontal)
        self.label_70 = QLabel(self.splitter_27)
        self.label_70.setObjectName(u"label_70")
        self.splitter_27.addWidget(self.label_70)
        self.lineEdit_ip1_to_ping_3 = QLineEdit(self.splitter_27)
        self.lineEdit_ip1_to_ping_3.setObjectName(u"lineEdit_ip1_to_ping_3")
        sizePolicy.setHeightForWidth(self.lineEdit_ip1_to_ping_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip1_to_ping_3.setSizePolicy(sizePolicy)
        self.splitter_27.addWidget(self.lineEdit_ip1_to_ping_3)
        self.label_76 = QLabel(self.groupBox_3)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(670, 20, 81, 21))
        self.lineEdit_count_ping_3 = QLineEdit(self.groupBox_3)
        self.lineEdit_count_ping_3.setObjectName(u"lineEdit_count_ping_3")
        self.lineEdit_count_ping_3.setGeometry(QRect(760, 20, 61, 20))
        self.pushButton_refresh_db_2 = QPushButton(self.groupBox_3)
        self.pushButton_refresh_db_2.setObjectName(u"pushButton_refresh_db_2")
        self.pushButton_refresh_db_2.setGeometry(QRect(740, 50, 91, 31))
        self.frame_19 = QFrame(self.frame_devices)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(10, 350, 841, 271))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.gridLayout_17.addWidget(self.frame_devices, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")

        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.main_widget, 0, 1, 1, 1)

        self.menu_widget = QWidget(self.centralwidget)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setMinimumSize(QSize(170, 0))
        self.menu_widget.setStyleSheet(u"background-color: #06162d;\n"
"color: #fff;\n"
"border: none;")
        self.gridLayout = QGridLayout(self.menu_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 15)
        self.toolBox = QToolBox(self.menu_widget)
        self.toolBox.setObjectName(u"toolBox")
        font5 = QFont()
        font5.setPointSize(12)
        self.toolBox.setFont(font5)
        self.toolBox.setStyleSheet(u"#toolBox {\n"
"	color: #fff;\n"
"}\n"
"\n"
"#toolBox::tab {\n"
"	padding-left:5px;\n"
"	text-align:left;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"#toolBox::tab:selected {\n"
"	background-color: #2d9cdb;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#toolBox QPushButton {\n"
"	padding:5px 0px 5px 20px;\n"
"	text-align:left;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"#toolBox QPushButton:hover {\n"
"	background-color: #85C1E9;\n"
"}\n"
"\n"
"#toolBox QPushButton:checked {\n"
"	background-color: #3498DB;\n"
"}\n"
"\n"
"")
        self.general_page = QWidget()
        self.general_page.setObjectName(u"general_page")
        self.general_page.setGeometry(QRect(0, 0, 162, 640))
        self.verticalLayout = QVBoxLayout(self.general_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, 5)
        self.pushButton_home = QPushButton(self.general_page)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setFont(font)
        self.pushButton_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_home.setFocusPolicy(Qt.NoFocus)
        self.pushButton_home.setStyleSheet(u"")
        self.pushButton_home.setCheckable(False)
        self.pushButton_home.setChecked(False)

        self.verticalLayout.addWidget(self.pushButton_home)

        self.pushButton_device_details = QPushButton(self.general_page)
        self.pushButton_device_details.setObjectName(u"pushButton_device_details")
        self.pushButton_device_details.setFont(font)
        self.pushButton_device_details.setFocusPolicy(Qt.NoFocus)
        self.pushButton_device_details.setStyleSheet(u"")
        self.pushButton_device_details.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_device_details)

        self.pushButton_system_functions = QPushButton(self.general_page)
        self.pushButton_system_functions.setObjectName(u"pushButton_system_functions")
        self.pushButton_system_functions.setFont(font)
        self.pushButton_system_functions.setFocusPolicy(Qt.NoFocus)
        self.pushButton_system_functions.setStyleSheet(u"")
        self.pushButton_system_functions.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_system_functions)

        self.pushButton_devices = QPushButton(self.general_page)
        self.pushButton_devices.setObjectName(u"pushButton_devices")
        self.pushButton_devices.setFont(font)
        self.pushButton_devices.setFocusPolicy(Qt.NoFocus)
        self.pushButton_devices.setStyleSheet(u"")
        self.pushButton_devices.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_devices)

        self.pushButton_meters = QPushButton(self.general_page)
        self.pushButton_meters.setObjectName(u"pushButton_meters")
        self.pushButton_meters.setFont(font)
        self.pushButton_meters.setFocusPolicy(Qt.NoFocus)
        self.pushButton_meters.setStyleSheet(u"")
        self.pushButton_meters.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_meters)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/home-4-48 (2).ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.general_page, icon1, u"General")
        self.cars_page = QWidget()
        self.cars_page.setObjectName(u"cars_page")
        self.cars_page.setGeometry(QRect(0, 0, 162, 640))
        self.verticalLayout_2 = QVBoxLayout(self.cars_page)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.pushButton_network_config = QPushButton(self.cars_page)
        self.pushButton_network_config.setObjectName(u"pushButton_network_config")
        self.pushButton_network_config.setFont(font)
        self.pushButton_network_config.setFocusPolicy(Qt.NoFocus)
        self.pushButton_network_config.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_network_config)

        self.pushButton_acc_config = QPushButton(self.cars_page)
        self.pushButton_acc_config.setObjectName(u"pushButton_acc_config")
        self.pushButton_acc_config.setFont(font)
        self.pushButton_acc_config.setFocusPolicy(Qt.NoFocus)
        self.pushButton_acc_config.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_acc_config)

        self.pushButton_database_settings = QPushButton(self.cars_page)
        self.pushButton_database_settings.setObjectName(u"pushButton_database_settings")
        self.pushButton_database_settings.setFont(font)
        self.pushButton_database_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_database_settings.setFocusPolicy(Qt.NoFocus)
        self.pushButton_database_settings.setStyleSheet(u"")
        self.pushButton_database_settings.setCheckable(False)
        self.pushButton_database_settings.setChecked(False)

        self.verticalLayout_2.addWidget(self.pushButton_database_settings)

        self.verticalSpacer_2 = QSpacerItem(20, 350, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        icon2 = QIcon()
        iconThemeName = u"t"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.toolBox.addItem(self.cars_page, icon2, u"Settings")

        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.menu_widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setAutoFillBackground(True)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.pushButton_8.toggled.connect(self.menu_widget.setHidden)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_pinger.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(10)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_8.setText("")
#if QT_CONFIG(tooltip)
        self.label_52.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Online Devices On Network", None))
        self.pushButton_details_new_window.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Interface", None))
        self.pushButton_test_speed.setText(QCoreApplication.translate("MainWindow", u"Test Speed", None))
        self.pushButton_start_cap.setText(QCoreApplication.translate("MainWindow", u"Start Capture", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Main Device", None))
        self.pushButton_stop_cap.setText(QCoreApplication.translate("MainWindow", u"Stop Capture", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Packet Limit", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Loop Sniff Every (Packet)", None))
        self.groupBox_ip_discovered.setTitle(QCoreApplication.translate("MainWindow", u"Ip Discovered", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Mac Address", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ip 1", None))
        self.lineEdit_ip1.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Mac Address", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Mac Address", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Ip 2", None))
        self.lineEdit_ip2.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Ip 3", None))
        self.lineEdit_ip3.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Mac Address", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Mac Address", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Ip 4", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Ip 5", None))
        self.pushButton_ping3.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.pushButton_ping5.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.pushButton_ping1.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.pushButton_ping4.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.pushButton_ping2.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.label_ping_status_ip1.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_ping_status_ip2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_ping_status_ip5.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_ping_status_ip4.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_ping_status_ip3.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Scan Network", None))
        ___qtablewidgetitem = self.tableWidget_cap.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No", None));
        ___qtablewidgetitem1 = self.tableWidget_cap.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Time Stamp", None));
        ___qtablewidgetitem2 = self.tableWidget_cap.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Source", None));
        ___qtablewidgetitem3 = self.tableWidget_cap.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Destination", None));
        ___qtablewidgetitem4 = self.tableWidget_cap.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Service", None));
        ___qtablewidgetitem5 = self.tableWidget_cap.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Site Name", None));
        ___qtablewidgetitem6 = self.tableWidget_cap.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Port Src", None));
        ___qtablewidgetitem7 = self.tableWidget_cap.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Port Dst", None));
        ___qtablewidgetitem8 = self.tableWidget_cap.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Blocked", None));
        ___qtablewidgetitem9 = self.tableWidget_cap.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Length Packet", None));
        ___qtablewidgetitem10 = self.tableWidget_cap.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Info", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.groupBox_network.setTitle(QCoreApplication.translate("MainWindow", u"Network", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Host IP", None))
        self.lineEdit_ip_host.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Host Mac Address", None))
        self.label_bandwidth_services.setText(QCoreApplication.translate("MainWindow", u"Services", None))
        ___qtablewidgetitem11 = self.tableWidget_bandwidth_services.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        ___qtablewidgetitem12 = self.tableWidget_bandwidth_services.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem13 = self.tableWidget_bandwidth_services.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Donwload", None));
        ___qtablewidgetitem14 = self.tableWidget_bandwidth_services.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Upload", None));
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Timeout", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"By Second", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Refresh Time", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"By Second", None))
        self.pushButton_bandwidth_services.setText(QCoreApplication.translate("MainWindow", u"Bandwidth With Services Info", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Network", None))
        self.label_bandwidth_down_speed.setText(QCoreApplication.translate("MainWindow", u"Download ", None))
        self.label_bandwidth_down_speed_2.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_bandwidth_upload_speed.setText(QCoreApplication.translate("MainWindow", u"Upload ", None))
        self.label_bandwidth_upload_speed_2.setText(QCoreApplication.translate("MainWindow", u"Upload ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Refresh Time", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"By Second", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Timeout", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"By Second", None))
        self.pushButton_start_bandwidth.setText(QCoreApplication.translate("MainWindow", u"Start Bandwidth", None))
        self.label_bandwidth.setText(QCoreApplication.translate("MainWindow", u"Downloaded : ", None))
        self.label_bandwidth_3.setText(QCoreApplication.translate("MainWindow", u"Uploaded : ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Interface", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Local Area Connection", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Sites Config", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Site Name 3", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Site Name 1", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Site Name 2", None))
        self.label_status_site2.setText(QCoreApplication.translate("MainWindow", u"Status Site 2", None))
        self.label_status_site1.setText(QCoreApplication.translate("MainWindow", u"Status Site 1", None))
        self.label_status_site3.setText(QCoreApplication.translate("MainWindow", u"Status Site 3", None))
        self.label_status_site1_2.setText(QCoreApplication.translate("MainWindow", u"Visited ?", None))
        self.label_status_site3_2.setText(QCoreApplication.translate("MainWindow", u"Visited ?", None))
        self.label_status_site2_2.setText(QCoreApplication.translate("MainWindow", u"Visited ?", None))
        self.pushButton_site_block.setText(QCoreApplication.translate("MainWindow", u"Block Sites", None))
        self.checkBox_disable_www.setText(QCoreApplication.translate("MainWindow", u"Disable add www / .com", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Save To DB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_network), QCoreApplication.translate("MainWindow", u"Network Configuration", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"User Info", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_18.setText(QCoreApplication.translate("MainWindow", u"*******", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Old Password", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Password Confiramtion", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Network Scanner Config", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"IP Master", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Network Card Name", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"IP Router", None))
        self.checkBox_save_packet.setText(QCoreApplication.translate("MainWindow", u"Save Captured Packets To Db", None))
        self.checkBox_show_packet.setText(QCoreApplication.translate("MainWindow", u"Show Packets (While Sniff )", None))
        self.checkBox_listen_blocked_sites.setText(QCoreApplication.translate("MainWindow", u"Listen While sniff To Blocked Sites", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_account), QCoreApplication.translate("MainWindow", u"Account Configuration", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Data Base Info", None))
        self.lineEdit_database_name.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Database Name", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Ip Count", None))
        self.lineEdit_count_ip.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Pings Count", None))
        self.lineEdit_count_ping.setText("")
        self.lineEdit_count_ping_2.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Packet Count", None))
        self.pushButton_refresh_db.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_database), QCoreApplication.translate("MainWindow", u"Database Settings", None))
        self.tabWidget_pinger.setTabText(self.tabWidget_pinger.indexOf(self.char0), QCoreApplication.translate("MainWindow", u"Table", None))
        self.tabWidget_pinger.setTabText(self.tabWidget_pinger.indexOf(self.char1), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget_pinger.setTabText(self.tabWidget_pinger.indexOf(self.char2), QCoreApplication.translate("MainWindow", u"Tab2", None))
        self.tabWidget_pinger.setTabText(self.tabWidget_pinger.indexOf(self.char3), QCoreApplication.translate("MainWindow", u"Tab3", None))
        self.tabWidget_pinger.setTabText(self.tabWidget_pinger.indexOf(self.char4), QCoreApplication.translate("MainWindow", u"Tab4", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Step By", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"By Second", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Timeout", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"By Second", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_chcker_ping_2.setText(QCoreApplication.translate("MainWindow", u"Start Ping Checker", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ping), QCoreApplication.translate("MainWindow", u"Devices Checker", None))
        self.pushButton_capture.setText(QCoreApplication.translate("MainWindow", u"Start Capture 2", None))
        self.pushButton_checker_ping.setText(QCoreApplication.translate("MainWindow", u"Start Ping Checker", None))
        self.pushButton_save_ping.setText(QCoreApplication.translate("MainWindow", u"Save Ping In DB", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Timeout", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"By Second", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Step By", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"By Second", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"System Functions", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_upload_meter.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"-- Mb Uploaded", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.label_meter_ip.setText(QCoreApplication.translate("MainWindow", u"192.168.1.2", None))
        self.label_meter_ping.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" vertical-align:super;\">0.0 m/s</span></p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_download_meter.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"-- Mb Downloaded", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Internet Speed", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Download Speed", None))
        self.lineEdit_download.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MB/S", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Upload Speed", None))
        self.lineEdit_upload.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MB/S", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.lineEdit_ping.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Sponsor", None))
        self.lineEdit_sponsor.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.lineEdit_host.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.lineEdit_city.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Lon", None))
        self.lineEdit_lon.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Lat", None))
        self.lineEdit_lat.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Internet Meters", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Devices Ping", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Ip 1", None))
        self.lineEdit_ip1_to_ping.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Count Ping", None))
        self.lineEdit_ip1_ping_count.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Last Seen", None))
        self.lineEdit_ip1_ping_last.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Last Seen", None))
        self.lineEdit_ip1_ping_last_2.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Count Ping", None))
        self.lineEdit_ip1_ping_count_2.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Ip 2", None))
        self.lineEdit_ip1_to_ping_2.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Last Seen", None))
        self.lineEdit_ip1_ping_last_3.setText("")
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Count Ping", None))
        self.lineEdit_ip1_ping_count_3.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Ip 3", None))
        self.lineEdit_ip1_to_ping_3.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Pings Count (DB)", None))
        self.lineEdit_count_ping_3.setText("")
        self.pushButton_refresh_db_2.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Devices", None))
        self.pushButton_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_device_details.setText(QCoreApplication.translate("MainWindow", u"Specific Device", None))
        self.pushButton_system_functions.setText(QCoreApplication.translate("MainWindow", u"System Functions", None))
        self.pushButton_devices.setText(QCoreApplication.translate("MainWindow", u"Devices", None))
        self.pushButton_meters.setText(QCoreApplication.translate("MainWindow", u"Meters", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.general_page), QCoreApplication.translate("MainWindow", u"General", None))
        self.pushButton_network_config.setText(QCoreApplication.translate("MainWindow", u"Network Configuration", None))
        self.pushButton_acc_config.setText(QCoreApplication.translate("MainWindow", u"Account Configuration", None))
        self.pushButton_database_settings.setText(QCoreApplication.translate("MainWindow", u"Database Settings", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.cars_page), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

