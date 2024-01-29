# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.drivers
# MAGIC (
# MAGIC driverId integer
# MAGIC ,driverRef string
# MAGIC ,number string
# MAGIC ,code string
# MAGIC ,forename string
# MAGIC ,surname string
# MAGIC ,dob date
# MAGIC ,nationality string
# MAGIC ,url string
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC )
# MAGIC using DELTA
# MAGIC partitioned By(date_part)
# MAGIC location '/mnt/silver_geekcoders_gen2/drivers'