# Databricks notebook source
# MAGIC %run /DeltaLake/Utilities/Common_Functions

# COMMAND ----------

df=spark.read.table('bronze.pitstop')
schema_input=df.dtypes[0:-3]

# COMMAND ----------

from pyspark.sql.types import *

schema = StructType(
    [
        StructField("raceId", IntegerType(), True),
        StructField("driverId", IntegerType(), True),
        StructField("stop", IntegerType(), True),
        StructField("lap", IntegerType(), True),
        StructField("time", TimestampType(), True),
        StructField("duration", StringType(), True),
        StructField("milliseconds", IntegerType(), True),
    ]
)

# COMMAND ----------

def f_write_delta(df,batchId):
    f_validate_schema(df,schema_input)
    df=f_add_input_file_name_loadtime(df,None,None)
    df.write.partitionBy("date_part").format('delta').mode("append").save("/mnt/bronze_geekcoders_gen2/pitstop/")

# COMMAND ----------

df=spark.readStream.format('csv').option('header',True).schema(schema).option('maxfilesperTrigger',1).load('/mnt/source_geekcoders_gen2/pitstop/')
df.writeStream.foreachBatch(f_write_delta).outputMode('append').start()

# COMMAND ----------

df=spark.read.format('csv').option('header',True).load('/mnt/source_geekcoders_gen2/pitstop/').withColumn("input_file_name",to_date(regexp_replace(regexp_extract(split(split(input_file_name(),'/')[4],'.csv')[0],r'([0-9]+_[0-9]+_[0-9]+)',1),'_','-')))
display(df)

# COMMAND ----------

from pyspark.sql.functions import *