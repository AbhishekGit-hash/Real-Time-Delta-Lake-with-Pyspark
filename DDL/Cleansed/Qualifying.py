# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.qualifying
# MAGIC (
# MAGIC qualifyId integer
# MAGIC ,raceId integer
# MAGIC ,driverId integer
# MAGIC ,constructorId integer
# MAGIC ,number integer
# MAGIC ,position integer
# MAGIC ,q1 string
# MAGIC ,q2 string
# MAGIC ,q3 string
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC )
# MAGIC using DELTA
# MAGIC partitioned By(date_part)
# MAGIC location '/mnt/silver_geekcoders_gen2/qualifying'