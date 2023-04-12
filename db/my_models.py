import datetime
from peewee import *

## Custom Import
try:
    from db.db_config import db
except:
    from db_config import db
## Base Model ( Inherit to My Models With Same Config To Database )
class BaseModel(Model):
    class Meta:
        database = db

## Model For All Ip Collected With Mac addr as Uniqu
class Device(BaseModel):
    type_dev = CharField(null=True,choices=("Host","Master","Local","Global","Website"))
    is_local = BooleanField(default=True)
    ip_dev = CharField(null=True,max_length=15)
    mac_address = CharField(null=True,unique=True)
    name_dev = CharField(null=True)
    os_info = CharField(null=True)

class PingInfo(BaseModel):
    owner = ForeignKeyField(Device, backref='owner_ip',null=True)
    is_anwsred = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    details = TextField(null=True)