# Databricks notebook source
# MAGIC %run /DeltaLake/Utilities/Common_Functions

# COMMAND ----------

df=spark.read.table('bronze.laptimes')
schema_input=df.dtypes[0:-3]

# COMMAND ----------

from pyspark.sql.types import *
schema=StructType([StructField('raceId',IntegerType(),True),
                   StructField('driverId',IntegerType(),True),
                   StructField('lap',IntegerType(),True),
                   StructField('position',IntegerType(),True),
                   StructField('time',StringType(),True),
                   StructField('milliseconds',LongType(),True)])

# COMMAND ----------

path=f_get_latest_type2('/mnt/source_geekcoders_gen2/laptimes')
df_input=spark.read.format('csv').option("header",False).schema(schema).load(path[1]).cache()
f_validate_schema(df_input,schema_input)
df=f_add_input_file_name_loadtime(df_input,path[0].date(),path[1].split('/')[-1])
df.write.partitionBy("date_part").mode('overwrite').option("replaceWhere","date_part=='{0}'".format(path[0].date())).save('/mnt/bronze_geekcoders_gen2/laptimes/')
df.unpersist()