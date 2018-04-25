
import mod
from Const import Const
import time


ZK1 = "45.76.48.245"
PORT = "2181"


def get_info(zk, topic):
    zk_list = zk.get_broker_id_list()
    print(zk_list)
    zk.get_broker_list(zk_list)
    zk.get_topic_detail(topic)


zk1 = mod.zookeeper.Zookeeper(ZK1, PORT)
get_info(zk1, "lb-replica")

