from peewee import *
#from db.my_models import *
## Custom Import
from db.db_config import db
from db.my_models import Device , PingInfo #, PacketInfo
## Data Base
db_set = db
## Models To Create Table In DataBase
models_listaa = [Device,PingInfo]

def connect_create_table(db_choosed,models_choosed):
    print("Done")
    db = db_choosed
    db.connect()
    print("Connected")
    try:
        db.create_tables(models_choosed)
        print("Tables Created")
    except Exception as er:
        print("Error : " , er)
    finally:
        db.close()
        print("Connection Closed")

connect_create_table(db_choosed=db_set,models_choosed=models_listaa)