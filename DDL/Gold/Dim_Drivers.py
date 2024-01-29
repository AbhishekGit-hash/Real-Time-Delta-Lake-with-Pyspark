# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS gold.dim_driver
# MAGIC (
# MAGIC driverId integer
# MAGIC ,driverRef string
# MAGIC ,number integer
# MAGIC ,code string
# MAGIC ,dob date
# MAGIC ,nationality string
# MAGIC ,full_name string
# MAGIC )
# MAGIC using DELTA
# MAGIC location '/mnt/gold_geekcoders_gen2/dim_driver'