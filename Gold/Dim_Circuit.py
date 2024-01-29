# Databricks notebook source
from pyspark.sql.functions import col,when,concat,lit
df=spark.read.table('silver.circuits')
df=df.select("circuitId","circuitRef","name","location","country","alt")
df_final=df.select([when(col(i)=='\\N',None).otherwise(col(i)).alias(i) for i in df.columns])
df_final.repartition(1).write.mode('overwrite').save('/mnt/gold_geekcoders_gen2/dim_circuits')