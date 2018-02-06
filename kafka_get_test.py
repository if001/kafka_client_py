import mod
from Const import Const

PORT = Const.PORT

kafka_servers = [Const.RANCHER_CLIENT2 + ":" + PORT]

print("server:" + str(kafka_servers) + ", " + Const.TOPIC)

consumer = mod.consummer.Getter.init(kafka_servers, Const.TOPIC)
mod.consummer.Getter.show_message(consumer)

