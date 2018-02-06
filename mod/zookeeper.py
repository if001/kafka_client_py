import kazoo, json
from kazoo.client import KazooClient
from kazoo.client import KazooState

def my_listener(state):
    if state == KazooState.LOST:
        print("Connection Lost")
    elif state == KazooState.SUSPENDED:
        print("SUPENDED")
    else:
        print("Connected")

def deb_print(message, json_data):
    print(message)
    print("{}".format(json.dumps(json_data,indent=4)))

        
class Zookeeper():
    def __init__(self, ip, port):
        self.IP = ip
        self.zk = KazooClient(hosts=self.IP+":"+port,  read_only=True)
        self.zk.start()
        self.zk.add_listener(my_listener)


    def get_broker_id_list(self):
        # broker idの一覧取得
        return self.zk.get_children('/brokers/ids')


    def get_broker_list(self, brokers_id_list):
        # broker一覧の表示
        for broker_id in brokers_id_list:
            broker, stat = self.zk.get('/brokers/ids/' + broker_id)
            broker = json.loads(broker.decode('utf-8'))
            deb_print("broker " + str(broker_id), broker)

    
    def get_topic_detail(self, topic, partitions=0):
        res, stat = self.zk.get("/brokers/topics/"+ topic + "/partitions/" + str(partitions) + "/state")
        res = json.loads(res.decode('utf-8'))
        deb_print("topic " + topic+" detail", res)

