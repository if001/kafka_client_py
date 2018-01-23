# import kafka
from kafka import KafkaConsumer


PORT="9092"
TOPIC='topic2'
IP1="45.32.21.73"
IP2="35.194.228.2"

class Getter():
    @staticmethod
    def init(kakfa_servers):
        return KafkaConsumer(TOPIC,bootstrap_servers=kakfa_servers)

    @staticmethod
    def show_message(consumer):
        print("show")
        for message in consumer:
            print("topic: %s message=%s" % (message.topic, message.value))


def main():
    host1 = IP1 + ':' + PORT
    host2 = IP2 + ':' + PORT
    consumer = KafkaConsumer(TOPIC,bootstrap_servers=[host1, host2])
    Getter.show_message(consumer)


if __name__ == "__main__":
    main()
