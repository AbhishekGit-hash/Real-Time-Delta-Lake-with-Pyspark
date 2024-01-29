# Databricks notebook source
# MAGIC %run /DeltaLake/Utilities/Common_Functions

# COMMAND ----------

jdbc_url=f_get_secret('source-sql-jdbc')
username=f_get_secret('source-sql-user')
password=f_get_secret('source-sql-password')

# COMMAND ----------

df=spark.read.table('bronze.qualifying')
schema=df.dtypes[0:-3]

# COMMAND ----------

from datetime import datetime
df_qualifying = (spark.read
  .format("jdbc")
  .option("url", jdbc_url)
  .option("dbtable", "dbo.qualifying")
  .option("user", username)
  .option("password", password)
  .load()
).cache()
f_validate_schema(df_qualifying,schema)
df_qualifying=f_add_input_file_name_loadtime(df_qualifying,datetime.today().date(),"dbo.qualifying")
df_qualifying.write.partitionBy("date_part").mode('overwrite').option("replaceWhere","date_part=='{0}'".format(datetime.today().date())).save('/mnt/bronze_geekcoders_gen2/qualifying/')
df_qualifying.unpersist()