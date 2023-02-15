
from kafka_utils import KafkaUtils

bootstrap_servers = 'localhost:9092'
kafka_utils = KafkaUtils(bootstrap_servers)
topic_name = 'user'
producer = kafka_utils.create_producer()
test = input("Enter a message: ")
producer.send(topic_name, test.encode('utf-8'))
producer.flush()
producer.close()

print("Message Sent")