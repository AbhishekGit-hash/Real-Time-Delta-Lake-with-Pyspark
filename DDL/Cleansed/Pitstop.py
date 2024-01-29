# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists silver.pitstop;
# MAGIC CREATE TABLE IF NOT EXISTS silver.pitstop
# MAGIC (
# MAGIC raceId integer
# MAGIC ,driverId integer
# MAGIC ,stop integer
# MAGIC ,lap integer
# MAGIC ,time timestamp
# MAGIC ,duration string
# MAGIC ,milliseconds integer
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC )
# MAGIC using DELTA
# MAGIC location '/mnt/silver_geekcoders_gen2/pitstop'