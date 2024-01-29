# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.results
# MAGIC (
# MAGIC resultId integer
# MAGIC ,raceId integer
# MAGIC ,driverId integer
# MAGIC ,constructorId integer
# MAGIC ,number integer
# MAGIC ,grid integer
# MAGIC ,position integer
# MAGIC ,positionText string
# MAGIC ,positionOrder integer
# MAGIC ,points double
# MAGIC ,laps integer
# MAGIC ,time string
# MAGIC ,milliseconds integer
# MAGIC ,fastestLap integer
# MAGIC ,rank integer
# MAGIC ,fastestLapTime string
# MAGIC ,fastestLapSpeed double
# MAGIC ,statusId integer
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC  
# MAGIC )
# MAGIC using DELTA
# MAGIC location '/mnt/silver_geekcoders_gen2/results'