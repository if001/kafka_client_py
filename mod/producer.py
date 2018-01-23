import sys
from kafka import KafkaProducer
from time import sleep

from Const import Const

PORT = Const.PORT
TOPIC = Const.TOPIC
IP1 = Const.IP1
IP2 = Const.IP2

class Sender():
    @staticmethod
    def init(kafka_servers):
        return KafkaProducer(bootstrap_servers=kafka_servers)


    @staticmethod
    def send_message(producer, topic, message):
        print("send " + message)
        producer.send(topic, message.encode())


def main():
    host1 = IP1 + ':' + PORT
    host2 = IP2 + ':' + PORT

    # 送信用のクライアントを作成
    producer = KafkaProducer(bootstrap_servers=[host1, host2])

    message = sys.argv[-1]
    while True:
        Sender.send_message(producer, TOPIC, message)
        sleep(1)

if __name__ == "__main__":
    main()
