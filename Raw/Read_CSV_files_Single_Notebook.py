# Databricks notebook source
# MAGIC %run /DeltaLake/Utilities/Common_Functions

# COMMAND ----------

dbutils.widgets.text("tablename","")
tablename=dbutils.widgets.get("tablename")

# COMMAND ----------

from pyspark.sql.types import *

# COMMAND ----------

df=spark.read.table(f'bronze.{tablename}')
schema=df.dtypes[0:-3]

# COMMAND ----------

path=f_get_latest_type2(f'/mnt/source_geekcoders_gen2/{tablename}')
df_input=spark.read.format('csv').option("header",True).option("inferschema",True).load(path[1]).cache()
f_validate_schema(df_input,schema)
df=f_add_input_file_name_loadtime(df_input,path[0].date(),path[1].split('/')[-1])
df.write.partitionBy("date_part").mode('overwrite').option("replaceWhere","date_part=='{0}'".format(path[0].date())).save(f'/mnt/bronze_geekcoders_gen2/{tablename}/')
df_input.unpersist()

# COMMAND ----------

df=spark.read.table('bronze.drivers')
schema=df.dtypes[0:-3]

# COMMAND ----------

path=f_get_latest_type2('/mnt/source_geekcoders_gen2/drivers')
df_input=spark.read.format('csv').option("header",True).option("inferschema",True).load(path[1]).cache()
f_validate_schema(df_input,schema)
df=f_add_input_file_name_loadtime(df_input,path[0].date(),path[1].split('/')[-1])
df.write.partitionBy("date_part").mode('overwrite').option("replaceWhere","date_part=='{0}'".format(path[0].date())).save('/mnt/bronze_geekcoders_gen2/drivers/')
df_input.unpersist()

# COMMAND ----------

df=spark.read.table('bronze.race')
schema=df.dtypes[0:-3]

# COMMAND ----------

path=f_get_latest_type2('/mnt/source_geekcoders_gen2/race')
df_input=spark.read.format('csv').option("header",True).option("inferschema",True).load(path[1]).cache()
f_validate_schema(df_input,schema)
df=f_add_input_file_name_loadtime(df_input,path[0].date(),path[1].split('/')[-1])
df.write.partitionBy("date_part").mode('overwrite').option("replaceWhere","date_part=='{0}'".format(path[0].date())).save('/mnt/bronze_geekcoders_gen2/race/')
df_input.unpersist()