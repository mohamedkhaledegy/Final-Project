import sys
import os
import time
import datetime
import timeit
import subprocess
# import numpy as np

# from PyQt5.QtDesigner import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5 import QtWidgets as qtw
# from PyQt5.QtQml import QQmlApplicationEngine
# from PyQt5.uic import loadUiType

# Import As Pyside2
from PySide2 import QtUiTools
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import QtWidgets as qtw
from PySide2.QtUiTools import loadUiType

# Import Network Modules
from scapy import all as sc
# import pyshark

# from front import resource_rc

################ Import Custom ################
# from meters import AnalogGaugeWidget
from threads_custom.scan_network import scan_network

## Import Buttons Config & Signal
from btns.circle_btns import *
from btns.btns import *

## Import Threads Functions
from threads_custom.works import Worker

## Test Speed Internet
from threads_custom.test_speed import *

## Bandwidth Functions
from threads_custom.bandwidth_usage_worker import *
from threads_custom.multi_usage_worker import *

## Import Database Models
from db.my_models import Device,PingInfo
## Import Database Functions
#from db.retrieve_from_db import get_all_dev
from db_to_qt import *
from db.db_config import db as my_db

from matplot_functions.set_sample import *

### Import Stylesheet Functions
#from qt_material import apply_stylesheet
import qdarkstyle

ui_main,_ = loadUiType('front/main_window2.ui')
ui_login,_ot = loadUiType('front/second_window.ui')
is_program_running = True
logo_url = "front/logo_small.png"
class Login(QMainWindow , ui_login):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_open = self.findChild(qtw.QPushButton,"pushButton")
        self.btn_open.clicked.connect(self.log_in_system)
        self.setWindowIcon(QIcon(logo_url))
        self.setWindowTitle("MTI Network")
        pixmap = QPixmap(f'{logo_url}')
        self.label_logo.setPixmap(pixmap)
        self.label_logo.resize(pixmap.width(), pixmap.height())
        
    def log_in_system(self):
        valid_auth = self.authenticate_user()
        if valid_auth == True:
            self.window2 = Main()
            self.close()
            self.window2.show()
        else:
            print("Wrong Password")
    def authenticate_user(self):
        self.user = self.findChild(qtw.QLineEdit,"lineEdit_user_log").text()
        self.password = self.findChild(qtw.QLineEdit,"lineEdit_password_log").text()
        print(self.user)
        valid = False
        user_name = "Mti"
        user_pass = "network2023"
        if self.user == user_name and self.password == user_pass:
            valid = True
        else:
            s = "Error In Username Or Password"
            print(s)
            print("Mo")
            dlg = QMessageBox()
            dlg.setText(s)
            dlg.setIcon(QMessageBox.Warning)
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setWindowTitle(s)
            button = dlg.exec_()
        return valid

class Main(QMainWindow,ui_main):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.auto_run()
        #self.threadsniffing()
        

    def auto_run(self):
        print("auto Run Enabled")
        self.set_vars()
        try:
            #print("Start To Connect Database ..")
            self.db.connect()
            #print("Connected To DB")
            #print("Closing Database ..")
            self.db.close()
            #print("Closed Connection To DB")
            print("Database Connected Success")
        except:
            print("Error To Connect Database")
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        #print("Maximum Threads : %d" % self.threadpool.maxThreadCount())
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        ## GUI Functions ##
        set_btns(self)
        set_circle_design(self)
        reset_circle_val(self)
        setup_btn(self)
        self.set_table_packet()
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        ## DataBase Functions ##
        self.set_data_base()
        #self.message_error(s="Scan Network Please")
        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        ## Custom Functions ##
        # networks_cards = sc.get_if_list()
        # all_network_cards = sc.conf.ifaces
        # ip = sc.get_if_addr(sc.conf.iface)
        # print("IPPP", ip)
        # print("IFACES", all_network_cards)
        # for n in all_network_cards.items():
        #     print(n)
        #print(all_network_cards2)
        ## Thread For Scan Network For Ip & Mac Address .
        #self.threadRunner2()Realtek PCIe GBE Family Controller
        #self.threadRunner()
        ## Thread For Test Speed Internet and get Donwload , Upload Sppeed In MB/S , and other info .
        #self.threadRunner3()
        #self.threadRunner4()
        #self.set_matplot()

    def open_new_win(self):
        print("Opened")
        self.win = Login()
        self.close()
        self.win.show()
    
    def set_vars(self):
        ## For DB
        self.db = my_db
        self.all_devs = None
        ## For Sniff And Packet Show To Gui
        self.counter_pkt = 0
        self.packet_lista = []
        self.packet_dict = {}
        ## For Block Sites
        self.ip_blocked = {}
        ## Ping Vars
        self.error_message = None
        ## Breaks
        self.LOOPPINGER = True
        self.LOOPTEST = True
        self.LOOPSCAN = True
        self.LOOPBNDWDTH = True
        self.LOOPSRVS= True
        self.SNF = True
        self.pkt_num = 0
        self.threadpool = QThreadPool()
        #self.layout = qtw.QHBoxLayout()
        self.main_widget = self.findChild(qtw.QTabWidget,"tabWidget")
        #print(dir(self.main_widget))
        ## For Icon
        self.setWindowIcon(QIcon(logo_url))
        self.setWindowTitle("MTI Network")

    def set_data_base(self):
        """
            Connect With Data Base And Config It,
            Get All quert and set it to variable
            Device = devs
            PingInfo = all_pings
        """
        config_data_base(self)
        #all_devs = collect_database_info()

    def config_database_finish(self):
        print("Data Collected From Database Finished")
        from db_to_qt import devss
        from db_to_qt import pingss
        #### Set To Gui Results Of Saved Records
        try:
            self.lineEdit_database_name.setText(str(db_file_name))
            self.lineEdit_count_ping.setText(str(len(pingss)))
            self.lineEdit_count_ping_3.setText(str(len(pingss)))
            self.lineEdit_count_ip.setText(str(len(devss)))
            self.lineEdit_count_device.setText(str(len(devss)))
            print(len(devss))
            print(len(pingss))
        except:
            pass

    def set_matplot(self):
        self.grafica = Canvas_grafica()
        self.grafica1 = Canvas_grafica2()
        self.grafica2 = Canvas_grafica3()
        self.grafica3 = Canvas_grafica4()
        self.grafica_uno.addWidget(self.grafica)
        self.grafica_dos.addWidget(self.grafica1)
        self.grafica_tres.addWidget(self.grafica2)
        self.grafica_cuatro.addWidget(self.grafica3)

    def set_table_packet(self):
        pos = self.tableWidget_cap.verticalScrollBar().value()
        #print(len(self.packet_lista))
        #self.tableWidget_cap.setRowCount(1)
        table = QTableWidget()
        #qtw.QApplication.processEvents()
        self.tableWidget_cap.verticalScrollBar().setValue(pos)
        self.tableWidget_cap.horizontalHeader().setStretchLastSection(True)

    def insert_to_table(self):
        row_packets = [{"no":"1","Time Stamp":"03:22"},{"no":"2","Time Stamp":"03:25"}]
        #### 
        for num_row, row_pkt in enumerate(row_packets):
            print(num_row)
            print(row_pkt)
            item_no = qtw.QTableWidgetItem(row_pkt['no'])
            item_time = qtw.QTableWidgetItem(row_pkt['Time Stamp'])
            ## setItem(row,column,str(item))
            #self.tableWidget_cap.setItem(int,int,item)
            self.tableWidget_cap.setItem(num_row,0,item_no)
            self.tableWidget_cap.setItem(num_row,1,item_time)

    ########################## Start ##########################
    ###########     General methods for Network     ###########
    ###########################################################
    def ping_ip(self,ip_to_ping):
        """
            Function To Ping Ip In *args and return full response after ping with 3 packet as default send
        """
        command = ['ping','-n','1',ip_to_ping]
        return subprocess.getoutput(command)

    ## Functions For Buttons
    def which_ip_to_ping(self,num_ip):
        """
            Function Set For 5 Buttons In Main Window To Ping And Colored results
        """
        ip_to_ping = self.findChild(qtw.QLineEdit,f"lineEdit_ip{str(num_ip)}").text()        
        mac_addr = self.findChild(qtw.QLineEdit,f"lineEdit_mac{str(num_ip)}").text()
        ip_ping_response = {
            'IP':ip_to_ping,
            'Mac':mac_addr,
            'Checked':False,
            'Response':False,
            'TTL':None,
            'ResTime':None,
        }
        try:
            ping_response = self.ping_ip(ip_to_ping)
            label_to_color = self.findChild(qtw.QLabel,f"label_ping_status_ip{num_ip}")
            if ip_to_ping == "" :
                label_to_color.setStyleSheet("background-color:slategray; border-radius:10px")
                #label_to_color.setStyleSheet(u"background-color: rgb(0, 0, 0);")
            else:
                if "Reply from" in ping_response and \
                    not "Destination host unreachable." in ping_response:
                    ### Set Label For Succes Ping
                    ## Color (In Stylesheet)
                    label_to_color.setStyleSheet("background-color:rgb(0,250,0); border-radius:10px")
                    ## Text (In setText)
                    label_to_color.setText("Success")
                    ## Find Results In Respons String In Terminal
                    ttl_index = ping_response.find("TTL=")
                    ttl = ping_response[ttl_index+4:ttl_index+7].strip()
                    time_index = ping_response.find("time=")
                    time_index_end = ping_response.find("ms TTL")
                    time_ping = ping_response[time_index+5:time_index_end]
                    ## Set Results To variable ip_ping_response type(dict)
                    ip_ping_response['Checked'] = True
                    ip_ping_response['Response'] = True
                    ip_ping_response['TTL'] = ttl
                    if "time<1" in time_ping:
                        time_ping = "0"
                    ip_ping_response['ResTime'] = time_ping
                else:
                    ip_ping_response['Checked'] = True
                    ip_ping_response['Response'] = False
                    label_to_color.setStyleSheet(u"background-color: rgb(170, 0, 0); border-radius:10px")
                    label_to_color.setText("Failed")
        except Exception as err:
            print("Failed To Ping" , err)
        finally:
            print(ip_ping_response)
            print("Ping Done")
            return ip_ping_response

    ########################## Start ##########################
    ### Methods For (Thread , Worker ) Instance and Objects ###
    ###########################################################
        # in this function we create our thread and run it
    def threadRunner(self):
        self.frame_1_circle_progres.show()
        self.frame_1_circle_progres.show()
        worker_1 = Worker(self.first_thread, num=1)# create our thread and give it a function as argument with its args
        worker_1.signals.result.connect(self.first_thread_result) # connect result signal of our thread to thread_result
        worker_1.signals.finished.connect(self.first_thread_finished) # connect finish signal of our thread to thread_complete
        self.threadpool.start(worker_1) # start thread

    def first_thread(self, num):
        print("first_thread")
        # some long processing
        self.btn_thread.setText("Processing...")
        #ip_scanned = scan_network("192.168.1.1/24")
        #print(ip_scanned)
        ## Time Top Process
        time_choosed = 20
        ## resault in %100
        stop_point_of_100 = time_choosed/100
        ## convert to msleep (sleep 1 second = mlsleep 1000 mlsecond) 
        stop_point_of_100 = stop_point_of_100 * 1000
        print(stop_point_of_100)
        #QThread.sleep(2)
        num = 0
        
        for i in range(101):
            #get_v = self.frame_1_circle_progres.rpb_getValue()
            if self.LOOPSCAN == True and i < 100:
                print(i)
                # if self.lineEdit_ip_host.text() != "":
                #     self.frame_2_circle_progres.rpb_setValue(100)
                #     break
                num += 1
                #val_now = self.frame_2_cricle_progres.rpb_getValue()
                #print(val_now)
                
                self.frame_1_circle_progres.rpb_setValue(i)
                QThread.msleep(stop_point_of_100)
            if self.LOOPSCAN == False:
                print("Real Value Now",i)
                for n in range(i,101):
                    self.frame_1_circle_progres.rpb_setValue(n)
                    QThread.msleep(10)
                break
        return num

    def first_thread_result(self):
        #self.frame_2_circle_progres.rpb_setValue(100)
        print("First Thread Result")
        self.btn_thread.setText("Finished")
        QThread.sleep(1)

    def first_thread_finished(self):
        print("First Thread Scan finished")
        self.btn_thread.setText("ReScan Network")
        self.LOOPSCAN = True
        QThread.msleep(10)
        self.frame_1_circle_progres.hide()

    def second_thrd_scan_network(self):
        global ip_scanned
        #self.btn_thread.setText("Processing...")
        print("Start Scan")
        global ip_router , ip_master
        ip_router = self.lineEdit_ip_router.text()
        ip_master = self.lineEdit_ip_master.text()
        if ip_master != "":
            pass
        else:
            ip_master = None
        if ip_router != "":
            ip_scanned = scan_network(f"{str(ip_router)}/24")
        else:
            ip_router = None
            ip_scanned = scan_network("192.168.1.1/24")
        #print("Finish Scan")
        #print(ip_scanned)
        return ip_scanned

    def third_thrd_speed_test(self):
        self.frame_3_circle_progres.show()
        self.pushButton_test_speed.setText("Processing...")
        print("Start Test Speed")
        global speed_test_dict
        st = speedtest.Speedtest()
        
        st.get_best_server()
        download_speed = return_bytes_by_mb(st.download())
        self.LOOPTESTDN = False
        uploaad_speed = return_bytes_by_mb(st.upload())
        self.LOOPTESTUP = False

        speed_test_dict = st.results.dict()
        downloaded = return_bytes_by_mb(speed_test_dict['bytes_received'])
        print(speed_test_dict)
        print(downloaded)
        #print("Your Download speed is", download_speed, "MB")
        print("Finished Test Speed Internet")
        #print("End Result First Thread")
        self.LOOPTEST = False
        return speed_test_dict

    def fourth_thrd_speed_test(self):
        print("Start Fourth Thread Speed Test Progress")
        time_choosed = 25
        ## resault in %100
        stop_point_of_100 = time_choosed/100
        ## convert to msleep (sleep 1 second = mlsleep 1000 mlsecond)
        stop_point_of_100 = stop_point_of_100 * 1000
        print(stop_point_of_100)
        #QThread.sleep(2)
        for i in range(101):
            if self.LOOPTEST == True:
                print(i)
                #self.frame_1_circle_progres.rpb_setValue(i)
                self.frame_3_circle_progres.rpb_setValue(i)
                QThread.msleep(stop_point_of_100)
            else:
                self.frame_3_circle_progres.rpb_setValue(i)
                QThread.msleep(10)

    def second_thread_scan_result(self):
        """
            Scan Network Results
            Loop on IP Scanned for Collect Info Stored In Dictionary (global var) > Updated in method : self.thread_scan_network
        """
        self.LOOPSCAN = False
        addrs = psutil.net_if_addrs()
        print(addrs.keys())
        self.section_network.setEnabled(True)
        self.section_ip_discovered.setEnabled(True)
        for n,info in ip_scanned.items():
            print(info)
            if info['IP'] == ip_master:
                info['master'] = True
            else:
                info['master'] = False
            if info['IP'] == ip_router:
                info['host'] = True
            else:
                info['host'] = False
        print(len(ip_scanned))
        for row_num , row_info in ip_scanned.items():
            print(row_num)
            print(row_info)
            ip = row_info['IP']
            mac = row_info['Mac']
            if row_info['host'] == True:
                label_ip = self.findChild(qtw.QLineEdit,"lineEdit_ip_host")
                label_mac = self.findChild(qtw.QLineEdit,"lineEdit_mac_host")
                label_ip.setText(str(ip))
                label_mac.setText(str(mac))
            check_ip = self.findChild(qtw.QCheckBox,f'checkBox_ping_{str(row_num)}')
            label_ip = self.findChild(qtw.QLineEdit,f"lineEdit_ip{str(row_num)}")
            label_mac = self.findChild(qtw.QLineEdit,f"lineEdit_mac{str(row_num)}")
            #print(dir(self.label_ip))
            label_ip.setText(str(ip))
            label_mac.setText(str(mac))
            check_ip.setChecked(True)

    def third_thrd_speed_test_result(self):
        print("Third Thread Scan Result")
        self.pushButton_test_speed.setText("Test again")

    def fourth_thrd_speed_test_result(self):
        print("Fourth Thread Speed Test Progress Result")
        self.LOOPTEST = True
        self.frame_3_circle_progres.hide()

    def second_thread_scan_finished(self):
        print("Second Thread Scan finished")

    def third_thrd_speed_test_finished(self):
        print("Third Thread Speed Test Finished")
        down_speed_mb = return_bytes_by_mb(speed_test_dict['download'])
        up_speed_mb = return_bytes_by_mb(speed_test_dict['upload'])
        time_stamp = speed_test_dict['timestamp']
        all_uploaded = return_bytes_by_mb(speed_test_dict['bytes_sent'])
        all_downloaded = return_bytes_by_mb(speed_test_dict['bytes_received'])
        try:
            time_stamp = round(time_stamp,2)
            print(time_stamp)
        except:
            pass
        # Convert To Limit 2 After ,
        dwn_mb = round(down_speed_mb,2)
        up_mb = round(up_speed_mb,2)
        all_up = str(round(all_uploaded,2)) + " Mb Uploaded"
        all_down = str(round(all_downloaded,2)) + " Mb Downloaded"
        ping = round(speed_test_dict['ping'],2)
        print(time_stamp)
        print(all_up)
        print(all_down)
        # Set To Gui
        self.lineEdit_download.setText(str(dwn_mb))
        self.label_download_meter.setText(str(dwn_mb))
        self.lineEdit_upload.setText(str(up_mb))
        self.label_upload_meter.setText(str(up_mb))
        self.lineEdit_ping.setText(str(ping))
        self.label_meter_ping.setText(str(ping))
        self.lineEdit_country.setText(str(speed_test_dict['server']['country']))
        self.lineEdit_host.setText(str(speed_test_dict['server']['host']))
        self.lineEdit_sponsor_server.setText(str(speed_test_dict['server']['sponsor']))
        self.lineEdit_area.setText(str(speed_test_dict['server']['name']))
        self.lineEdit_city.setText(str(speed_test_dict['client']['country']))
        self.lineEdit_sponsor.setText(str(speed_test_dict['client']['isp']))
        self.lineEdit_lon.setText(str(speed_test_dict['client']['lon']))
        self.lineEdit_lat.setText(str(speed_test_dict['client']['lat']))
        self.lineEdit_global_ip.setText(str(speed_test_dict['client']['ip']))
        self.label_all_up.setText(str(all_up))
        self.label_all_down.setText(str(all_down))
        self.label_test_time.setText(str(time_stamp))
        self.label_meter_ip.setText(str(speed_test_dict['client']['ip']))

    def fourth_thrd_speed_test_finished(self):
        print("Fourth Thread Speed Test Finished")

    def threadRunner4(self):
        worker_1 = Worker(self.fourth_thrd_speed_test)# create our thread and give it a function as argument with its args
        worker_1.signals.result.connect(self.fourth_thrd_speed_test_result) # connect result signal of our thread to thread_result
        worker_1.signals.finished.connect(self.fourth_thrd_speed_test_finished) # connect finish signal of our thread to thread_complete
        self.threadpool.start(worker_1) # start thread

    def threadRunner3(self):
        worker_1 = Worker(self.third_thrd_speed_test)# create our thread and give it a function as argument with its args
        worker_1.signals.result.connect(self.third_thrd_speed_test_result) # connect result signal of our thread to thread_result
        worker_1.signals.finished.connect(self.third_thrd_speed_test_finished) # connect finish signal of our thread to thread_complete
        self.threadpool.start(worker_1) # start thread

    def threadRunner2(self):
        worker_2 = Worker(self.second_thrd_scan_network) # create our thread and give it a function as argument with its args
        worker_2.signals.result.connect(self.second_thread_scan_result) # connect result signal of our thread to thread_result
        worker_2.signals.finished.connect(self.second_thread_scan_finished) # connect finish signal of our thread to thread_complete
        self.threadpool.start(worker_2)

    def threadsniffing(self):
        worker = Worker(self.sniffer_start)
        worker.signals.result.connect(self.sniffer_results)
        worker.signals.finished.connect(self.sniffer_finished)
        self.threadpool.start(worker)

    ###### Network Functions Custom for re view results catched
    def get_serv(self,src_port,dst_port):
        try:
            service = socket.getservbyport(src_port)
        except:
            service = socket.getservbyport(dst_port)
            return service

    def get_host_name(self,ip):
        if "192.168" in ip:
            name = "Local Device"
        else:
            try:
                name = socket.getfqdn(ip)
            except:
                name = None
        return name

    def analyzer_sniff(self,pkt):
        ## packet dictionary
        # num
        # time
        # ip-src
        # ip-dst
        # mac-src
        # mac-dst
        # port-src
        # port-dst
        is_blocked = False
        try:
            ## Full Date
            ## strftime("%H:%M:%S")
            dt_object = datetime.fromtimestamp(pkt.time)
            src = pkt.src
            dst = pkt.dst
            ttl_pkt = pkt.ttl
            len_pkt = pkt.len
            try:
                ######
                src_ip = pkt[IP].src
                dst_ip = pkt[IP].dst
                ########################
                mac_src = pkt.src
                mac_dst = pkt.dst
            except:
                src_ip = None
                dst_ip = None
                pass
            ## Get Host NAme
            host_name = None
            host_name1 = None
            host_name2 = None
            try:
                if src_ip != None and dst_ip != None:
                    host_name1 = self.get_host_name(ip=src_ip)
                    host_name2 = self.get_host_name(ip=dst_ip)
            except Exception as err:
                print(err)
                pass
            try:
                if host_name1 != None:
                    if host_name1 != "Local Device":
                        host_name = host_name1
                        if host_name1 == self.ip_blocked[1]['host'] or self.ip_blocked[1]['name'] in host_name1 :
                            is_blocked = True
                            print("Blocked")
                if host_name2 != None:
                    if host_name2 != "Local Device":
                        host_name = host_name2
                        if host_name2 == self.ip_blocked[1]['host'] or self.ip_blocked[1]['name'] in host_name2 :
                            is_blocked = True
                            print("Blocked")
            except:
                pass
            self.pkt_num += 1
            pckt_dict = {
                'num':self.pkt_num,
                'time':dt_object,
                'ip-src':src,
                'ip-dst':dst,
                "ttl-pkt":ttl_pkt,
                "len-pkt":len_pkt,
                'port-src':None,
                'port-dst':None,
                'host-name':host_name,
                'service':None,
                'blocked': is_blocked,
            }
            #print(pckt_dict)
            if pkt.haslayer(ICMP):
                print("----------------------------------------")
                #print("ICMP PACKET..." , "src-ip",src_ip,"dst-ip",dst_ip)
                #print("SRC-MAC : " + mac_src)
                #print("DST-MAC : " + mac_dst)
                if pkt.haslayer(Raw):
                    data = pkt[Raw].load
                ####
                pckt_dict = {
                    'num':self.pkt_num,
                    'layer':"ICMP",
                    'time':dt_object,
                    'ip-src':pkt['IP'].src,
                    'ip-dst':pkt['IP'].dst,
                    "ttl-pkt":ttl_pkt,
                    "len-pkt":len_pkt,
                    'port-src':None,
                    'port-dst':None,
                    'host-name':host_name,
                    'service':None,
                    'blocked': is_blocked,
                    }
                #self.packet_lista.append(pckt_dict['num'])
                #self.set_pkt_on_table(pckt_dict)
            else:
                try:
                    src_port = pkt.sport
                    dst_port = pkt.dport
                    service  = self.get_serv(src_port,dst_port)
                    pckt_dict = {
                        'num':self.pkt_num,
                        'time':dt_object,
                        'ip-src':pkt['IP'].src,
                        'ip-dst':pkt['IP'].dst,
                        "ttl-pkt":ttl_pkt,
                        "len-pkt":len_pkt,
                        'port-src':str(src_port),
                        'port-dst':str(dst_port),
                        'host-name':host_name,
                        'service':service,
                        'blocked':is_blocked,
                        }
                    #print("Service",service)
                    if pkt.haslayer(TCP):
                        print("----------------------------------------")
                        print("TCP PACKET..." , "src-ip",src_ip,'port-src',src_port,"dst-ip",dst_ip,'port-dst',dst_port,"service",service)
                    if pkt.haslayer(UDP):
                        print("----------------------------------------")
                        print("UDP PACKET..." , "src-ip",src_ip,"dst-ip",dst_ip,"service",service)
                except:
                    pass
            if self.checkBox_show_packet.isChecked():
                print("Printing Packet To Table")
                self.set_pkt_on_table(pckt_dict)
                #self.packet_dict[pkt.num]
        except Exception as err:
            print(err)
            pass

    def set_pkt_on_table(self,pkt_dict):
        try:
            print("Packet Insert To Table Widget")
            row = pkt_dict['num']
            print(row)
            self.tableWidget_cap.setRowCount(row + 1)
            item_pkt_no = qtw.QTableWidgetItem(str(pkt_dict['num']))
            item_pkt_time = qtw.QTableWidgetItem(str(pkt_dict['time']))
            item_pkt_ip_src = qtw.QTableWidgetItem(pkt_dict['ip-src'])
            item_pkt_ip_dst = qtw.QTableWidgetItem(pkt_dict['ip-dst'])
            item_pkt_len = qtw.QTableWidgetItem(pkt_dict['len-pkt'])
            item_pkt_ttl = qtw.QTableWidgetItem(pkt_dict['ttl-pkt'])
            self.tableWidget_cap.setItem(row,0,item_pkt_no)
            self.tableWidget_cap.setItem(row,1,item_pkt_time)
            self.tableWidget_cap.setItem(row,2,item_pkt_ip_src)
            self.tableWidget_cap.setItem(row,3,item_pkt_ip_dst)
            self.tableWidget_cap.setItem(row,9,item_pkt_len)
            self.tableWidget_cap.setItem(row,10,item_pkt_ttl)
            if pkt_dict['service'] != None:
                item_pkt_service = qtw.QTableWidgetItem(pkt_dict['service'])
                self.tableWidget_cap.setItem(row,4,item_pkt_service)
            if pkt_dict['host-name'] != None:
                item_pkt_host_name = qtw.QTableWidgetItem(pkt_dict['host-name'])
                self.tableWidget_cap.setItem(row,5,item_pkt_host_name)
            if pkt_dict['port-src'] != None:
                item_pkt_port_src = qtw.QTableWidgetItem(pkt_dict['port-src'])
                self.tableWidget_cap.setItem(row,6,item_pkt_port_src)
            if pkt_dict['port-dst'] != None:
                item_pkt_port_dst = qtw.QTableWidgetItem(pkt_dict['port-dst'])
                self.tableWidget_cap.setItem(row,7,item_pkt_port_dst)
            if pkt_dict['blocked'] != False:
                item_pkt_blocked = qtw.QTableWidgetItem("Blocked Site")
                self.tableWidget_cap.setItem(row,8,item_pkt_blocked)
        except Exception as err:
            print(err)

    def sniffer_start(self):
        print("Start Sniffer")
        count_pkt = self.spinBox_pkt_count_by.text()
        count_pkt = int(count_pkt)
        limit_pkt = self.spinBox_pkt_limit.text()
        print(limit_pkt)
        self.counter_pkt = 0
        limit_pkt = int(limit_pkt)
        if count_pkt == 0:
            counter = 0
        else:
            counter = count_pkt
        comb_network = self.comboBox_sniff_cards
        print(comb_network.currentText())
        while self.SNF == True:
            sc.sniff(iface=comb_network.currentText(),prn=self.analyzer_sniff,count=count_pkt)
            counter += count_pkt
            self.counter_pkt = counter
            print("Packet Lista >>",counter)
            if limit_pkt == 0:
                pass
            else:
                if counter >= limit_pkt:
                    self.SNF = False

    def sniffer_results(self):
        print("Results cap")

    def sniffer_finished(self):
        save_to_db = self.checkBox_save_packet.isChecked()
        if save_to_db:
            print("Saving To DB")
            return
        else:
            print("Finished Sniffer")

    def stop_snifer(self):
        self.SNF = False
        print("Stopped Sniff")
        print(len(self.packet_lista) ," Packet Captured" )
        return self.SNF

    def continue_snifer(self):
        self.SNF = True
        print(self.SNF)
        self.threadsniffing()
        return self.SNF

    #####################################
    ####### Sites Blocked Threads #######
    def block_site_worker(self):
        worker = Worker(self.start_block_site_sample)
        self.threadpool.start(worker)

    def start_block_site_sample(self):
        """
            BlockSite Functions Start Thread
        """
        strt_bndwds = "Start Blocked Site Thread"
        print(strt_bndwds)
        with_out_www = self.checkBox_disable_www.isChecked()
        site_1 = self.lineEdit_site_name1.text()
        if site_1 != "":
            if not with_out_www:
                site_name1 = "www." + str(site_1) + ".com"
            else:
                site_name1 = str(site_1)    
            ip_1 = socket.gethostbyname(site_name1)
            host_1 = socket.getfqdn(ip_1)
        else:
            site_1 = None
        site_2 = self.lineEdit_site_name2.text()
        if site_2 != "":
            if not with_out_www:
                site_name2 = "www." + str(site_2) + ".com"
            else:
                site_name2 = str(site_2)
            ip_2 = socket.gethostbyname(site_name2)
            host_2 = socket.getfqdn(ip_2)
        else:
            site_2 = None
        #site_3 = self.lineEdit_site_name3.text()
        #host_2 = socket.gethostbyaddr(str(ip_2))
        if site_1 != None:
            self.ip_blocked = {
                1 : {'ip' : ip_1, 'name':site_1 , 'host':host_1} ,
            }
        if site_2 != None:
            self.ip_blocked = {
                2 : {'ip' : ip_1, 'name':site_1 , 'host':host_1} ,
            }
        print(self.ip_blocked)

    #####################################
    ######### BandWidth Threads #########
    def bandwidth_sample_worker(self):
        worker = Worker(self.start_calculate_bandwitdh_sample)
        #worker.signals.result.connect(self.ping_checker_results)
        self.threadpool.start(worker)

    def start_calculate_bandwitdh_sample(self):
        """
            BandWidth Calculate Functions Start Thread
        """
        strt_bndwds = "Start Bandwidth Thread"
        print(strt_bndwds)
        io = psutil.net_io_counters()
        #print(io)
        update_delay = 1 # in seconds
        # extract the total bytes sent and received
        bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv    
        gui_step_by = self.findChild(qtw.QDoubleSpinBox,"doubleSpinBox_bandwidth").text()
        gui_timeout_ping = self.findChild(qtw.QSpinBox,"spinBox_timeout_bandwidth").text()
        timeout_counter = 0
        step_by = float(gui_step_by)
        timeout_ping = float(gui_timeout_ping)
        time_st = datetime.now()
        print("Bandwidth Traffic Start")
        while timeout_counter < timeout_ping:
            res = calc_bandwidth(self,bytes_sent=bytes_sent,bytes_recv=bytes_recv,update_delay=update_delay)
            QThread.msleep(step_by)
            print(res)
            self.bandwidth_set_to_dict(response_dic=res)
            #timeout_counter += step_by
            time_end = datetime.now()
            all_time = time_end - time_st
            timeout_counter = float(all_time.seconds)
            print(all_time.seconds)

    def bandwidth_services_worker(self):
        worker = Worker(self.start_calculate_bandwitdh_services_method1)
        worker2 = Worker(self.start_calculate_bandwitdh_services_method2)
        worker3 = Worker(self.start_sniff_services)
        worker.signals.result.connect(self.bandwitdh_services_results)
        self.threadpool.start(worker)
        global worker_bandwidth_1,worker_bandwidth_2 , worker_bandwidth_3
        worker_bandwidth_1 = worker
        worker_bandwidth_2 = worker2
        worker_bandwidth_3 = worker3
        self.threadpool.start(worker2)
        self.threadpool.start(worker3)

    def start_calculate_bandwitdh_services_method1(self):
        """
            Simple function that keeps printing the stats
        """
        strt_bndwds = "Start Bandwidth Services Collect"
        print(strt_bndwds)
        # extract the total bytes sent and received
        gui_step_by = self.findChild(qtw.QDoubleSpinBox,"doubleSpinBox_bandwidth_services").text()
        gui_timeout_ping = self.findChild(qtw.QSpinBox,"spinBox_timeout_bandwidth_services").text()
        timeout_counter = 0
        step_by = float(gui_step_by)
        timeout_ping = float(gui_timeout_ping)
        time_st = datetime.now()
        print("Bandwidth Traffic Start")
        # self.tableWidget_bandwidth_services.setColumnCount(4)
        # columns = ('PID','Name','Download','Upload')
        # self.tableWidget_bandwidth_services.setHorizontalHeaderLabels(columns)
        while timeout_counter < timeout_ping and self.LOOPSRVS !=False:
            try:
                # self.bandwidth_set_to_dict(response_dic=res)
                #timeout_counter += step_by
                time_end = datetime.now()
                all_time = time_end - time_st
                all_time = all_time.seconds
                timeout_counter = float(all_time)
                response_services = print_pid2traffic()
                self.set_services_bandwidth_to_table(response_services)
                time.sleep(step_by)
            except Exception as err:
                time.sleep(step_by)
                print("Error Bandwidth Traffic",err)
        print("Finished Bandwidth Traffic Start")
        self.LOOPSRVS = False
        #self.threadpool.clear()
        # self.threadpool.cancel(worker_bandwidth_1)
        self.threadpool.cancel(worker_bandwidth_2)
        self.threadpool.cancel(worker_bandwidth_3)

    def set_services_bandwidth_to_table(self,resp):
        """
            Convert From Global DataFrame which created by pandas to Gui Table Widget
        """
        self.tableWidget_bandwidth_services.clear()
        self.tableWidget_bandwidth_services.setRowCount(len(resp))
        dict_resp = resp.to_dict()
        #print(dict_resp)
        if 'name' in dict_resp:
            for key , dict_values in dict_resp.items():
                #print("key >>>   ",key)
                #print("dict_values >>>>     ",dict_values)
                count_services = 0
                for pid,value in dict_values.items():
                    #print("pid #",pid)
                    item_pid = qtw.QTableWidgetItem(str(pid))
                    self.tableWidget_bandwidth_services.setItem(count_services,0,item_pid)
                    if key == "name":
                        item_name = qtw.QTableWidgetItem(str(value))
                        self.tableWidget_bandwidth_services.setItem(count_services,1,item_name)
                    if key == "Download":
                        item_download = qtw.QTableWidgetItem(str(value))
                        self.tableWidget_bandwidth_services.setItem(count_services,2,item_download)
                    if key == "Upload":
                        item_upload = qtw.QTableWidgetItem(str(value))
                        self.tableWidget_bandwidth_services.setItem(count_services,3,item_upload)
                        #print("Key", key)
                        #print("value ############ ",value)
                    #print("dict_resp",dict_resp['name'])
                    count_services += 1

    def bandwitdh_services_results(self):
        QThread.sleep(2)
        self.LOOPSRVS = True
        print("Timer Bandwidth Services Finished")

    def start_calculate_bandwitdh_services_method2(self):
        """
            A function that keeps listening for connections on this machine 
            and adds them to `connection2pid` global variable
        """
        global connection2pid    
        gui_step_by = self.findChild(qtw.QDoubleSpinBox,"doubleSpinBox_bandwidth_services").text()
        gui_timeout_ping = self.findChild(qtw.QSpinBox,"spinBox_timeout_bandwidth_services").text()
        timeout_counter = 0
        step_by = float(gui_step_by)
        timeout_ping = float(gui_timeout_ping)
        time_st = datetime.now()
        #print("Bandwidth Traffic Start")
        while self.LOOPSRVS != False:
            try:
                time_end = datetime.now()
                all_time = time_end - time_st
                all_time = all_time.seconds
                timeout_counter = float(all_time)
                #while True:
                    # using psutil, we can grab each connection's source and destination ports
                    # and their process ID
                for c in psutil.net_connections():
                    if c.laddr and c.raddr and c.pid:
                        # if local address, remote address and PID are in the connection
                        # add them to our global dictionary
                        connection2pid[(c.laddr.port, c.raddr.port)] = c.pid
                        connection2pid[(c.raddr.port, c.laddr.port)] = c.pid
                #time.sleep(step_by)
                    #print(connection2pid)
            except Exception as err:
                print("Error",err)
       
    def start_sniff_services(self):
        gui_step_by = self.findChild(qtw.QDoubleSpinBox,"doubleSpinBox_bandwidth_services").text()
        gui_timeout_ping = self.findChild(qtw.QSpinBox,"spinBox_timeout_bandwidth_services").text()
        timeout_counter = 0
        step_by = float(gui_step_by)
        timeout_ping = float(gui_timeout_ping)
        time_st = datetime.now()
        while self.LOOPSRVS != False:
            try:
                time_end = datetime.now()
                all_time = time_end - time_st
                all_time = all_time.seconds
                timeout_counter = float(all_time)
                sc.sniff(prn=process_packet, store=False)
                #time.sleep(step_by)
            except Exception as err:
                print("Error",err)
                #time.sleep(step_by)
    def process_packet(self,packet):
        global pid2traffic
        try:
            # get the packet source & destination IP addresses and ports
            packet_connection = (packet.sport, packet.dport)
        except (AttributeError, IndexError):
            # sometimes the packet does not have TCP/UDP layers, we just ignore these packets
            pass
        else:
            # get the PID responsible for this connection from our `connection2pid` global dictionary
            packet_pid = connection2pid.get(packet_connection)
            if packet_pid:
                if packet.src in all_macs:
                    # the source MAC address of the packet is our MAC address
                    # so it's an outgoing packet, meaning it's upload
                    pid2traffic[packet_pid][0] += len(packet)
                else:
                    # incoming packet, download
                    pid2traffic[packet_pid][1] += len(packet)        

    def bandwidth_set_to_dict(self,response_dic):
        """
            Gui Functions Signal To Set Results Bandwidth
        """
        res = response_dic
        self.label_bandwidth_down_speed.setText(res['Download Speed'])
        self.label_bandwidth_upload_speed.setText(res['Upload Speed'])
        self.lineEdit_bandwidth_down.setText(res['Download'])
        self.lineEdit_bandwidth_upload.setText(res['Upload'])

    ###################################
    ########### Message Box ###########
    ###################################
    def message_error(self, s,timer_sleep=None):
        if timer_sleep == None:
            print("Error", s)
            dlg = QMessageBox(self)
            dlg.setText(s)
            dlg.setIcon(QMessageBox.Warning)
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setWindowTitle("Error")
            button = dlg.exec_()
        else:
            print("Error Timer", s)
            dlg = QMessageBox(self)
            dlg.setText(s)
            dlg.setWindowTitle("Error")
            button = dlg.exec_()
        
    ###################################
    ########### Start Ping ############
    ###################################
    def thread_ping_all(self):
        worker = Worker(self.start_ping_all_scanned)
        worker.signals.result.connect(self.ping_all_scanned_result)
        self.threadpool.start(worker)

    def thread_ping_check_auto_save(self):
        worker = Worker(self.ping_checker_auto)
        #worker.signals.result.connect(self.ping_checker_results)
        self.threadpool.start(worker)

    def start_ping_all_scanned(self):
        print("Ping All Scanned")
        gui_step_by = self.findChild(qtw.QSpinBox,"spinBox_step_ping_all").text()
        auto_check = self.checkBox_ping_timer_all.isChecked()
        ping_save_check = self.checkBox_ping_save_db_home.isChecked()
        listen_dev_check = self.checkBox_listen_dev_off.isChecked()
        dev_save_check = self.checkBox_save_dev_db.isChecked()
        step_by = float(gui_step_by)
        print(auto_check)
        if auto_check:
            while self.LOOPPINGER:
                try:
                    online_devices = 0
                    self.pushButton_ping_all.setText("Pinging ...")
                    self.pushButton_ping_all_stop.setEnabled(True)
                    self.pushButton_ping_all.setEnabled(False)
                    for row_num , row_info in ip_scanned.items():
                        try:
                            check_ip = self.findChild(qtw.QCheckBox,f"checkBox_ping_{str(row_num)}").isChecked()
                        except:
                            continue
                        if check_ip == True:
                            resp = self.which_ip_to_ping(num_ip=row_num)
                            if resp['Response'] == True:
                                online_devices += 1
                            else:
                                if listen_dev_check == True:
                                    self.error_message = f"Device With Ip {resp['IP']} and Mac Address {resp['Mac']} Has an error and sent to administration e-mail"
                                    self.LOOPPINGER = False
                                    break
                            if dev_save_check == True:
                                try:
                                    print("Start To Create Device")
                                    ip = resp['IP']
                                    mac = resp['Mac']
                                    self.db.connect()
                                    try:
                                        dev = Device.select().where(Device.mac_address == mac).get()
                                        print(dev)
                                    except:
                                        dev = None
                                    if dev != None:
                                        print("Found",dev)
                                        self.db.close()
                                    else:
                                        print(ip)
                                        print(mac)
                                        #self.db.connect()
                                        dev = Device.create(
                                            ip_dev=ip,
                                            mac_address=mac,
                                            )
                                        dev.save()
                                        self.db.close()
                                        print("Device Created",ip,"Success")
                                except "UNIQUE" in Exception:
                                    print("Device Already Inserted : ",err)
                                    self.db.close()
                                    pass
                                except Exception as err:
                                    print("Failed To Create Instance : ",err)
                                    self.db.close()
                                    pass
                            if ping_save_check == True:
                                try:
                                    print("Start To Create Ping")
                                    self.db.connect()
                                    dev = Device.select().where(Device.mac_address == resp['Mac']).get()
                                    print(dev)
                                    #print(dev.ip_dev)
                                    ping_obj = PingInfo.create(
                                        owner=dev,
                                        is_anwsred = resp['Response'],
                                        resp_time = resp['ResTime'],
                                        ttl = resp['TTL'],
                                    )
                                    ping_obj.save()
                                    self.db.close()
                                    print("Created","IP",resp['IP'],"Response Time",resp['ResTime'])
                                except Exception as err:
                                    self.db.close()
                                    print("Error In Save To db > ",err)
                    print("Online Devices",online_devices)
                    self.lcdNumber.display(online_devices)
                    time.sleep(step_by)
                except NameError:
                    print("Scan Network First Please ....")
                    self.LOOPPINGER = False
                except Exception as err:
                    print("Error",err)
                    self.LOOPPINGER = False
        else:
            try:
                for row_num , row_info in ip_scanned.items():
                    check_ip = self.findChild(qtw.QCheckBox,f"checkBox_ping_{str(row_num)}").isChecked()
                    if check_ip == True:
                        self.which_ip_to_ping(num_ip=row_num)
                time.sleep(step_by)
            except NameError:
                print("Scan Network First Please ....")
                self.LOOPPINGER = False
            except Exception as err:
                print("Error",err)
                self.LOOPPINGER = False

    def ping_all_scanned_result(self):
        print("Ping All Results ")
        try:
            if len(ip_scanned) > 0:
                print("Scanned")
            else:
                print("Not Scanned")
        except NameError:
            self.message_error(s="Scan Network First Please")
        if self.error_message != None:
            self.message_error(s=str(self.error_message))
            self.error_message = None
        btn_stop_ping = self.findChild(qtw.QPushButton,"pushButton_ping_all_stop")
        btn_strt_ping = self.findChild(qtw.QPushButton,"pushButton_ping_all")
        btn_strt_ping.setText("Start Ping")
        btn_stop_ping.setEnabled(False)
        btn_strt_ping.setEnabled(True)
        self.LOOPPINGER = True

    def stop_ping(self):
        print("Ping Stopped")
        self.LOOPPINGER = False

    def ping_checker_auto(self,main=None):
        #time_st = datetime.datetime.now().second
        print(main)
        gui_step_by = self.findChild(qtw.QDoubleSpinBox,"doubleSpinBox_ping_stepby").text()
        gui_timeout_ping = self.findChild(qtw.QSpinBox,"spinBox_ping_timeout").text()
        timeout_counter = 0
        step_by = float(gui_step_by)
        timeout_ping = float(gui_timeout_ping)
        time_st = datetime.now()
        ip_scanned_checked = self.checkBox_ping_ip_scanned.isChecked()
        multi_check = self.checkBox_ping_timer.isChecked()
        save_device_db_check = self.checkBox_save_device_db.isChecked()
        if main == True:
            ip_scanned_checked = True
            gui_step_by = self.findChild(qtw.QDoubleSpinBox,"spinBox_step_ping_all").text()
            step_by = float(gui_step_by)
        print("Ping Checker Is Running")
        if save_device_db_check:
            list_to_check = []
            for n in range(4):
                try:
                    text = self.findChild(qtw.QLineEdit,f'lineEdit_ip_to_ping_{str(n)}').text()
                    if text != "":
                        list_to_check.append(text)
                except:
                    pass
            if ip_scanned_checked != True:
                print("IP Scanned Manual",list_to_check)
                if len(list_to_check) >= 1:
                    for ip in list_to_check:
                        try:
                            #print("Create IP Scanned In Database Info")
                            self.insert_ip_to_db(scanned_dic=False,ip_to_save=ip)
                        except:
                            self.db.close()
                            pass
            else:
                try:
                    #print("Create IP Scanned In Database Info")
                    self.insert_ip_to_db()
                except:
                    self.db.close()
                    pass
        if multi_check:
            while timeout_counter < timeout_ping:
                self.ping_checker()
                QThread.sleep(step_by)
                #timeout_counter += step_by
                time_end = datetime.now()
                all_time = time_end - time_st
                timeout_counter = float(all_time.seconds)
                print(all_time.seconds)
        else:
            self.ping_checker()
        #print(str_time)

    def thread_ping_save_in_db(self):
        worker = Worker(self.ping_checker)
        #worker.signals.result.connect(self.ping_checker_results)
        self.threadpool.start(worker)

    def ping_checker(self,from_main=False):
        ip_scanned_checked = self.checkBox_ping_ip_scanned.isChecked()
        save_ping_to_db_checked = self.checkBox_save_ping_db.isChecked()
        save_device_to_db_checked = self.checkBox_save_device_db.isChecked()
        list_to_check = []
        for n in range(4):
            try:
                text = self.findChild(qtw.QLineEdit,f'lineEdit_ip_to_ping_{str(n)}').text()
                if text != "":
                    list_to_check.append(text)
            except:
                pass
        #print("Start Create If Not In DB")
        #print("Start Ping Checker")
        if ip_scanned_checked:
            try:
                for row_num , row_info in ip_scanned.items():
                    ip = row_info['IP']
                    mac = row_info['Mac']
                    ## Get Ip Ping Response And prepare it to save in db if checked 
                    ip_ping_response = self.collect_ping_to_dict(ip)
                    if save_ping_to_db_checked:
                        try:
                            print("Start To Create Ping")
                            self.db.connect()
                            dev = Device.select().where(Device.mac_address == mac).get()
                            #print(dev)
                            #print(dev.ip_dev)
                            ping_obj = PingInfo.create(
                                owner=dev,
                                is_anwsred = ip_ping_response['Response'] ,
                                details = ip_ping_response
                            )
                            ping_obj.save()
                            self.db.close()
                            print("Created",ip)
                        except Exception as err:
                            self.db.close()
                            print("Error In Save To db > ",err)
            except NameError:
                print("Scan Network First Please ....")
                
            except Exception as err:
                print("Error",err)
                pass
        else:
            for ip in list_to_check:
                ip_ping_response = self.collect_ping_to_dict(ip)
                print(ip_ping_response)
                if save_ping_to_db_checked:
                    try:
                        self.db.connect()
                        ping_obj = PingInfo.create(
                                is_anwsred = ip_ping_response['Response'] ,
                                details = ip_ping_response
                            )
                        ping_obj.save()
                        self.db.close()
                        print("Created",ip)
                    except Exception as err:
                        self.db.close()
                        print("Error",err)
                        pass
            #print(list_to_check)              
    def insert_ip_to_db(self,scanned_dic=True,ip_to_save=None):
        try:
            if scanned_dic == True:
                print(ip_scanned)
                print(len(ip_scanned))
                for row_num , row_info in ip_scanned.items():
                    ip = row_info['IP']
                    mac = row_info['Mac']
                    try:
                        self.db.connect()
                        ip_1 = Device.create(
                            ip_dev=ip,
                            mac_address=mac
                            )
                        ip_1.save()
                        self.db.close()
                        print("Device Created", ip,mac ,"Success")
                    except "UNIQUE" in Exception:
                        print("Device Already Inserted : ",err)
                        self.db.close()
                    except Exception as err:
                        print("Failed To Create Instance : ",err)
                        self.db.close()
            else:
                print(ip_to_save)
                try:
                    self.db.connect()
                    ip_1 = Device.create(
                        ip_dev=ip_to_save,
                        is_local=False,
                        )
                    ip_1.save()
                    self.db.close()
                    print("Device Created", ip_to_save ,"Success")
                except "UNIQUE" in Exception:
                    print("Device Already Inserted : ",err)
                    self.db.close()
                except Exception as err:
                    print("Failed To Create Instance : ",err)
                    self.db.close()

        except NameError:
            print("Scan Network First Please ....")
            self.db.close()
            pass
        except:
            self.db.close()
            pass
        
    def collect_ping_to_dict(self,ip_to_ping):
        ip_ping_response = {
            'IP':ip_to_ping,
            'Mac':None,
            'Checked':False,
            'Response':False,
            'TTL':None,
            'ResTime':None,
        }
        if ip_to_ping == "" :
            pass
        else:
            ping_response = self.ping_ip(ip_to_ping)
            if "Reply from" in ping_response and \
                not "Destination host unreachable." in ping_response:
                ## Find Results In Respons String In Terminal
                ttl_index = ping_response.find("TTL=")
                ttl = ping_response[ttl_index+4:ttl_index+7].strip()
                time_index = ping_response.find("time=")
                time_index_end = ping_response.find("ms TTL")
                time_ping = ping_response[time_index+5:time_index_end]
                ## Set Results To variable ip_ping_response type(dict)
                ip_ping_response['Checked'] = True
                ip_ping_response['Response'] = True
                ip_ping_response['TTL'] = ttl
                ip_ping_response['ResTime'] = time_ping
            if  "Reply from" in ping_response :
                ip_ping_response['Checked'] = True
                print(ping_response)
                if "Destination host unreachable." in ping_response:
                    ip_ping_response['Response'] = False
        return ip_ping_response

    def ping_checker_results(self):
        print("Done Results")

    ### Table Widget Ping And Device ###
    def set_table_widget_from_db(self):
        worker = Worker(self.get_table_rows)
        worker.signals.result.connect(self.results_get_info_table)
        self.threadpool.start(worker)

    def get_table_rows(self):
        from db_to_qt import devss
        from db_to_qt import pingss
        global dev_db , ping_db , max_ping_table
        dev_db = devss
        ping_db = pingss
        max_ping_table = 100
        self.tableWidget1_ping.setRowCount(len(ping_db))
        # self.tableWidget1_ping.setRowCount(max_ping_table)
        print(len(devss))
        print(len(pingss))
        
    def results_get_info_table(self):
        print("Done Get Data")
        try:
            for counter , ping in enumerate(ping_db):
                try:
                    time_ping = str(ping.created_at).split(".")[0]
                except:
                    pass
                try:
                    owner_ip = str(ping.owner.ip_dev)
                except:
                    owner_ip = "Not Found"
                item_id = qtw.QTableWidgetItem(str(ping.id))
                item_anwser = qtw.QTableWidgetItem(str(ping.is_anwsred))
                item_time = qtw.QTableWidgetItem(str(time_ping))
                item_owner = qtw.QTableWidgetItem(str(owner_ip))
                self.tableWidget1_ping.setItem(counter,1,item_owner)
                #item_det = qtw.QTableWidgetItem(str(ping.details))
                #self.tableWidget1_ping.setItem(counter,4,item_det)
                self.tableWidget1_ping.setItem(counter,0,item_id)
                self.tableWidget1_ping.setItem(counter,2,item_anwser)
                self.tableWidget1_ping.setItem(counter,3,item_time)
        except Exception as err:
            print(err)
        print("Finished")

def create_app():
    #widget_meters = AnalogGaugeWidget()
    #window = Main()
    window = Login()
    window.show()
    app.exec_()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle('Fusion')
    
    #engine = QQmlApplicationEngine()
    #engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))
    # with open("front/style.qss", "r") as f:
    #     _style = f.read()
    #     app.setStyleSheet(_style)
    list_theme = [
        'dark_amber.xml',
        'dark_blue.xml',
        'dark_cyan.xml',
        'dark_lightgreen.xml',
        'dark_pink.xml',
        'dark_purple.xml',
        'dark_red.xml',
        'dark_teal.xml',
        'dark_yellow.xml',
        'light_amber.xml',
        'light_blue.xml',
        'light_cyan.xml',
        'light_cyan_500.xml',
        'light_lightgreen.xml',
        'light_pink.xml',
        'light_purple.xml',
        'light_red.xml',
        'light_teal.xml',
        'light_yellow.xml'
    ]
    #apply_stylesheet(app, theme=list_theme[1])
    
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    create_app()
    is_program_running = True
