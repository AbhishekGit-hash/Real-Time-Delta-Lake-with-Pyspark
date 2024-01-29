# Databricks notebook source
spark.sql(""" use gold """)
df=spark.sql("""Show tables""").collect()
table_names=[i.tableName for i in df]

# COMMAND ----------

for tablename in table_names:
    spark.sql("""create or replace  view gold_vw.{0}
          as
          select * from gold.{0}""".format(tablename))