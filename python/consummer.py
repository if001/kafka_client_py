from kafka import KafkaConsumer
import sys
import argparse
from enum import Enum

PORT = "9092"
IP = "45.76.48.245"


class OffSet(Enum):
    latest = "latest"
    earlist = "earlist"

    @staticmethod
    def option(v):
        if v == "l":
            return OffSet.latest
        elif v == "e":
            return OffSet.earlist


class Consummer():
    def __init__(self, args):
        self.__group = args.group
        self.consumer = KafkaConsumer(args.topic,
                                      group_id=self.__group,
                                      bootstrap_servers=args.ip + ":" + args.port)
        # self.consumer = KafkaConsumer(args.topic, auto_offset_reset=OffSet.option(args.offset),
        #                               group_id=self.__group,
        #                               bootstrap_servers=args.ip + ":" + args.port)
        self.show_message()

    def show_message(self):
        print("show")
        if self.__group != None:
            self.consumer.commit()

        for message in self.consumer:
            print(self.__group)
            print("topic:%s  partition:%d  offset:%d key:%s value:%s" % (message.topic, message.partition,
                                                                         message.offset, message.key,
                                                                         message.value))


def main():
    parser = argparse.ArgumentParser(description='kafka-consummer')
    parser.add_argument('--port', '-p', default=PORT, type=str,
                        help='broker port ' + 'default ' + PORT)
    parser.add_argument('--ip', '-i', default=IP,
                        help='borker ip ' + 'default ' + IP)
    parser.add_argument('--topic', '-t', required=True, type=str,
                        help='topic')
    parser.add_argument('--group', '-g', default=None,
                        help='group id')
    parser.add_argument('--offset', '-o', default='l',
                        help='offset option\ l:latest\ e:earlist')
    args = parser.parse_args()

    Consummer(args)


if __name__ == "__main__":
    main()
