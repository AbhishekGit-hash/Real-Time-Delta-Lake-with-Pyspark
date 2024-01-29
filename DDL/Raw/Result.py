# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS bronze.results
# MAGIC (
# MAGIC resultId bigint
# MAGIC ,raceId bigint
# MAGIC ,driverId bigint
# MAGIC ,constructorId bigint
# MAGIC ,number bigint
# MAGIC ,grid bigint
# MAGIC ,position bigint
# MAGIC ,positionText string
# MAGIC ,positionOrder bigint
# MAGIC ,points double
# MAGIC ,laps bigint
# MAGIC ,time string
# MAGIC ,milliseconds bigint
# MAGIC ,fastestLap bigint
# MAGIC ,rank bigint
# MAGIC ,fastestLapTime string
# MAGIC ,fastestLapSpeed double
# MAGIC ,statusId bigint
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC )
# MAGIC using DELTA
# MAGIC partitioned By(date_part)
# MAGIC location '/mnt/bronze_geekcoders_gen2/results'