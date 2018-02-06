
import mod
#from mod import *
from Const import Const
import time

PORT = Const.PORT
TOPIC = Const.TOPIC

kafka_servers = [Const.GCP + ":" + PORT]
kafka_servers = [Const.RANCHER_CLIENT3 + ":" + PORT]

print("server:"+ str(kafka_servers) + ", " + Const.TOPIC)
producer = mod.producer.Sender.init(kafka_servers)
cnt = 0
while(True):
    mod.producer.Sender.send_message(producer, TOPIC, str(cnt))
    time.sleep(3)
    cnt += 0.1
