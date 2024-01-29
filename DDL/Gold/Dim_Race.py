# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS gold.dim_race
# MAGIC (
# MAGIC raceId integer
# MAGIC ,round integer
# MAGIC ,circuitId integer
# MAGIC ,name string
# MAGIC ,time string
# MAGIC )
# MAGIC using DELTA
# MAGIC location '/mnt/gold_geekcoders_gen2/dim_race'