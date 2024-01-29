# Databricks notebook source
from pyspark.sql.functions import col,when,concat,lit
df=spark.read.table('silver.drivers')
df_final=df.select("*").\
    withColumn("full_name",concat(col("forename"),lit(" "),col("surname"))).\
    withColumn("number",when(col("number")=="\\N",None).otherwise(col("number")).cast("int")).\
    withColumn("code",when(col("code")=="\\N",None).otherwise(col("code"))).\
    drop("url","input_file_name","date_part","load_timestamp","forename","surname")
df_final.repartition(1).write.mode('overwrite').save('/mnt/gold_geekcoders_gen2/dim_driver')