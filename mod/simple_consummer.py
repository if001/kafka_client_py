import kafka

PORT="64688"
PORT="9092"
TOPIC='test01'
# IP="45.76.199.23"
IP="35.194.228.2"

def get_message(topic):
    print("get topic")
    # my-topic に対してデータを取りに行く
    consumer = kafka.KafkaConsumer(
        topic, group_id='my_group',
        bootstrap_servers=[str(IP)+':'+str(PORT)])
    return consumer


def show_message(consumer):
    print("print message")
    # メッセージの subscribe (for文をいきなり回せば勝手にリクエストしてくれる)
    for message in consumer:
        print("topic: %s message=%s" % (message.topic, message.value))


def main():
    kafka_client = kafka.KafkaClient(str(IP)+':'+str(PORT))
    # 送信用のクライアントを作成
    producer = kafka.SimpleProducer(kafka_client)

    # send_message(producer)
    consumer = get_message(TOPIC)
    show_message(consumer)


if __name__ == "__main__":
    main()
