from kafka_utils import KafkaUtils
import sys
bootstrap_servers = "localhost:9092"
topic_name = "user"
group_id = "user-1"
consumer = KafkaUtils(bootstrap_servers).create_consumer(topic_name)

# Consume messages from Kafka
print(consumer)
for message in consumer:
    # print(message)
    print(f"Received message: {message.value}")
sys.exit()