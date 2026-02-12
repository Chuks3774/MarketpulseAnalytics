import os
from pyspark.sql.types import StructType, StructField, StringType

checkpoint_dir = "/tmp/checkpoint/kafka_to_postgres"

postgres_user = os.getenv("POSTGRES_USER", "admin")
postgres_password = os.getenv("POSTGRES_PASSWORD", "admin")

postgres_config = {
    "url": "jdbc:postgresql://postgres:5432/stock_data",
    "user": postgres_user,
    "password": postgres_password,
    "dbtable": "stocks",
    "driver": "org.postgresql.Driver",
}

kafka_data_schema = StructType([
    StructField("date", StringType(), True),
    StructField("high", StringType(), True),
    StructField("low", StringType(), True),
    StructField("open", StringType(), True),
    StructField("close", StringType(), True),
    StructField("symbol", StringType(), True),
])
