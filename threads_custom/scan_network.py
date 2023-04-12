import time
from scapy.all import ARP, Ether, srp

#target_ip = None
# try:
#     target_ip = input("Enter Ip Host ( Empty = 192.168.1.1 ) : ")
# except:
#     pass
# try:
#     timeout_scan_input = input("Enter Seconds of Time out : ")
# except:
#     pass
# if not "192" in target_ip:
#     target_ip = "192.168.1.1/24"

#print("Host IP > ",target_ip)

# IP Address for the destination
def scan_network(target_ip_to_scan,timeout_scan_input=None):
    if not "192" in target_ip_to_scan:
        target_ip_to_scan = "192.168.1.1/24"
    # create ARP packet
    arp = ARP(pdst=target_ip_to_scan)
    # create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # stack them
    packet = ether/arp
    # لو المستخدم ادخل قيمة timeout
    strt_tim = time.process_time()
    if timeout_scan_input:
        ## لو القيمة اكبر من 0 واقل من دقيقتين
        if 10 > len(timeout_scan_input) > 0:
            result = srp(packet,timeout=timeout_scan_input)[0]
        else:
            result = srp(packet,timeout=10)[0]
    else:
        result = srp(packet,timeout=10)[0]
    
    end_tim = time.process_time()
    expnded = end_tim - strt_tim
    print(expnded)
    # a list of clients, we will fill this in the upcoming loop
    clients = []
    for sent, received in result:
        # for each response, append ip and mac address to `clients` list
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    # print clients
    print("Available devices in the network:",len(clients))
    
    #print("IP" + " "*18+"MAC")
    global dict_ip_scaned
    dict_ip_scaned = {}
    ip_counter_scaned = 0
    for client in clients:
        ip_counter_scaned += 1
        #print( "IP:","{:16} Mac Address :{}".format(client['ip'], client['mac']))
        dict_ip_scaned[ip_counter_scaned] = {
            "IP":str(client['ip']),
            "Mac":str(client['mac']) }
    return dict_ip_scaned

#scan_network("192.168.1.1",0)