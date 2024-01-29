# Databricks notebook source
# MAGIC %run /DeltaLake/Utilities/Common_Functions

# COMMAND ----------

df=spark.read.table('bronze.results')
schema=df.dtypes[0:-3]

# COMMAND ----------

path=f_get_latest_type2('/mnt/source_geekcoders_gen2/results')
df_input=spark.read.format('parquet').load(path[1]).cache()
f_validate_schema(df_input,schema)
df=f_add_input_file_name_loadtime(df_input,path[0].date(),path[1].split('/')[-1])
df.write.partitionBy("date_part").mode('overwrite').option("replaceWhere","date_part=='{0}'".format(path[0].date())).save('/mnt/bronze_geekcoders_gen2/results/')
df_input.unpersist()