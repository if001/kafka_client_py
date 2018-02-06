import sys
from kafka import KafkaProducer
from time import sleep


class Sender():
    @staticmethod
    def init(kafka_servers):
        return KafkaProducer(bootstrap_servers=kafka_servers)


    @staticmethod
    def send_message(producer, topic, message):
        print("send " + message)
        producer.send(topic, message.encode())


def main():
    GUEST="45.32.21.73"
    PORT="9092"
    TOPIC="test03"

    host1 = GUEST + ':' + PORT

    # 送信用のクライアントを作成
    producer = KafkaProducer(bootstrap_servers=[host1])

    message = sys.argv[-1]
    while True:
        Sender.send_message(producer, TOPIC, message)
        sleep(1)

if __name__ == "__main__":
    main()
