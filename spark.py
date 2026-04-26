from pyspark.sql import SparkSession

def create_spark():
    spark = SparkSession.builder \
        .appName("Football Big Data Project") \
        .master("local[*]") \
        .getOrCreate()

    return spark