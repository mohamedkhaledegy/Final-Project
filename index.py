import sys
import os
import time
import datetime
import timeit
import subprocess
#import numpy as np

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
import pyshark

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

ui_main,_ = loadUiType('front/main_window2.ui')

ui_login,_ot = loadUiType('front/second_window.ui')

is_program_running = True

class Login(QMainWindow , ui_login):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_open = self.findChild(qtw.QPushButton,"pushButton")
        self.btn_open.clicked.connect(self.log_in_system)
    def log_in_system(self):
        self.window2 = Main()
        self.close()
        self.window2.show()

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
        #self.set_data_base()

        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        ## Custom Functions ##
        self.set_matplot()
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
    def open_new_win(self):
        print("Opened")
        self.win = Login()
        self.close()
        self.win.show()
        
    def set_vars(self):
        self.db = my_db
        self.all_devs = None
        self.packet_lista = []
        self.packet_dict = {}
        self.SNF = True
        self.pkt_num = 0
        self.threadpool = QThreadPool()
        self.layout = qtw.QHBoxLayout()
        self.main_widget = self.findChild(qtw.QTabWidget,"tabWidget")

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
        print("Finished")
        from db_to_qt import devss as devs
        from db_to_qt import pingss as devs_pngs
        print(devs)
        print(all_pings)

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
        print(len(self.packet_lista))
        self.tableWidget_cap.setRowCount(10)
        qtw.QApplication.processEvents()
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
        mac_addr = self.findChild(qtw.QLabel,f"lineEdit_mac{num_ip}")
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
                label_to_color.setStyleSheet(u"background-color: rgb(0, 0, 0);")
            else:
                if "Reply from" in ping_response and \
                    not "Destination host unreachable." in ping_response:
                    label_to_color.setStyleSheet(u"background-color: rgb(0, 255, 0);padding: 2px;")
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
                else:
                    ip_ping_response['Checked'] = True
                    ip_ping_response['Response'] = False
                    label_to_color.setStyleSheet(u"background-color: rgb(170, 0, 0);")
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
        time_choosed = 9
        ## resault in %100
        stop_point_of_100 = time_choosed/100
        ## convert to msleep (sleep 1 second = mlsleep 1000 mlsecond) 
        stop_point_of_100 = stop_point_of_100 * 1000
        print(stop_point_of_100)
        #QThread.sleep(2)
        num = 0
        for i in range(101):
            print(i)
            # if self.lineEdit_ip_host.text() != "":
            #     self.frame_2_circle_progres.rpb_setValue(100)
            #     break
            num += 1
            #val_now = self.frame_2_cricle_progres.rpb_getValue()
            #print(val_now)
            self.frame_2_circle_progres.rpb_setValue(i)
            QThread.msleep(stop_point_of_100)
        return num

    def first_thread_result(self):
        #self.frame_2_circle_progres.rpb_setValue(100)
        print("First Thread Result")
    
    def first_thread_finished(self):
        print("First Thread Scan finished")
        self.btn_thread.setText("Finished")
        
    def second_thrd_scan_network(self):
        global ip_scanned
        self.btn_thread.setText("Processing...")
        print("Start Scan")
        ip_scanned = scan_network("192.168.1.1/24")
        #print("Finish Scan")
        #print(ip_scanned)
        return ip_scanned

    def third_thrd_speed_test(self):
        print("Start Test Speed")
        global speed_test_dict
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = return_bytes_by_mb(st.download())
        uploaad_speed = return_bytes_by_mb(st.upload())
        speed_test_dict = st.results.dict()
        #print(res_dict)
        #print("Your Download speed is", download_speed, "MB")
        print("Finished Test Speed Internet")
        #print("End Result First Thread")
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
        num = 0
        for i in range(101):
            print(i)
            num += 1
            #self.frame_1_circle_progres.rpb_setValue(i)
            self.frame_4_circle_progres.rpb_setValue(i)
            QThread.msleep(stop_point_of_100)

    def second_thread_scan_result(self):
        """
            Scan Network Results
            Loop on IP Scanned for Collect Info Stored In Dictionary (global var) > Updated in method : self.thread_scan_network
        """
        self.section_network.setEnabled(True)
        self.section_ip_discovered.setEnabled(True)
        print(len(ip_scanned))
        for row_num , row_info in ip_scanned.items():
            print(row_num)
            print(row_info)
            ip = row_info['IP']
            mac = row_info['Mac']
            label_ip = self.findChild(qtw.QLineEdit,f"lineEdit_ip{str(row_num)}")
            label_mac = self.findChild(qtw.QLineEdit,f"lineEdit_mac{str(row_num)}")
            #print(dir(self.label_ip))
            label_ip.setText(str(ip))
            label_mac.setText(str(mac))

    def third_thrd_speed_test_result(self):
        print("Third Thread Scan Result")

    def fourth_thrd_speed_test_result(self):
        print("Fourth Thread Speed Test Progress Result")


    def second_thread_scan_finished(self):
        print("Second Thread Scan finished")

    def third_thrd_speed_test_finished(self):
        print("Third Thread Speed Test Finished")
        down_speed_mb = return_bytes_by_mb(speed_test_dict['download'])
        up_speed_mb = return_bytes_by_mb(speed_test_dict['upload'])
        # Convert To Limit 2 After ,
        dwn_mb = round(down_speed_mb,2)
        up_mb = round(up_speed_mb,2)
        # Set To Gui
        self.lineEdit_download.setText(str(dwn_mb))
        self.lineEdit_upload.setText(str(up_mb))
        self.lineEdit_ping.setText(str(speed_test_dict['ping']))
        self.lineEdit_host.setText(str(speed_test_dict['server']['host']))
        self.lineEdit_city.setText(str(speed_test_dict['server']['name']))
        self.lineEdit_sponsor.setText(str(speed_test_dict['client']['isp']))
        self.lineEdit_lon.setText(str(speed_test_dict['client']['lon']))
        self.lineEdit_lat.setText(str(speed_test_dict['client']['lat']))

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
        self.threadpool.start(worker)

    def analyzer_sniff(self,pkt):
        self.pkt_num += 1
        ## Full Date
        ## strftime("%H:%M:%S"
        dt_object = datetime.fromtimestamp(pkt.time)        
        t1 = str(self.pkt_num)
        pckt_dict = {
            'num':self.pkt_num,
            'time':dt_object,
            'ip-src':pkt['IP'].src,
            'ip-dst':pkt['IP'].dst,
            }
        self.set_pkt_on_table(pckt_dict)
        self.packet_lista.append(pckt_dict['num'])

    def set_pkt_on_table(self,pkt_dict):
        row = pkt_dict['num']
        #print(pkt_dict)
        #row-1
        #print("row",row)
        item_pkt_no = qtw.QTableWidgetItem(str(pkt_dict['num']))
        item_pkt_time = qtw.QTableWidgetItem(str(pkt_dict['time']))
        item_pkt_ip_src = qtw.QTableWidgetItem(pkt_dict['ip-src'])
        item_pkt_ip_dst = qtw.QTableWidgetItem(pkt_dict['ip-dst'])
        self.tableWidget_cap.setItem(row,0,item_pkt_no)
        self.tableWidget_cap.setItem(row,1,item_pkt_time)
        self.tableWidget_cap.setItem(row,2,item_pkt_ip_src)
        self.tableWidget_cap.setItem(row,3,item_pkt_ip_dst)

    def sniffer_start(self):
        print("Start Sniffer")
        count_pkt = 0
        if count_pkt == 0:
            counter = 1
        else:
            counter = count_pkt
        while self.SNF == True:
            sc.sniff(iface="Realtek PCIe GBE Family Controller",prn=self.analyzer_sniff,count=count_pkt)
            counter += count_pkt
            print("Packet Lista >>",len(self.packet_lista))
            self.tableWidget_cap.setRowCount(counter)

    def sniffer_results(self):
        print("Results cap")

    def stop_snifer(self):
        self.SNF = False
        print(self.SNF)
        print("Stopped Sniff")
        print(len(self.packet_lista) ," Packet Captured"  )
        #print(packet_lista[-1])
        #self.event_stop.set()
        #worker = Worker(self.sniffer_start)
        #worker.signals.result.connect(self.sniffer_results)
        #self.threadpool.stop()
        return self.SNF

    def continue_snifer(self):
        self.SNF = True
        print(self.SNF)
        self.threadsniffing()
        #self.threadsniffing()
        return self.SNF

    def threadsniffing1(self):
        worker2 = Worker(self.sniffer1_start)
        worker2.signals.result.connect(self.sniffer1_results)
        self.threadpool.start(worker2)

    def sniffer1_start(self):
        print("Start Sniffer")
        count_pkt = 4
        capture = pyshark.LiveCapture(interface="Ethernet").sniff_continuously(packet_count=4)
        #capture
        #capture.sniff(timeout=5)
        #cap.sniff(packet_count=20)
        print("Captured ",count_pkt)

    def sniffer1_results(self):
        print("Start Sniffer")
        count_pkt = 4
        counter = count_pkt
        while self.SNF == True:
            sc.sniff(iface="Ethernet",prn=self.analyzer_sniff,count=count_pkt)



    #####################################
    ######### Site Blocked Threads #########
    def block_site_worker(self):
        worker = Worker(self.start_block_site_sample)
        #worker.signals.result.connect(self.ping_checker_results)
        self.threadpool.start(worker)
        
    def start_block_site_sample(self):
        """
            BandWidth Calculate Functions Start Thread
        """
        strt_bndwds = "Start Blocked Site Thread"
        print(strt_bndwds)
        site_1 = self.lineEdit_site_name1.text()
        site_2 = self.lineEdit_site_name2.text()
        site_3 = self.lineEdit_site_name3.text()
        print(site_1)
        print(site_2)
        print(site_3)

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
        time_st = datetime.datetime.now()
        print("Bandwidth Traffic Start")
        while timeout_counter < timeout_ping:
            res = calc_bandwidth(self,bytes_sent=bytes_sent,bytes_recv=bytes_recv,update_delay=update_delay)
            time.sleep(step_by)
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
        #worker.signals.result.connect(self.ping_checker_results)
        self.threadpool.start(worker)
        self.threadpool.start(worker2)
        self.threadpool.start(worker3)

    def start_calculate_bandwitdh_services_method1(self):
        """Simple function that keeps printing the stats"""
        strt_bndwds = "Start Bandwidth Services Collect"
        print(strt_bndwds)
        #update_delay = 1 # in seconds
        # extract the total bytes sent and received
        gui_step_by = self.findChild(qtw.QDoubleSpinBox,"doubleSpinBox_bandwidth_services").text()
        gui_timeout_ping = self.findChild(qtw.QSpinBox,"spinBox_timeout_bandwidth_services").text()
        timeout_counter = 0
        step_by = float(gui_step_by)
        timeout_ping = float(gui_timeout_ping)
        time_st = datetime.now()
        print("Bandwidth Traffic Start")
        self.tableWidget_bandwidth_services.setColumnCount(4)
        columns = ['PID','Name','Download','Upload']
        self.tableWidget_bandwidth_services.setHorizontalHeaderLabels(columns)
        while timeout_counter < timeout_ping:
            time.sleep(step_by)
            # self.bandwidth_set_to_dict(response_dic=res)
            #timeout_counter += step_by
            time_end = datetime.now()
            all_time = time_end - time_st
            all_time = all_time.seconds
            timeout_counter = float(all_time)
            print(all_time)
            response_services = print_pid2traffic()
            self.set_services_bandwidth_to_table(response_services)

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
        while timeout_counter < timeout_ping:
            time.sleep(step_by)
            time_end = datetime.now()
            all_time = time_end - time_st
            all_time = all_time.seconds
            timeout_counter = float(all_time)
            print(all_time)
            while True:
                # using psutil, we can grab each connection's source and destination ports
                # and their process ID
                for c in psutil.net_connections():
                    if c.laddr and c.raddr and c.pid:
                        # if local address, remote address and PID are in the connection
                        # add them to our global dictionary
                        connection2pid[(c.laddr.port, c.raddr.port)] = c.pid
                        connection2pid[(c.raddr.port, c.laddr.port)] = c.pid
                #print(connection2pid)

    def start_sniff_services(self):
        gui_step_by = self.findChild(qtw.QDoubleSpinBox,"doubleSpinBox_bandwidth_services").text()
        gui_timeout_ping = self.findChild(qtw.QSpinBox,"spinBox_timeout_bandwidth_services").text()
        timeout_counter = 0
        step_by = float(gui_step_by)
        timeout_ping = float(gui_timeout_ping)
        time_st = datetime.now()
        while timeout_counter < timeout_ping:
            time.sleep(step_by)
            time_end = datetime.now()
            all_time = time_end - time_st
            all_time = all_time.seconds
            timeout_counter = float(all_time)
            print(all_time)
            #time.sleep(step_by)
            sc.sniff(prn=process_packet, store=False)

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

    def thread_ping_check_auto_save(self):
        worker = Worker(self.ping_checker_auto)
        #worker.signals.result.connect(self.ping_checker_results)
        self.threadpool.start(worker)

    def ping_checker_auto(self):
        #time_st = datetime.datetime.now().second
        gui_step_by = self.findChild(qtw.QDoubleSpinBox,"doubleSpinBox_ping_stepby").text()
        gui_timeout_ping = self.findChild(qtw.QSpinBox,"spinBox_ping_timeout").text()
        timeout_counter = 0
        step_by = float(gui_step_by)
        timeout_ping = float(gui_timeout_ping)
        time_st = datetime.now()
        while timeout_counter < timeout_ping:
            self.ping_checker()
            time.sleep(step_by)
            #timeout_counter += step_by
            print("Ping Checker Is Running")
            time_end = datetime.now()
            all_time = time_end - time_st
            timeout_counter = float(all_time.seconds)
            print(all_time.seconds)
        #print(str_time)

    def thread_ping_save_in_db(self):
        worker = Worker(self.ping_checker)
        #worker.signals.result.connect(self.ping_checker_results)
        self.threadpool.start(worker)

    def ping_checker(self):
        #print("Start Create If Not In DB")
        try:
            #print("Create IP Scanned In Database Info")
            self.insert_ip_to_db()
        except:
            self.db.close()
            pass
        #print("Start Ping Checker")
        try:
            for row_num , row_info in ip_scanned.items():
                ip = row_info['IP']
                mac = row_info['Mac']
                ip_ping_response = self.collect_ping_to_dict(ip)
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
                    
    def insert_ip_to_db(self):
        try:
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
        except NameError:
            print("Scan Network First Please ....")
            pass
        except:
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
            else:
                ip_ping_response['Checked'] = True
                ip_ping_response['Response'] = False
        return ip_ping_response

    def ping_checker_results(self):
        print("Done Results")



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
    with open("front/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    create_app()
    is_program_running = True

