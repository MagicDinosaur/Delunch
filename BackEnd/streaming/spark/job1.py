from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


#create spark session
spark = SparkSession.builder.appName("Kafka-Increase-Counter").getOrCreate()
#kafka configuration
kafka_server = "localhost:9092"
kafka_topic = "user"
#schema for the data
message_schema = StructType([
    StructField("id", IntegerType()),
    # StructField("name", StringType()),
    # StructField("count", IntegerType()),
])
#read data from kafka–––
# df = spark.readStream.format("kafka")\
#     .option("kafka.bootstrap.servers", kafka_server)\
#     .option("subscribe", kafka_topic)\
#     .option("startingOffsets", "earliest")\
#     .load()
# print("+++++++++++++++++++++++++++++++++++")
# df.printSchema()

# #Parse the Kafka message as Json
# df = df.selectExpr("CAST(value AS STRING)") \
#     .select(from_json(col("value"), message_schema).alias("message")) \
#     .select("message.*")\
#     .withColumn("count", col("count").cast(IntegerType()))

#increase the count by 1

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
"""
Option 1: Write to csv file !!! NEED TO FIX TO WRITE INTO A SINGLE FILE
"""
def write_to_csv(df):
    df = df.withColumn("count", col("count") + 1)
    final_df = df.select("id", "name", "count").repartition(1)
    output_file = "output/"
    query = final_df.writeStream \
        .format("csv") \
        .trigger(processingTime="10 seconds") \
        .option("path", output_file) \
        .option("checkpointLocation", "checkpoint/") \
        .option("header", "true") \
        .outputMode("append") \
        .start().awaitTermination()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
"""
Option 2: Write process data into database. update the field count of user table
"""
def write_to_db():
    """
    function to update processed kafka data into database
    """
    sqlite_path = "/Users/apple/Projects/Delunch/BackEnd/database.db"
    sqlite_table = "view_count"
    # Increase the "count" field by 1
    df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", kafka_server) \
        .option("subscribe", kafka_topic) \
        .option("startingOffsets", "earliest") \
        .load()
    df = df.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col("value"), message_schema).alias("message")) \
        .select("message.*") \
        .withColumn("id", col("id").cast(IntegerType()))

    # Define the update query to update the SQLite table
    update_query = """
        UPDATE {table}
        SET count = count + 1
        WHERE id = ?
    """.format(table=sqlite_table)
    # read = process = write
    # Write the processed data to SQLite
    query = df.writeStream \
        .outputMode("update") \
        .foreachBatch(lambda batch_df, batch_id: batch_df.foreachPartition(
        lambda partition: update_sqlite(partition, sqlite_path, update_query)
    )) \
        .start()

    # Wait for the query to terminate
    query.awaitTermination()

    # Function to update SQLite table
import sqlite3

def update_sqlite(partition, db_path, query):
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)

    # Execute update query for each row in the partition
    for row in partition:
        id_value = row.id
        cursor = conn.cursor()
        cursor.execute(query, (id_value,))
        conn.commit()

    # Close the database connection
    conn.close()
write_to_db()

#kafka configuration