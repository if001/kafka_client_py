
import mod
#from mod import *
from Const import Const
import time


zk_list = mod.zookeeper.Zookeeper.get_broker_id_list()
print(zk_list)

mod.zookeeper.Zookeeper.get_broker_list(zk_list)
print("end")
