
import mod
from Const import Const


PORT = Const.PORT
TOPIC = Const.TOPIC
IP1 = Const.IP1
IP2 = Const.IP2

kafka_servers = [IP1 + ":" + PORT]
# kafka_servers = [IP1 + ":" + PORT,
#                  IP2 + ":" + PORT]

consumer = mod.consummer.Getter.init(kafka_servers)
producer = mod.producer.Sender.init(kafka_servers)

mod.consummer.Getter.show_message(consumer)

