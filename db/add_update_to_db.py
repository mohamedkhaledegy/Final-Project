from datetime import date
from my_models import Device , PingInfo

print("Start Creating .. ")

def create_dev():
    try:
        ip_1 = Device.create(
            ip_dev="192.168.1.1",
            mac_address="ac:64:62:78:87:64"
            )
        ip_1.save()
        print("Created")
    except Exception as err:
        print("Failed To Create Instance : ",err)

def edit_dev(ip_1):
    try:
        ip_1_get = Device.get(Device.ip_dev == ip_1)
        dev = ip_1_get
    except:
        ip_1_find_get = Device.select().where(Device.ip_dev == ip_1).get()
        dev = ip_1_find_get
    try:
        print("Start Edit .. ",dev.ip_dev)
        dev.name_dev = "mohamed"
        dev.save()
        print("Done Edit",dev.ip_dev,"Success")
    except Exception as err:
        dev = None
        print("Failed To Edit" , err)
    #return dev_edit

create_dev()
edit_dev("192.168.1.2")