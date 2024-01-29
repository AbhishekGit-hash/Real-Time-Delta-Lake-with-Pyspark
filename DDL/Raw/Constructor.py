# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS bronze.constructor
# MAGIC (
# MAGIC constructorId integer
# MAGIC ,constructorRef string
# MAGIC ,name string
# MAGIC ,nationality string
# MAGIC ,url string
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC )
# MAGIC using DELTA
# MAGIC partitioned By(date_part)
# MAGIC location '/mnt/bronze_geekcoders_gen2/constructor'