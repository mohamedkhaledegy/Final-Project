import time

from PySide2.QtCore import Signal,QRunnable,QObject,Slot
#from .scan_network import scan_network 
#from .works import Worker ,Slot
import pyshark
from scapy import all as sc

def sniffer_start(self):
    print("Start Sniffer")
    while self.SNF == True:
        sc.sniff(iface="Ethernet",prn=self.analyzer_sniff,count=10)

def thrd_folder(self):
    cap = pyshark.LiveCapture(interface="Ethernet",output_file='mycapture.csv') # include_raw=True,
    packet_count = 0
    packet_http = 0
    try:
        while True:
            #cap.sniff()
            packet_list = []
            for packet in cap.sniff_continuously(packet_count=4):
                
                #if packet.haslayer(http.HTTPRequest):
                #    print("[+]HTTP Request >> " + get_url(pkt))
                #print("length:" , packet.length)
                #print("captured_length:" , packet.captured_length)
                #print("layers:" , packet.layers)
                #print("frame_info:" , packet.frame_info)
                    #print("transport_layer :",packet.transport_layer)
                    #print("highest_layer :",packet.highest_layer)
                    #print("ip :",packet.ip.addr)
                if packet.ip.src:
                    print(packet.ip.src)
                    #print(packet.ip.dst)
                #print("Layer :",dir(packet))
                packet_count += 1
                row_count = 0
                for row_pkt in packet:
                    row_count += 1
                    #print("row_pkt",row_pkt)
                
                ##
                url = None
                #print('Just arrived:',packet,
                #"Mac For Destination And Source",packet[0],
                #"Layer IP",packet[1],
                #"Layer TCP",packet[2],)
                packet_list.append(packet)
            return packet_list
            def print_callback(pkt):
                if len(pkt) > 0:
                    print("packet[0]")
                    print(pkt[0])
                    print("packet[1]")
                    print(pkt[1])
                print ('Just arrived:', pkt)
            
            #cap.apply_on_packets(print_callback, timeout=5)
    except KeyboardInterrupt:
        print("Finished Sniffer")
        print("hello")

def foo_thread(self, num):
    # some long processing
    self.btn_thread.setText("Processing...")
    global ip_scanned
    #ip_scanned = scan_network("192.168.1.1/24")
    #print(ip_scanned)
    for i in range(101):
        num += 1
        self.frame_1_cricle_progres.rpb_setValue(i)
        time.sleep(.1)
    return num
# we'll use this function when 'result' signal is emited
def thread_finished(self):
    print("Finished signal emited.")
    self.btn_thread.setText("Finished")
# in this function we create our thread and run it
def thread_result(self, s):
    print(ip_scanned[1]['IP'])
    ip_1 = ip_scanned[1]['IP']
    self.btn_resault.setText(str(ip_1))
    self.line_thread.setText(str(ip_1))
# in this function we create our thread and run it

def threadRunner(self):
    worker = Worker(self.foo_thread, num=1) # create our thread and give it a function as argument with its args
    worker2 = Worker(self.scan_network, num=1) # create our thread and give it a function as argument with its args
    worker.signals.result.connect(self.thread_result) # connect result signal of our thread to thread_result
    worker.signals.finished.connect(self.thread_finished) # connect finish signal of our thread to thread_complete
    self.threadpool.start(worker) # start thread