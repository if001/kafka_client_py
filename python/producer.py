
from kafka import KafkaProducer
from time import sleep
import sys
import argparse

LB = "45.76.48.245"

class Producer():
    def __init__(self, args):
        self.__topic = args.topic
        self.producer = KafkaProducer(
            bootstrap_servers=args.ip + ":" + args.port)

    def send_message(self, message):
        print("topic " + self.__topic + "   send " + message)
        # producer.send(topic, value=message.encode(), partition=3)
        self.producer.send(self.__topic, value=message.encode())

    def auto_send(self):
        cnt = 0
        while True:
            self.send_message(str(cnt))
            cnt += 1
            sleep(1)


def main():
    parser = argparse.ArgumentParser(description='kafka-consummer')
    parser.add_argument('--port', '-p', default='9092', type=str,
                        help='broker port')
    parser.add_argument('--ip', '-i', default=LB,
                        help='borker ip')
    parser.add_argument('--topic', '-t', required=True, type=str,
                        help='topic')
    parser.add_argument('--message', '-m', default=None,
                        help='if not set, send number that auto incremented as a message')

    args = parser.parse_args()

    producer = Producer(args)

    if args.message == None:
        producer.auto_send()
    else:
        producer.send_message(args.message)


if __name__ == "__main__":
    main()
