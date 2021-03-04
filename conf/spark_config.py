from pyspark.sql import SparkSession

from conf.constants import *


def spark_session():
    return SparkSession.builder.config("spark.jars", mssql_jar_path).master("local").appName("PySpark TEST").getOrCreate()