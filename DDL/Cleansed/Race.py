# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.race
# MAGIC (
# MAGIC raceId integer
# MAGIC ,year integer
# MAGIC ,round integer
# MAGIC ,circuitId integer
# MAGIC ,name string
# MAGIC ,date date
# MAGIC ,time string
# MAGIC ,url string
# MAGIC ,fp1_date string
# MAGIC ,fp1_time string
# MAGIC ,fp2_date string
# MAGIC ,fp2_time string
# MAGIC ,fp3_date string
# MAGIC ,fp3_time string
# MAGIC ,quali_date string
# MAGIC ,quali_time string
# MAGIC ,sprint_date string
# MAGIC ,sprint_time string
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC )
# MAGIC using DELTA
# MAGIC partitioned By(date_part)
# MAGIC location '/mnt/silver_geekcoders_gen2/race'