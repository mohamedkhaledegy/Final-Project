from .my_models import Device ,PingInfo
from db.db_config import db_file_name

def get_one_dev():
    ip_1_find_get = Device.select().where(Device.ip_dev == '192.168.1.2').get()
    ip_1_get = Device.get(Device.ip_dev == '192.168.1.2')
    ### Get One 
    #print(ip_1_find_get)
    #print(ip_1_get.type_dev)
    #print(ip_1_get.ip_dev)
    #print(ip_1_get.name_dev)
    #print(ip_1_get.mac_address)
    #print(ip_1_get.is_local)
    #print(ip_1_get.os_info)

### Get List

def get_all_dev():
    # All
    ip_listaa = Device.select()
    return ip_listaa

def get_all_pings():
    # All
    ip_listaa = PingInfo.select()
    return ip_listaa