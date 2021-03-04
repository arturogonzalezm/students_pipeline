from conf.constants import table_name
from conf.spark_config import spark_session, csv_file
from db.connections import *


def extract(data):
    return spark_session().read.csv(data, header=True, inferSchema=True)


def transform(data):
    renamed_df = extract(data=data).toDF(*(c.replace(' ', '_') for c in extract(data=data).columns))
    return renamed_df.toDF(*[c.lower() for c in renamed_df.columns])


def load(data):
    return transform(data=data).write.jdbc(connection_mssql_string(), properties=connection_mssql_properties(),
                                           table=table_name, mode="overwrite")
