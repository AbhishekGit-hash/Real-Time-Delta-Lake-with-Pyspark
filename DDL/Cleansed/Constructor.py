# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.constructor
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
# MAGIC location '/mnt/silver_geekcoders_gen2/constructor'