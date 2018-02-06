
import mod
#from mod import *
from Const import Const
import time


ZK1="45.76.48.245"
ZK2="35.194.228.2"
PORT="2181"


zk = mod.zookeeper.Zookeeper(ZK1, PORT)

zk_list = zk.get_broker_id_list()
print(zk_list)

zk.get_broker_list(zk_list)

zk.get_topic_detail("test12")

