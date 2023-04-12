import sys
import os
import time
import timeit
import subprocess
#import pyshark
# from PyQt5.QtDesigner import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5 import QtWidgets as qtw
# from PyQt5.QtQml import QQmlApplicationEngine
# from PyQt5.uic import loadUiType
# Import As Pyside2
from PySide2.QtWidgets import *
#from PyQt5.QtDesigner import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import QtWidgets as qtw
from PySide2.QtUiTools import loadUiType
from scapy import all as sc

import threading

#from meters import AnalogGaugeWidget
from threads_custom.scan_network import scan_network 

## Import Buttons Config & Signal
from btns.circle_btns import *
from btns.btns import *

## Import Threads Functions
from threads_custom.works import Worker
from threads_custom.test_speed import *
from threads_custom.thrds import thrd_folder
#from threading import Event

#from front import *

app = qtw.QApplication(sys.argv)
app.setStyle('Fusion')
ui_main,_ = loadUiType('main_window2.ui')

ui_main2,_ot = loadUiType('second_window.ui')
main_window = qtw.QMainWindow

class MainWindow(main_window,ui_main):
    def __init__(self):
        main_window.__init__(self)
        self.setupUi(self)
        self.time = QTime()
        ## Progress Tube
        ## UiComponents(self)
        ## self.initUI()
        set_btns(self)
        self.threadpool = QThreadPool()
        self.layout = qtw.QHBoxLayout()
        print("Maximum Threads : %d" % self.threadpool.maxThreadCount())
        self.main_widget = self.findChild(qtw.QTabWidget,"tabWidget")
        set_circle_design(self)
        reset_circle_val(self)
        setup_btn(self)
        #self.threadsniffing()
        global packet_lista
        packet_lista = []
        self.SNF = True

        ## Thread For Scan Network For Ip & Mac Address .
        #self.threadRunner2()
        #self.threadRunner()

        ## Thread For Test Speed Internet and get Donwload , Upload Sppeed In MB/S , and other info .
        #self.threadRunner3()
        #self.threadRunner4()
    
    def open_new_win(self):
        self.win = qtw.QMainWindow(MainWindow)
        self.ui = ui_main2
        self.ui.setupUi(self.win)
        self.win.show()

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

    def which_ip_to_ping(self,num_ip):
        time_ping = 0
        if num_ip == 1:
            ip = self.lineEdit_ip_main.text()
            ping_response = self.ping_ip(ip)
            if "Reply from" in ping_response and ip != "" and not "Destination host unreachable." in ping_response:
                self.label_ip1_ping_status.setStyleSheet(u"background-color: rgb(0, 255, 0);")
                ttl_index = ping_response.find("TTL=")
                ttl = ping_response[ttl_index+4:ttl_index+7].strip()
                time_index = ping_response.find("time=")
                time_index_end = ping_response.find("ms TTL")
                time_ping = ping_response[time_index+5:time_index_end]
            else:
                self.label_ip1_ping_status.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        if num_ip == 2:
            ip = self.lineEdit_ip2.text()
            ping_response = self.ping_ip(ip)
            if "Reply from" in ping_response and ip != "" and not "Destination host unreachable." in ping_response:
                self.label_ip2_ping_status.setStyleSheet(u"background-color: rgb(0, 255, 0);")
                ttl_index = ping_response.find("TTL=")
                ttl = ping_response[ttl_index+4:ttl_index+7].strip()
                time_index = ping_response.find("time=")
                time_index_end = ping_response.find("ms TTL")
                time_ping = ping_response[time_index+5:time_index_end]
            else:
                self.label_ip2_ping_status.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        if num_ip == 3:
            ip = self.lineEdit_ip3.text()
            ping_response = self.ping_ip(ip)
            if "Reply from" in ping_response and ip != "" and not "Destination host unreachable." in ping_response:
                self.label_ip3_ping_status.setStyleSheet(u"background-color: rgb(0, 255, 0);")
                ttl_index = ping_response.find("TTL=")
                ttl = ping_response[ttl_index+4:ttl_index+7].strip()
                time_index = ping_response.find("time=")
                time_index_end = ping_response.find("ms TTL")
                time_ping = ping_response[time_index+5:time_index_end]
            else:
                self.label_ip3_ping_status.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        if num_ip == 4:
            ip = self.lineEdit_ip4.text()
            ping_response = self.ping_ip(ip)
            if "Reply from" in ping_response and ip != "" and not "Destination host unreachable." in ping_response:
                self.label_ip4_ping_status.setStyleSheet(u"background-color: rgb(0, 255, 0);")
                ttl_index = ping_response.find("TTL=")
                ttl = ping_response[ttl_index+4:ttl_index+7].strip()
                time_index = ping_response.find("time=")
                time_index_end = ping_response.find("ms TTL")
                time_ping = ping_response[time_index+5:time_index_end]
            else:
                self.label_ip4_ping_status.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        if num_ip == 5:
            ip = self.lineEdit_ip5.text()
            ping_response = self.ping_ip(ip)
            if "Reply from" in ping_response and ip != "" and not "Destination host unreachable." in ping_response:
                self.label_ip5_ping_status.setStyleSheet(u"background-color: rgb(0, 255, 0);")
                ttl_index = ping_response.find("TTL=")
                ttl = ping_response[ttl_index+4:ttl_index+7].strip()
                time_index = ping_response.find("time=")
                time_index_end = ping_response.find("ms TTL")
                time_ping = ping_response[time_index+5:time_index_end]
            else:
                self.label_ip5_ping_status.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        return ip,time_ping
        #print(ip)

    def ping_for_rang_ip(self):
        range_ip = ['192.168.1.2','192.168.1.3','192.168.1.4']

    def second_thrd_scan_network(self):
        global ip_scanned 
        self.btn_thread.setText("Processing...")
        print("Start Scan")
        ip_scanned = scan_network("192.168.1.1/24")
        #print("Finish Scan")
        #print(ip_scanned)
        return ip_scanned
        
    def third_thrd_speed_test(self):
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
        time_choosed = 22
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
        
    def first_thread_result(self):
        #self.frame_2_circle_progres.rpb_setValue(100)
        print("First Thread Result")
    def second_thread_scan_result(self):
        # for row_num , row_info in ip_scanned.items():
        #     print(row_info)
        print(len(ip_scanned))
        ip_1 = ip_scanned[1]['IP']
        ip_2 = ip_scanned[2]['IP']
        ip_3 = ip_scanned[3]['IP']
        
        mac_1 = ip_scanned[1]['Mac']
        mac_2 = ip_scanned[2]['Mac']
        mac_3 = ip_scanned[3]['Mac']
        self.lineEdit_ip_host.setText(str(ip_1))
        self.lineEdit_ip_main.setText(str(ip_2))
        self.lineEdit_ip2.setText(str(ip_3))
        self.lineEdit_mac_host.setText(str(mac_1))
        self.lineEdit_mac_main.setText(str(mac_2))
        self.lineEdit_mac2.setText(str(mac_3))
    def third_thrd_speed_test_result(self):
        print("Third Thread Scan Result")
        
    def fourth_thrd_speed_test_result(self):
        print("Fourth Thread Speed Test Progress Result")

    def first_thread_finished(self):
        print("First Thread Scan finished")
        self.btn_thread.setText("Finished")

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
        
    def ping_ip(self,ip_to_ping):
        command = ['ping','-n','1',ip_to_ping]
        return subprocess.getoutput(command)

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
    # in this function we create our thread and run it
    def threadRunner(self):
        worker_1 = Worker(self.first_thread, num=1)# create our thread and give it a function as argument with its args
        worker_1.signals.result.connect(self.first_thread_result) # connect result signal of our thread to thread_result
        worker_1.signals.finished.connect(self.first_thread_finished) # connect finish signal of our thread to thread_complete
        self.threadpool.start(worker_1) # start thread

    def threadsniffing(self):
        worker = Worker(self.sniffer_start)
        worker.signals.result.connect(self.sniffer_results)
        self.threadpool.start(worker)
        
    def analyzer_sniff(self,pkt):
        print(pkt)
        packet_lista.append(pkt)
        
    def sniffer_start(self):
        print("Start Sniffer")
        while self.SNF == True:
            sc.sniff(iface="Ethernet",prn=self.analyzer_sniff,count=10)

    def sniffer_results(self):
        print("Start cap")

    def stop_snifer(self):
        self.SNF = False
        print(self.SNF)
        print("Stopped Sniff")
        print(len(packet_lista))
        print(packet_lista[-1])
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
        
def main():
    #widget_meters = AnalogGaugeWidget()
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    #engine = QQmlApplicationEngine()
    #engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))
    with open("front/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    main()