# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.circuits
# MAGIC (
# MAGIC circuitId integer
# MAGIC ,circuitRef string
# MAGIC ,name string
# MAGIC ,location string
# MAGIC ,country string
# MAGIC ,lat double
# MAGIC ,lng double
# MAGIC ,alt string
# MAGIC ,url string
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC  
# MAGIC )
# MAGIC using DELTA
# MAGIC location '/mnt/silver_geekcoders_gen2/circuits'