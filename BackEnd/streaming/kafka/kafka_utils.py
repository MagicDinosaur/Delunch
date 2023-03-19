from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
import json
class KafkaUtils:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
    def get_topics(self):
        admin_client = KafkaAdminClient(
            bootstrap_servers=self.bootstrap_servers,
        )
        return admin_client.list_topics()

    def create_topic(self, topic_name, num_partitions, replication_factor):
        admin_client = KafkaAdminClient(
            bootstrap_servers=[self.bootstrap_servers],
        )

        topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
        admin_client.create_topics(new_topics=topic, validate_only=False)

    def create_producer(self):
        return KafkaProducer(bootstrap_servers=[self.bootstrap_servers])

    def create_consumer(self, topic_name):
        return KafkaConsumer(
            topic_name,
            bootstrap_servers=[self.bootstrap_servers],
            auto_offset_reset='earliest',

            enable_auto_commit=False,
            group_id='user-1',
          )
    def delete_kafka_topic(self, topic_name):
        admin_client = KafkaAdminClient(
            bootstrap_servers=self.bootstrap_servers,
            client_id='delete-topic-client'
        )
        admin_client.delete_topics([topic_name])
