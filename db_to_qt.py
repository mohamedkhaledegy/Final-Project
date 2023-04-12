import time
## Import Threads Functions
from threads_custom.works import Worker
from threads_custom.test_speed import *

## Import Database Models
from db.my_models import Device,PingInfo
## Import Database Functions
from db.retrieve_from_db import *

def config_data_base(self):
    worker_1 = Worker(collect_database_info)# create our thread and give it a function as argument with its args
    worker_1.signals.result.connect(config_data_base_resault)
    worker_1.signals.finished.connect(self.config_database_finish)
    #self.all_devs = all_devs
    self.threadpool.start(worker_1)

def collect_database_info():
    #time.sleep(5)
    global all_devs
    global all_pings
    all_devs = None
    all_pings = None
    all_devs = get_all_dev()
    all_pings = get_all_pings()
    return all_devs , all_pings

def config_data_base_resault():
    global devss
    global pingss
    devss = all_devs
    pingss = all_pings
    print("Database Configed Success")
    #print("all Devs",all_devs)
    return devss , pingss