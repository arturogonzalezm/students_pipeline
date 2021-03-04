from conf.constants import csv_file, table_name
from conf.spark_config import spark_session
from db.connections import *
from etl.process import load

if __name__ == '__main__':
    load(csv_file)
    read_table = spark_session().read.jdbc(connection_mssql_string(), properties=connection_mssql_properties(), table=table_name)
    read_table.show(5, truncate=False)
    read_table.printSchema()

