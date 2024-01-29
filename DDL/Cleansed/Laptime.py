# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.laptimes
# MAGIC (
# MAGIC
# MAGIC raceId integer
# MAGIC ,driverId integer
# MAGIC ,lap integer
# MAGIC ,position integer
# MAGIC ,time string
# MAGIC ,milliseconds long
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC  
# MAGIC )
# MAGIC using DELTA
# MAGIC location '/mnt/silver_geekcoders_gen2/laptimes'