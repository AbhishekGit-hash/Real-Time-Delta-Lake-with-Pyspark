# Databricks notebook source
dbutils.widgets.text("tablename","")
tablename=dbutils.widgets.get("tablename")

# COMMAND ----------

# MAGIC %run /DeltaLake/Utilities/Common_Functions

# COMMAND ----------

f_merge(f"/mnt/bronze_geekcoders_gen2/{tablename}",f"silver.{tablename}")