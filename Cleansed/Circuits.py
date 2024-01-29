# Databricks notebook source
# MAGIC %run /DeltaLake/Utilities/Common_Functions

# COMMAND ----------

f_merge("/mnt/bronze_geekcoders_gen2/circuits","silver.circuits")