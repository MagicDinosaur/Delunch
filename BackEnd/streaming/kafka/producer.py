import random
import time
import json
from bson import json_util
from kafka_utils import KafkaUtils
from datetime import datetime
bootstrap_servers = 'localhost:9092'
kafka_utils = KafkaUtils(bootstrap_servers)
topic_name = 'user'

#delete topic if exists
if topic_name in kafka_utils.get_topics():
    kafka_utils.delete_kafka_topic(topic_name)
    print(f"Topic {topic_name} deleted")
producer = kafka_utils.create_producer()

data = {
    "id": None,
    # "name": None,
    # "count": None
}
while True:
    # test = datetime.now().strftime("%H:%M:%S")
    data["id"] = random.randint(1, 20)
    producer.send(topic_name, json.dumps(data, default=json_util.default).encode('utf-8'))
    time.sleep(5)
    response = {
        "message": "Message Sent",
        "data": data,
        "time": datetime.now().strftime("%H:%M:%S %Y-%m-%d")
    }
    print(response)

