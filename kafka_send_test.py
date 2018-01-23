
import mod
#from mod import *
from Const import Const
import time

PORT = Const.PORT
TOPIC = Const.TOPIC
IP1 = Const.IP1
IP2 = Const.IP2

kafka_servers = [IP1 + ":" + PORT,
                 IP2 + ":" + PORT]


consumer = mod.consummer.Getter.init(kafka_servers)
producer = mod.producer.Sender.init(kafka_servers)

while(True):
    mod.producer.Sender.send_message(producer, TOPIC, "test")
    time.sleep(1)

