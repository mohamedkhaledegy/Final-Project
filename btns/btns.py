from PySide2 import QtWidgets as qtw

def set_btns(self):
    ### Tab Widget
    ## Home
    # Network
    self.section_network = self.findChild(qtw.QGroupBox,"groupBox_network")
    self.lineEdit_ip_host = self.findChild(qtw.QLineEdit,"lineEdit_ip_host")
    self.lineEdit_mac_host = self.findChild(qtw.QLineEdit,"lineEdit_mac_host")

    # interface
    self.btn_stop_cap = self.findChild(qtw.QPushButton,"pushButton_stop_cap")
    self.btn_start_cap = self.findChild(qtw.QPushButton,"pushButton_start_cap")
    self.btn_ping1 = self.findChild(qtw.QPushButton,"pushButton_ping1")
    self.btn_ping2 = self.findChild(qtw.QPushButton,"pushButton_ping2")
    self.btn_ping3 = self.findChild(qtw.QPushButton,"pushButton_ping3")
    self.btn_ping4 = self.findChild(qtw.QPushButton,"pushButton_ping4")
    self.btn_ping5 = self.findChild(qtw.QPushButton,"pushButton_ping5")
    self.btn_dtls = self.findChild(qtw.QPushButton,"pushButton_details_new_window")

    # IP Discovered
    self.section_ip_discovered = self.findChild(qtw.QGroupBox,"groupBox_ip_discovered")

    ## Network Config
    # Network

    # Internet Speed
    self.lineEdit_city = self.findChild(qtw.QLineEdit,"lineEdit_city") #
    self.lineEdit_download = self.findChild(qtw.QLineEdit,"lineEdit_download") #
    self.lineEdit_upload = self.findChild(qtw.QLineEdit,"lineEdit_upload") #
    self.lineEdit_host = self.findChild(qtw.QLineEdit,"lineEdit_host") #
    self.lineEdit_ping = self.findChild(qtw.QLineEdit,"lineEdit_ping") #
    self.lineEdit_lat = self.findChild(qtw.QLineEdit,"lineEdit_lat") #
    self.lineEdit_lon = self.findChild(qtw.QLineEdit,"lineEdit_lon") #
    self.lineEdit_sponsor = self.findChild(qtw.QLineEdit,"lineEdit_sponsor") #
    ## Side Bar Buttons
    self.btn_thread = self.findChild(qtw.QPushButton,"pushButton_5")#
    self.btn_resault = self.findChild(qtw.QPushButton,"pushButton_14")#
    self.btn_network_config = self.findChild(qtw.QPushButton,"pushButton_network_config")#
    self.btn_home = self.findChild(qtw.QPushButton,"pushButton_home")#
    self.btn_meters = self.findChild(qtw.QPushButton,"pushButton_meters")#
    self.btn_database_settings = self.findChild(qtw.QPushButton,"pushButton_database_settings")#
    self.btn_network_config = self.findChild(qtw.QPushButton,"pushButton_network_config")#
    self.btn_system_functions = self.findChild(qtw.QPushButton,"pushButton_system_functions")#
    self.btn_devices = self.findChild(qtw.QPushButton,"pushButton_devices")#
    self.btn_acc_config = self.findChild(qtw.QPushButton,"pushButton_acc_config")#
    ## Table Widget
    #self.table_cap = self.findChild(qtw.QTableWidget,"tableWidget_cap")

def setup_btn(self):
    ###### System Functions Tab
    # Ping
    #self.findChild(qtw.QPushButton,"pushButton_save_ping").pressed.connect(self.thread_ping_save_in_db)
    #self.findChild(qtw.QPushButton,"pushButton_checker_ping").pressed.connect(self.thread_ping_check_auto_save)
    self.findChild(qtw.QPushButton,"pushButton_checker_ping_3").pressed.connect(self.thread_ping_check_auto_save)
    self.findChild(qtw.QPushButton,"pushButton_ping_all").pressed.connect(self.thread_ping_all)
    self.findChild(qtw.QPushButton,"pushButton_ping_all_stop").pressed.connect(self.stop_ping)
    #### Bandwidth
    self.findChild(qtw.QPushButton,"pushButton_start_bandwidth").pressed.connect(self.bandwidth_sample_worker)
    self.findChild(qtw.QPushButton,"pushButton_bandwidth_services").pressed.connect(self.bandwidth_services_worker)
    #### Site Block Config
    self.findChild(qtw.QPushButton,"pushButton_site_block").pressed.connect(self.block_site_worker)
    #### DB
    self.findChild(qtw.QPushButton,"pushButton_refresh_db").pressed.connect(self.set_data_base)
    self.findChild(qtw.QPushButton,"pushButton_refresh_db_2").pressed.connect(self.set_data_base)
    self.findChild(qtw.QPushButton,"pushButton_get_db_tables").pressed.connect(self.set_table_widget_from_db)
    ## New Window
    self.btn_dtls.pressed.connect(lambda : self.open_new_win())
    ## Scan Network For Ip & Progress Circle
    self.btn_thread.pressed.connect(self.threadRunner)
    self.btn_thread.pressed.connect(self.threadRunner2)
    ## Test Speed
    self.pushButton_test_speed.pressed.connect(lambda : self.threadRunner3())
    self.pushButton_test_speed.pressed.connect(lambda : self.threadRunner4())
    ## Ping
    try:
        self.btn_ping1.pressed.connect(lambda : self.which_ip_to_ping(num_ip=1))
        self.btn_ping2.pressed.connect(lambda : self.which_ip_to_ping(num_ip=2))
        self.btn_ping3.pressed.connect(lambda : self.which_ip_to_ping(num_ip=3))
        self.btn_ping4.pressed.connect(lambda : self.which_ip_to_ping(num_ip=4))
        self.btn_ping5.pressed.connect(lambda : self.which_ip_to_ping(num_ip=5))
    except:
        pass
    ## Capture Start & Stop
    #self.pushButton_capture.clicked.connect(self.threadsniffing1)
    self.btn_start_cap.clicked.connect(self.continue_snifer)
    self.btn_stop_cap.clicked.connect(self.stop_snifer)
    #### Side Bar Buttons ####
    try:
        self.btn_network_config.clicked.connect(lambda : self.main_widget.setCurrentIndex(1))
        self.btn_acc_config.clicked.connect(lambda : self.main_widget.setCurrentIndex(2))
        self.btn_database_settings.clicked.connect(lambda : self.main_widget.setCurrentIndex(3))
        self.btn_meters.clicked.connect(lambda : self.main_widget.setCurrentIndex(4))
        self.btn_devices.clicked.connect(lambda : self.main_widget.setCurrentIndex(5))
        self.btn_home.clicked.connect(lambda : self.main_widget.setCurrentIndex(0))
        self.main_widget.setCurrentIndex(0)
    except Exception as err:
        print("Failed to Set SideBar Buttons Signals :",err)
        pass
