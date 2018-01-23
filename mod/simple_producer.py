import kafka
import sys


PORT="64688"
PORT="9092"
TOPIC='test01'
# IP="45.76.199.23"
IP="35.194.228.2"

def send_message(producer, topic, message):
    print("send " + message)
    producer.send_messages(topic, message.encode())

def main():
    # 送信用のクライアントを作成
    kafka_client = kafka.KafkaClient(str(IP)+':'+str(PORT))
    producer = kafka.SimpleProducer(kafka_client)

    message = sys.argv[-1]
    send_message(producer, TOPIC, message)

if __name__ == "__main__":
    main()
