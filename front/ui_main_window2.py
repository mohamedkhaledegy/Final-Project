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
        MainWindow.resize(1079, 771)
        MainWindow.setStyleSheet(u"#menu_widget, #toolBox {\n"
"	background-color: #3333FF;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_11 = QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QSize(810, 600))
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.menu_widget = QWidget(self.splitter)
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
        font = QFont()
        font.setPointSize(12)
        self.toolBox.setFont(font)
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
        font1 = QFont()
        font1.setPointSize(10)
        self.pushButton_home.setFont(font1)
        self.pushButton_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_home.setFocusPolicy(Qt.NoFocus)
        self.pushButton_home.setStyleSheet(u"")
        self.pushButton_home.setCheckable(False)
        self.pushButton_home.setChecked(False)

        self.verticalLayout.addWidget(self.pushButton_home)

        self.pushButton_device_details = QPushButton(self.general_page)
        self.pushButton_device_details.setObjectName(u"pushButton_device_details")
        self.pushButton_device_details.setFont(font1)
        self.pushButton_device_details.setFocusPolicy(Qt.NoFocus)
        self.pushButton_device_details.setStyleSheet(u"")
        self.pushButton_device_details.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_device_details)

        self.pushButton_system_functions = QPushButton(self.general_page)
        self.pushButton_system_functions.setObjectName(u"pushButton_system_functions")
        self.pushButton_system_functions.setFont(font1)
        self.pushButton_system_functions.setFocusPolicy(Qt.NoFocus)
        self.pushButton_system_functions.setStyleSheet(u"")
        self.pushButton_system_functions.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_system_functions)

        self.pushButton_devices = QPushButton(self.general_page)
        self.pushButton_devices.setObjectName(u"pushButton_devices")
        self.pushButton_devices.setFont(font1)
        self.pushButton_devices.setFocusPolicy(Qt.NoFocus)
        self.pushButton_devices.setStyleSheet(u"")
        self.pushButton_devices.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_devices)

        self.pushButton_meters = QPushButton(self.general_page)
        self.pushButton_meters.setObjectName(u"pushButton_meters")
        self.pushButton_meters.setFont(font1)
        self.pushButton_meters.setFocusPolicy(Qt.NoFocus)
        self.pushButton_meters.setStyleSheet(u"")
        self.pushButton_meters.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_meters)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        icon = QIcon()
        icon.addFile(u":/icon/icon/home-4-48 (2).ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.general_page, icon, u"General")
        self.cars_page = QWidget()
        self.cars_page.setObjectName(u"cars_page")
        self.cars_page.setGeometry(QRect(0, 0, 162, 640))
        self.verticalLayout_2 = QVBoxLayout(self.cars_page)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.pushButton_network_config = QPushButton(self.cars_page)
        self.pushButton_network_config.setObjectName(u"pushButton_network_config")
        self.pushButton_network_config.setFont(font1)
        self.pushButton_network_config.setFocusPolicy(Qt.NoFocus)
        self.pushButton_network_config.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_network_config)

        self.pushButton_acc_config = QPushButton(self.cars_page)
        self.pushButton_acc_config.setObjectName(u"pushButton_acc_config")
        self.pushButton_acc_config.setFont(font1)
        self.pushButton_acc_config.setFocusPolicy(Qt.NoFocus)
        self.pushButton_acc_config.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_acc_config)

        self.pushButton_database_settings = QPushButton(self.cars_page)
        self.pushButton_database_settings.setObjectName(u"pushButton_database_settings")
        self.pushButton_database_settings.setFont(font1)
        self.pushButton_database_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_database_settings.setFocusPolicy(Qt.NoFocus)
        self.pushButton_database_settings.setStyleSheet(u"")
        self.pushButton_database_settings.setCheckable(False)
        self.pushButton_database_settings.setChecked(False)

        self.verticalLayout_2.addWidget(self.pushButton_database_settings)

        self.verticalSpacer_2 = QSpacerItem(20, 350, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        icon1 = QIcon()
        iconThemeName = u"t"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.toolBox.addItem(self.cars_page, icon1, u"Settings")

        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.splitter.addWidget(self.menu_widget)
        self.main_widget = QWidget(self.splitter)
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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/arrow-96-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon/icon/arrow-31-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(15, 15))
        self.pushButton_8.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.search_frame = QFrame(self.search_widget)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(300, 30))
        self.search_frame.setMaximumSize(QSize(300, 30))
        self.search_frame.setFont(font1)
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

        self.pushButton = QPushButton(self.search_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout_4.addWidget(self.search_widget, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.main_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(800, 600))
        self.tabWidget.setFont(font1)
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
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.gridLayout_5 = QGridLayout(self.home)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.splitter_17 = QSplitter(self.frame)
        self.splitter_17.setObjectName(u"splitter_17")
        self.splitter_17.setOrientation(Qt.Vertical)
        self.splitter_16 = QSplitter(self.splitter_17)
        self.splitter_16.setObjectName(u"splitter_16")
        self.splitter_16.setOrientation(Qt.Horizontal)
        self.splitter_14 = QSplitter(self.splitter_16)
        self.splitter_14.setObjectName(u"splitter_14")
        self.splitter_14.setOrientation(Qt.Vertical)
        self.groupBox_3 = QGroupBox(self.splitter_14)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setMaximumSize(QSize(500, 60))
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter_15 = QSplitter(self.groupBox_3)
        self.splitter_15.setObjectName(u"splitter_15")
        self.splitter_15.setOrientation(Qt.Horizontal)
        self.label_13 = QLabel(self.splitter_15)
        self.label_13.setObjectName(u"label_13")
        self.splitter_15.addWidget(self.label_13)
        self.lineEdit_ip_host = QLineEdit(self.splitter_15)
        self.lineEdit_ip_host.setObjectName(u"lineEdit_ip_host")
        sizePolicy1.setHeightForWidth(self.lineEdit_ip_host.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip_host.setSizePolicy(sizePolicy1)
        self.splitter_15.addWidget(self.lineEdit_ip_host)

        self.gridLayout_3.addWidget(self.splitter_15, 0, 0, 1, 1)

        self.splitter_13 = QSplitter(self.groupBox_3)
        self.splitter_13.setObjectName(u"splitter_13")
        self.splitter_13.setOrientation(Qt.Horizontal)
        self.label_23 = QLabel(self.splitter_13)
        self.label_23.setObjectName(u"label_23")
        self.splitter_13.addWidget(self.label_23)
        self.lineEdit_mac_host = QLineEdit(self.splitter_13)
        self.lineEdit_mac_host.setObjectName(u"lineEdit_mac_host")
        sizePolicy1.setHeightForWidth(self.lineEdit_mac_host.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac_host.setSizePolicy(sizePolicy1)
        self.lineEdit_mac_host.setMinimumSize(QSize(180, 0))
        self.splitter_13.addWidget(self.lineEdit_mac_host)

        self.gridLayout_3.addWidget(self.splitter_13, 0, 1, 1, 1)

        self.splitter_14.addWidget(self.groupBox_3)
        self.frame_5 = QFrame(self.splitter_14)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.splitter_12 = QSplitter(self.frame_5)
        self.splitter_12.setObjectName(u"splitter_12")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.splitter_12.sizePolicy().hasHeightForWidth())
        self.splitter_12.setSizePolicy(sizePolicy2)
        self.splitter_12.setOrientation(Qt.Horizontal)
        self.label_22 = QLabel(self.splitter_12)
        self.label_22.setObjectName(u"label_22")
        self.splitter_12.addWidget(self.label_22)
        self.comboBox_interface_2 = QComboBox(self.splitter_12)
        self.comboBox_interface_2.addItem("")
        self.comboBox_interface_2.addItem("")
        self.comboBox_interface_2.addItem("")
        self.comboBox_interface_2.setObjectName(u"comboBox_interface_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_interface_2.sizePolicy().hasHeightForWidth())
        self.comboBox_interface_2.setSizePolicy(sizePolicy3)
        self.splitter_12.addWidget(self.comboBox_interface_2)

        self.gridLayout_13.addWidget(self.splitter_12, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.pushButton_5, 0, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_5)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.pushButton_13, 0, 1, 1, 1)

        self.pushButton_start_cap = QPushButton(self.frame_5)
        self.pushButton_start_cap.setObjectName(u"pushButton_start_cap")
        sizePolicy4.setHeightForWidth(self.pushButton_start_cap.sizePolicy().hasHeightForWidth())
        self.pushButton_start_cap.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.pushButton_start_cap, 1, 2, 1, 1)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_13.addWidget(self.label_18, 1, 0, 1, 1)

        self.pushButton_stop_cap = QPushButton(self.frame_5)
        self.pushButton_stop_cap.setObjectName(u"pushButton_stop_cap")
        sizePolicy4.setHeightForWidth(self.pushButton_stop_cap.sizePolicy().hasHeightForWidth())
        self.pushButton_stop_cap.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.pushButton_stop_cap, 1, 1, 1, 1)

        self.splitter_14.addWidget(self.frame_5)
        self.groupBox_ip_discovered = QGroupBox(self.splitter_14)
        self.groupBox_ip_discovered.setObjectName(u"groupBox_ip_discovered")
        self.groupBox_ip_discovered.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_ip_discovered.sizePolicy().hasHeightForWidth())
        self.groupBox_ip_discovered.setSizePolicy(sizePolicy5)
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
        sizePolicy1.setHeightForWidth(self.lineEdit_mac2.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac2.setSizePolicy(sizePolicy1)
        self.splitter_5.addWidget(self.lineEdit_mac2)

        self.gridLayout_8.addWidget(self.splitter_5, 1, 1, 1, 1)

        self.splitter_2 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_12 = QLabel(self.splitter_2)
        self.label_12.setObjectName(u"label_12")
        self.splitter_2.addWidget(self.label_12)
        self.lineEdit_ip_main = QLineEdit(self.splitter_2)
        self.lineEdit_ip_main.setObjectName(u"lineEdit_ip_main")
        sizePolicy1.setHeightForWidth(self.lineEdit_ip_main.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip_main.setSizePolicy(sizePolicy1)
        self.splitter_2.addWidget(self.lineEdit_ip_main)

        self.gridLayout_8.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.splitter_4 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_4.setObjectName(u"splitter_4")
        sizePolicy.setHeightForWidth(self.splitter_4.sizePolicy().hasHeightForWidth())
        self.splitter_4.setSizePolicy(sizePolicy)
        self.splitter_4.setMinimumSize(QSize(180, 0))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label_20 = QLabel(self.splitter_4)
        self.label_20.setObjectName(u"label_20")
        self.splitter_4.addWidget(self.label_20)
        self.lineEdit_mac_main = QLineEdit(self.splitter_4)
        self.lineEdit_mac_main.setObjectName(u"lineEdit_mac_main")
        sizePolicy1.setHeightForWidth(self.lineEdit_mac_main.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac_main.setSizePolicy(sizePolicy1)
        self.splitter_4.addWidget(self.lineEdit_mac_main)

        self.gridLayout_8.addWidget(self.splitter_4, 0, 1, 1, 1)

        self.splitter_3 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_19 = QLabel(self.splitter_3)
        self.label_19.setObjectName(u"label_19")
        self.splitter_3.addWidget(self.label_19)
        self.lineEdit_ip2 = QLineEdit(self.splitter_3)
        self.lineEdit_ip2.setObjectName(u"lineEdit_ip2")
        sizePolicy1.setHeightForWidth(self.lineEdit_ip2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip2.setSizePolicy(sizePolicy1)
        self.splitter_3.addWidget(self.lineEdit_ip2)

        self.gridLayout_8.addWidget(self.splitter_3, 1, 0, 1, 1)

        self.splitter_7 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.label_25 = QLabel(self.splitter_7)
        self.label_25.setObjectName(u"label_25")
        self.splitter_7.addWidget(self.label_25)
        self.lineEdit_ip3 = QLineEdit(self.splitter_7)
        self.lineEdit_ip3.setObjectName(u"lineEdit_ip3")
        sizePolicy1.setHeightForWidth(self.lineEdit_ip3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip3.setSizePolicy(sizePolicy1)
        self.splitter_7.addWidget(self.lineEdit_ip3)

        self.gridLayout_8.addWidget(self.splitter_7, 2, 0, 1, 1)

        self.splitter_6 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_6.setObjectName(u"splitter_6")
        sizePolicy1.setHeightForWidth(self.splitter_6.sizePolicy().hasHeightForWidth())
        self.splitter_6.setSizePolicy(sizePolicy1)
        self.splitter_6.setMinimumSize(QSize(180, 0))
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.label_24 = QLabel(self.splitter_6)
        self.label_24.setObjectName(u"label_24")
        self.splitter_6.addWidget(self.label_24)
        self.lineEdit_mac3 = QLineEdit(self.splitter_6)
        self.lineEdit_mac3.setObjectName(u"lineEdit_mac3")
        sizePolicy1.setHeightForWidth(self.lineEdit_mac3.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac3.setSizePolicy(sizePolicy1)
        self.lineEdit_mac3.setMaximumSize(QSize(16777215, 23))
        self.splitter_6.addWidget(self.lineEdit_mac3)

        self.gridLayout_8.addWidget(self.splitter_6, 2, 1, 1, 1)

        self.splitter_9 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_9.setOrientation(Qt.Horizontal)
        self.label_27 = QLabel(self.splitter_9)
        self.label_27.setObjectName(u"label_27")
        self.splitter_9.addWidget(self.label_27)
        self.lineEdit_ip4 = QLineEdit(self.splitter_9)
        self.lineEdit_ip4.setObjectName(u"lineEdit_ip4")
        sizePolicy1.setHeightForWidth(self.lineEdit_ip4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip4.setSizePolicy(sizePolicy1)
        self.splitter_9.addWidget(self.lineEdit_ip4)

        self.gridLayout_8.addWidget(self.splitter_9, 3, 0, 1, 1)

        self.splitter_8 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setMinimumSize(QSize(180, 0))
        self.splitter_8.setOrientation(Qt.Horizontal)
        self.label_26 = QLabel(self.splitter_8)
        self.label_26.setObjectName(u"label_26")
        self.splitter_8.addWidget(self.label_26)
        self.lineEdit_mac4 = QLineEdit(self.splitter_8)
        self.lineEdit_mac4.setObjectName(u"lineEdit_mac4")
        sizePolicy1.setHeightForWidth(self.lineEdit_mac4.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac4.setSizePolicy(sizePolicy1)
        self.splitter_8.addWidget(self.lineEdit_mac4)

        self.gridLayout_8.addWidget(self.splitter_8, 3, 1, 1, 1)

        self.splitter_11 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_11.setObjectName(u"splitter_11")
        self.splitter_11.setMinimumSize(QSize(180, 0))
        self.splitter_11.setOrientation(Qt.Horizontal)
        self.label_29 = QLabel(self.splitter_11)
        self.label_29.setObjectName(u"label_29")
        self.splitter_11.addWidget(self.label_29)
        self.lineEdit_mac5 = QLineEdit(self.splitter_11)
        self.lineEdit_mac5.setObjectName(u"lineEdit_mac5")
        sizePolicy1.setHeightForWidth(self.lineEdit_mac5.sizePolicy().hasHeightForWidth())
        self.lineEdit_mac5.setSizePolicy(sizePolicy1)
        self.splitter_11.addWidget(self.lineEdit_mac5)

        self.gridLayout_8.addWidget(self.splitter_11, 4, 1, 1, 1)

        self.splitter_10 = QSplitter(self.groupBox_ip_discovered)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_10.setOrientation(Qt.Horizontal)
        self.label_28 = QLabel(self.splitter_10)
        self.label_28.setObjectName(u"label_28")
        self.splitter_10.addWidget(self.label_28)
        self.lineEdit_ip5 = QLineEdit(self.splitter_10)
        self.lineEdit_ip5.setObjectName(u"lineEdit_ip5")
        sizePolicy1.setHeightForWidth(self.lineEdit_ip5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip5.setSizePolicy(sizePolicy1)
        self.splitter_10.addWidget(self.lineEdit_ip5)

        self.gridLayout_8.addWidget(self.splitter_10, 4, 0, 1, 1)

        self.pushButton_details_new_window = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_details_new_window.setObjectName(u"pushButton_details_new_window")
        self.pushButton_details_new_window.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_details_new_window, 4, 3, 1, 1)

        self.pushButton_ping3 = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_ping3.setObjectName(u"pushButton_ping3")
        self.pushButton_ping3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_ping3, 2, 3, 1, 1)

        self.pushButton_ping1 = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_ping1.setObjectName(u"pushButton_ping1")
        self.pushButton_ping1.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_ping1, 0, 3, 1, 1)

        self.pushButton_ping2 = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_ping2.setObjectName(u"pushButton_ping2")
        self.pushButton_ping2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_ping2, 1, 3, 1, 1)

        self.pushButton_ping4 = QPushButton(self.groupBox_ip_discovered)
        self.pushButton_ping4.setObjectName(u"pushButton_ping4")
        self.pushButton_ping4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.pushButton_ping4, 3, 3, 1, 1)

        self.label_48 = QLabel(self.groupBox_ip_discovered)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(40, 0))
        self.label_48.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_48, 1, 2, 1, 1)

        self.label_47 = QLabel(self.groupBox_ip_discovered)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(40, 0))
        self.label_47.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_47, 0, 2, 1, 1)

        self.label_51 = QLabel(self.groupBox_ip_discovered)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(40, 0))
        self.label_51.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_51, 4, 2, 1, 1)

        self.label_50 = QLabel(self.groupBox_ip_discovered)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(40, 0))
        self.label_50.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_50, 3, 2, 1, 1)

        self.label_49 = QLabel(self.groupBox_ip_discovered)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(40, 0))
        self.label_49.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_49, 2, 2, 1, 1)

        self.splitter_14.addWidget(self.groupBox_ip_discovered)
        self.splitter_16.addWidget(self.splitter_14)
        self.frame_3 = QFrame(self.splitter_16)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_square_4 = roundProgressBar(self.frame_3)
        self.widget_square_4.setObjectName(u"widget_square_4")

        self.gridLayout_7.addWidget(self.widget_square_4, 0, 1, 1, 1)

        self.widget_square_2 = roundProgressBar(self.frame_3)
        self.widget_square_2.setObjectName(u"widget_square_2")

        self.gridLayout_7.addWidget(self.widget_square_2, 1, 1, 1, 1)

        self.widget_square_3 = roundProgressBar(self.frame_3)
        self.widget_square_3.setObjectName(u"widget_square_3")

        self.gridLayout_7.addWidget(self.widget_square_3, 1, 0, 1, 1)

        self.widget_square_1 = roundProgressBar(self.frame_3)
        self.widget_square_1.setObjectName(u"widget_square_1")

        self.gridLayout_7.addWidget(self.widget_square_1, 0, 0, 1, 1)

        self.splitter_16.addWidget(self.frame_3)
        self.splitter_17.addWidget(self.splitter_16)
        self.frame_4 = QFrame(self.splitter_17)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(100)
        sizePolicy6.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy6)
        self.tableWidget.setMinimumSize(QSize(600, 30))
        self.tableWidget.setMaximumSize(QSize(821, 16777215))
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_6.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.splitter_17.addWidget(self.frame_4)

        self.gridLayout_12.addWidget(self.splitter_17, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.home, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frame_2 = QFrame(self.tab_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 881, 631))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 381, 101))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setValue(5)

        self.horizontalLayout_3.addWidget(self.spinBox_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_16.addWidget(self.label_14)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(20)

        self.horizontalLayout_16.addWidget(self.spinBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_16, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(400, 10, 461, 161))
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 30, 81, 20))
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(149, 30, 31, 20))
        self.lineEdit_download = QLineEdit(self.groupBox_4)
        self.lineEdit_download.setObjectName(u"lineEdit_download")
        self.lineEdit_download.setGeometry(QRect(110, 30, 31, 20))
        self.lineEdit_download.setReadOnly(True)
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 60, 50, 20))
        self.lineEdit_ping = QLineEdit(self.groupBox_4)
        self.lineEdit_ping.setObjectName(u"lineEdit_ping")
        self.lineEdit_ping.setGeometry(QRect(80, 60, 41, 20))
        self.lineEdit_ping.setReadOnly(True)
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 60, 50, 20))
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 90, 51, 20))
        self.lineEdit_host = QLineEdit(self.groupBox_4)
        self.lineEdit_host.setObjectName(u"lineEdit_host")
        self.lineEdit_host.setGeometry(QRect(80, 90, 101, 20))
        self.lineEdit_host.setReadOnly(True)
        self.lineEdit_sponsor = QLineEdit(self.groupBox_4)
        self.lineEdit_sponsor.setObjectName(u"lineEdit_sponsor")
        self.lineEdit_sponsor.setGeometry(QRect(260, 60, 101, 20))
        self.lineEdit_sponsor.setReadOnly(True)
        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(200, 60, 51, 20))
        self.lineEdit_city = QLineEdit(self.groupBox_4)
        self.lineEdit_city.setObjectName(u"lineEdit_city")
        self.lineEdit_city.setGeometry(QRect(260, 90, 101, 20))
        self.lineEdit_city.setReadOnly(True)
        self.label_30 = QLabel(self.groupBox_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(200, 90, 51, 20))
        self.lineEdit_lat = QLineEdit(self.groupBox_4)
        self.lineEdit_lat.setObjectName(u"lineEdit_lat")
        self.lineEdit_lat.setGeometry(QRect(250, 120, 111, 20))
        self.lineEdit_lat.setReadOnly(True)
        self.label_31 = QLabel(self.groupBox_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(200, 120, 41, 20))
        self.label_46 = QLabel(self.groupBox_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(20, 120, 31, 20))
        self.lineEdit_lon = QLineEdit(self.groupBox_4)
        self.lineEdit_lon.setObjectName(u"lineEdit_lon")
        self.lineEdit_lon.setGeometry(QRect(70, 120, 111, 20))
        self.lineEdit_lon.setReadOnly(True)
        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(200, 30, 81, 20))
        self.lineEdit_upload = QLineEdit(self.groupBox_4)
        self.lineEdit_upload.setObjectName(u"lineEdit_upload")
        self.lineEdit_upload.setGeometry(QRect(290, 30, 31, 20))
        self.lineEdit_upload.setReadOnly(True)
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(329, 30, 31, 20))
        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(140, 210, 271, 251))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.groupBox_5 = QGroupBox(self.tab_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(270, 20, 341, 101))
        self.lineEdit_17 = QLineEdit(self.groupBox_5)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(112, 30, 111, 20))
        self.lineEdit_17.setFrame(True)
        self.lineEdit_17.setClearButtonEnabled(False)
        self.label_41 = QLabel(self.groupBox_5)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(20, 30, 81, 21))
        self.label_42 = QLabel(self.groupBox_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(20, 60, 81, 21))
        self.lineEdit_18 = QLineEdit(self.groupBox_5)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(112, 60, 111, 20))
        self.groupBox_6 = QGroupBox(self.tab_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(270, 150, 341, 171))
        self.lineEdit_19 = QLineEdit(self.groupBox_6)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(142, 30, 111, 20))
        self.label_43 = QLabel(self.groupBox_6)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(20, 30, 111, 21))
        self.label_44 = QLabel(self.groupBox_6)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(20, 60, 111, 21))
        self.lineEdit_20 = QLineEdit(self.groupBox_6)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(142, 60, 111, 20))
        self.label_45 = QLabel(self.groupBox_6)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(20, 90, 111, 21))
        self.lineEdit_21 = QLineEdit(self.groupBox_6)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(142, 90, 111, 20))
        self.pushButton_12 = QPushButton(self.groupBox_6)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(230, 130, 91, 23))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.specific_device = QWidget()
        self.specific_device.setObjectName(u"specific_device")
        self.tabWidget.addTab(self.specific_device, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
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
        self.frame_circle_2 = QFrame(self.frame_infos)
        self.frame_circle_2.setObjectName(u"frame_circle_2")
        self.frame_circle_2.setMinimumSize(QSize(250, 250))
        self.frame_circle_2.setMaximumSize(QSize(250, 250))
        self.frame_circle_2.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle_2.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_circle_2)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 50, 10, 50)
        self.label_33 = QLabel(self.frame_circle_2)
        self.label_33.setObjectName(u"label_33")
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(11)
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_circle_2)
        self.label_34.setObjectName(u"label_34")
        font3 = QFont()
        font3.setFamily(u"Roboto Thin")
        font3.setPointSize(60)
        self.label_34.setFont(font3)
        self.label_34.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_circle_2)
        self.label_35.setObjectName(u"label_35")
        font4 = QFont()
        font4.setFamily(u"Roboto")
        font4.setPointSize(8)
        self.label_35.setFont(font4)
        self.label_35.setStyleSheet(u"border: none;\n"
" color: rgb(128, 102, 168);")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_circle_2)
        self.label_36.setObjectName(u"label_36")
        font5 = QFont()
        font5.setFamily(u"Roboto")
        font5.setPointSize(10)
        self.label_36.setFont(font5)
        self.label_36.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_36)


        self.gridLayout_9.addWidget(self.frame_circle_2, 0, 1, 1, 1)

        self.frame_circle_1 = QFrame(self.frame_infos)
        self.frame_circle_1.setObjectName(u"frame_circle_1")
        self.frame_circle_1.setMinimumSize(QSize(250, 250))
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
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_5 = QLabel(self.frame_circle_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"border: none;\n"
" color: rgb(128, 102, 168);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_10 = QLabel(self.frame_circle_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_10)

        self.label_32 = QLabel(self.frame_circle_1)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font5)
        self.label_32.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_32)


        self.gridLayout_9.addWidget(self.frame_circle_1, 0, 0, 1, 1)

        self.frame_circle_3 = QFrame(self.frame_infos)
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
        self.label_37.setFont(font2)
        self.label_37.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_circle_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_circle_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font4)
        self.label_39.setStyleSheet(u"border: none;\n"
" color: rgb(128, 102, 168);")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_circle_3)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setFont(font5)
        self.label_40.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_40)


        self.gridLayout_9.addWidget(self.frame_circle_3, 0, 2, 1, 1)


        self.gridLayout_10.addWidget(self.frame_infos, 0, 0, 1, 3)

        self.circularProgressBar_Main = QFrame(self.tab)
        self.circularProgressBar_Main.setObjectName(u"circularProgressBar_Main")
        self.circularProgressBar_Main.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main.setFrameShadow(QFrame.Raised)
        self.circularProgressCPU = QFrame(self.circularProgressBar_Main)
        self.circularProgressCPU.setObjectName(u"circularProgressCPU")
        self.circularProgressCPU.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressCPU.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.400 rgba(85, 170, 255, 255), stop:0.395 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressCPU.setFrameShape(QFrame.StyledPanel)
        self.circularProgressCPU.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBar_Main)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg.setFrameShape(QFrame.StyledPanel)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.circularContainer = QFrame(self.circularProgressBar_Main)
        self.circularContainer.setObjectName(u"circularContainer")
        self.circularContainer.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer.setBaseSize(QSize(0, 0))
        self.circularContainer.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer.setFrameShape(QFrame.StyledPanel)
        self.circularContainer.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.circularContainer)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 34, 131, 131))
        self.infoLayout = QGridLayout(self.layoutWidget_2)
        self.infoLayout.setObjectName(u"infoLayout")
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName = QLabel(self.layoutWidget_2)
        self.labelAplicationName.setObjectName(u"labelAplicationName")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(10)
        self.labelAplicationName.setFont(font6)
        self.labelAplicationName.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.labelAplicationName, 0, 0, 1, 1)

        self.labelPercentageCPU = QLabel(self.layoutWidget_2)
        self.labelPercentageCPU.setObjectName(u"labelPercentageCPU")
        font7 = QFont()
        font7.setFamily(u"Roboto Thin")
        font7.setPointSize(30)
        self.labelPercentageCPU.setFont(font7)
        self.labelPercentageCPU.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelPercentageCPU.setAlignment(Qt.AlignCenter)
        self.labelPercentageCPU.setIndent(-1)

        self.infoLayout.addWidget(self.labelPercentageCPU, 1, 0, 1, 1)

        self.labelCredits = QLabel(self.layoutWidget_2)
        self.labelCredits.setObjectName(u"labelCredits")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(8)
        self.labelCredits.setFont(font8)
        self.labelCredits.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.labelCredits, 2, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgressCPU.raise_()
        self.circularContainer.raise_()

        self.gridLayout_10.addWidget(self.circularProgressBar_Main, 1, 0, 1, 1)

        self.circularProgressBar_Main_2 = QFrame(self.tab)
        self.circularProgressBar_Main_2.setObjectName(u"circularProgressBar_Main_2")
        self.circularProgressBar_Main_2.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main_2.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_2.setFrameShadow(QFrame.Raised)
        self.circularProgressGPU = QFrame(self.circularProgressBar_Main_2)
        self.circularProgressGPU.setObjectName(u"circularProgressGPU")
        self.circularProgressGPU.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressGPU.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.600 rgba(85, 255, 127, 255), stop:0.595 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressGPU.setFrameShape(QFrame.StyledPanel)
        self.circularProgressGPU.setFrameShadow(QFrame.Raised)
        self.circularBg_2 = QFrame(self.circularProgressBar_Main_2)
        self.circularBg_2.setObjectName(u"circularBg_2")
        self.circularBg_2.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_2.setFrameShape(QFrame.StyledPanel)
        self.circularBg_2.setFrameShadow(QFrame.Raised)
        self.circularContainer_2 = QFrame(self.circularProgressBar_Main_2)
        self.circularContainer_2.setObjectName(u"circularContainer_2")
        self.circularContainer_2.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer_2.setBaseSize(QSize(0, 0))
        self.circularContainer_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_2.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.circularContainer_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 40, 171, 127))
        self.infoLayout_2 = QGridLayout(self.layoutWidget_3)
        self.infoLayout_2.setObjectName(u"infoLayout_2")
        self.infoLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_2 = QLabel(self.layoutWidget_3)
        self.labelAplicationName_2.setObjectName(u"labelAplicationName_2")
        self.labelAplicationName_2.setFont(font6)
        self.labelAplicationName_2.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_2.setAlignment(Qt.AlignCenter)

        self.infoLayout_2.addWidget(self.labelAplicationName_2, 0, 0, 1, 1)

        self.labelPercentageGPU = QLabel(self.layoutWidget_3)
        self.labelPercentageGPU.setObjectName(u"labelPercentageGPU")
        self.labelPercentageGPU.setFont(font7)
        self.labelPercentageGPU.setStyleSheet(u"color: rgb(115, 255, 171); padding: 0px; background-color: none;")
        self.labelPercentageGPU.setAlignment(Qt.AlignCenter)
        self.labelPercentageGPU.setIndent(-1)

        self.infoLayout_2.addWidget(self.labelPercentageGPU, 1, 0, 1, 1)

        self.labelCredits_2 = QLabel(self.layoutWidget_3)
        self.labelCredits_2.setObjectName(u"labelCredits_2")
        self.labelCredits_2.setFont(font8)
        self.labelCredits_2.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_2.setAlignment(Qt.AlignCenter)

        self.infoLayout_2.addWidget(self.labelCredits_2, 2, 0, 1, 1)

        self.circularBg_2.raise_()
        self.circularProgressGPU.raise_()
        self.circularContainer_2.raise_()

        self.gridLayout_10.addWidget(self.circularProgressBar_Main_2, 1, 1, 1, 1)

        self.circularProgressBar_Main_3 = QFrame(self.tab)
        self.circularProgressBar_Main_3.setObjectName(u"circularProgressBar_Main_3")
        self.circularProgressBar_Main_3.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main_3.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_3.setFrameShadow(QFrame.Raised)
        self.circularProgressRAM = QFrame(self.circularProgressBar_Main_3)
        self.circularProgressRAM.setObjectName(u"circularProgressRAM")
        self.circularProgressRAM.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressRAM.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.750 rgba(255, 0, 127, 255), stop:0.745 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressRAM.setFrameShape(QFrame.StyledPanel)
        self.circularProgressRAM.setFrameShadow(QFrame.Raised)
        self.circularBg_3 = QFrame(self.circularProgressBar_Main_3)
        self.circularBg_3.setObjectName(u"circularBg_3")
        self.circularBg_3.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg_3.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_3.setFrameShape(QFrame.StyledPanel)
        self.circularBg_3.setFrameShadow(QFrame.Raised)
        self.circularContainer_3 = QFrame(self.circularProgressBar_Main_3)
        self.circularContainer_3.setObjectName(u"circularContainer_3")
        self.circularContainer_3.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer_3.setBaseSize(QSize(0, 0))
        self.circularContainer_3.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_3.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.circularContainer_3)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 40, 171, 125))
        self.infoLayout_3 = QGridLayout(self.layoutWidget_4)
        self.infoLayout_3.setObjectName(u"infoLayout_3")
        self.infoLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_3 = QLabel(self.layoutWidget_4)
        self.labelAplicationName_3.setObjectName(u"labelAplicationName_3")
        self.labelAplicationName_3.setFont(font6)
        self.labelAplicationName_3.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_3.setAlignment(Qt.AlignCenter)

        self.infoLayout_3.addWidget(self.labelAplicationName_3, 0, 0, 1, 1)

        self.labelPercentageRAM = QLabel(self.layoutWidget_4)
        self.labelPercentageRAM.setObjectName(u"labelPercentageRAM")
        self.labelPercentageRAM.setFont(font7)
        self.labelPercentageRAM.setStyleSheet(u"color: rgb(255, 44, 174); padding: 0px; background-color: none;")
        self.labelPercentageRAM.setAlignment(Qt.AlignCenter)
        self.labelPercentageRAM.setIndent(-1)

        self.infoLayout_3.addWidget(self.labelPercentageRAM, 1, 0, 1, 1)

        self.labelCredits_3 = QLabel(self.layoutWidget_4)
        self.labelCredits_3.setObjectName(u"labelCredits_3")
        self.labelCredits_3.setFont(font8)
        self.labelCredits_3.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_3.setAlignment(Qt.AlignCenter)

        self.infoLayout_3.addWidget(self.labelCredits_3, 2, 0, 1, 1)

        self.circularBg_3.raise_()
        self.circularProgressRAM.raise_()
        self.circularContainer_3.raise_()

        self.gridLayout_10.addWidget(self.circularProgressBar_Main_3, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.splitter.addWidget(self.main_widget)

        self.gridLayout_11.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setAutoFillBackground(True)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.pushButton_8.toggled.connect(self.menu_widget.setHidden)

        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(10)
        self.tabWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.pushButton_8.setText("")
#if QT_CONFIG(tooltip)
        self.label_52.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Online Devices On Network", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Network", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Host IP", None))
        self.lineEdit_ip_host.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Host Mac Address", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Interface", None))
        self.comboBox_interface_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Local Area Connection", None))
        self.comboBox_interface_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Wifi", None))
        self.comboBox_interface_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Ethernet", None))

        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Scan Network", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Test Speed", None))
        self.pushButton_start_cap.setText(QCoreApplication.translate("MainWindow", u"Start Capture", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Main Device", None))
        self.pushButton_stop_cap.setText(QCoreApplication.translate("MainWindow", u"Stop Capture", None))
        self.groupBox_ip_discovered.setTitle(QCoreApplication.translate("MainWindow", u"Ip Discovered", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Mac Address", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ip 1", None))
        self.lineEdit_ip_main.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Mac Address", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Ip 2", None))
        self.lineEdit_ip2.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Ip 3", None))
        self.lineEdit_ip3.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Mac Address", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Ip 4", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Mac Address", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Mac Address", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Ip 5", None))
        self.pushButton_details_new_window.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.pushButton_ping3.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.pushButton_ping1.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.pushButton_ping2.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.pushButton_ping4.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"--", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Time Stamp", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Source", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Destination", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Protocol", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Info", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), QCoreApplication.translate("MainWindow", u"home", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Network", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Interface", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Local Area Connection", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Timeout", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"By Second", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Packet Count", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Internet Speed", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Download Speed", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MB/S", None))
        self.lineEdit_download.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ms", None))
        self.lineEdit_ping.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.lineEdit_host.setText("")
        self.lineEdit_sponsor.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Sponsor", None))
        self.lineEdit_city.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.lineEdit_lat.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Lat", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Lon", None))
        self.lineEdit_lon.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Upload Speed", None))
        self.lineEdit_upload.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MB/S", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Network Configuration", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"User Info", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_18.setText(QCoreApplication.translate("MainWindow", u"********", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Old Password", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Password Confiramtion", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Account Configuration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Database Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.specific_device), QCoreApplication.translate("MainWindow", u"Device Details", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"System Functions", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"GPU USAGE", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"40%", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"RTX 2080 Ti", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Temp: 55C\u00ba", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU USAGE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Intel | i9 9900k | 8 Cores", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"25%", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Temp: 45C\u00ba", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"RAM USAGE", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"8GB", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Total: 64gb", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Temp: 25C\u00ba", None))
        self.labelAplicationName.setText(QCoreApplication.translate("MainWindow", u"<strong>CPU</strong> USAGE", None))
        self.labelPercentageCPU.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">60</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))
        self.labelCredits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>TEMP: <span style=\" color:#ffffff;\">40\u00ba</span></p></body></html>", None))
        self.labelAplicationName_2.setText(QCoreApplication.translate("MainWindow", u"<strong>GPU</strong> USAGE", None))
        self.labelPercentageGPU.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">40</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))
        self.labelCredits_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>TEMP: <span style=\" color:#ffffff;\">60\u00ba</span></p></body></html>", None))
        self.labelAplicationName_3.setText(QCoreApplication.translate("MainWindow", u"<strong>RAM</strong> USAGE", None))
        self.labelPercentageRAM.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">25</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))
        self.labelCredits_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>TEMP: <span style=\" color:#ffffff;\">20\u00ba</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Meters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Devices", None))
    # retranslateUi

