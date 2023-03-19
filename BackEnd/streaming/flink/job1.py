from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


#create spark session
spark = SparkSession.builder.appName("Kafka-Streaming").getOrCreate()

#kafka configuration
kafka_server = "localhost:9092"
kafka_topic = "user"