# import kafka
from kafka import KafkaConsumer


PORT="9092"
TOPIC='test03'

IP1="45.32.21.73" #vultr1
IP2="35.194.228.2" #gcp
IP3="45.77.180.225" #vultr2


class Getter():
    @staticmethod
    def init(kakfa_servers, topic):
        return KafkaConsumer(topic, auto_offset_reset='earliest', bootstrap_servers=kakfa_servers)
        # return KafkaConsumer(topic, auto_offset_reset='latest', bootstrap_servers=kakfa_servers)

    @staticmethod
    def show_message(consumer):
        print("show")
        for message in consumer:
            print ("topic:%s  partition:%d  offset:%d key:%s value:%s" % (message.topic, message.partition,
                                                  message.offset, message.key,
                                                  message.value))


def main():
    host = IP1 + ':' + PORT
    consumer = KafkaConsumer(TOPIC,bootstrap_servers=[host])
    Getter.show_message(consumer)

if __name__ == "__main__":
    main()
