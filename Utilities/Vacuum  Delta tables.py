# Databricks notebook source
dbutils.widgets.text("tablename","")
tablename=dbutils.widgets.get("tablename")

# COMMAND ----------

spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled",False)

# COMMAND ----------

from delta.tables import DeltaTable
spark.sql("""use {0}""".format(tablename));
df=spark.sql("""Show tables""").select("tableName").collect()
list_tables=[i.tableName for i in df]
for tablename in list_tables:
    deltatable=DeltaTable.forName(spark,tablename)
    deltatable.vacuum(4)
    break