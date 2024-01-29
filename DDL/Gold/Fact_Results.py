# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS gold.fact_results
# MAGIC (
# MAGIC raceId integer
# MAGIC ,driverId integer
# MAGIC ,circuitId integer
# MAGIC ,date date
# MAGIC ,total_points double
# MAGIC ,total_wins long
# MAGIC )
# MAGIC using DELTA
# MAGIC location '/mnt/gold_geekcoders_gen2/fact_results'