# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS gold.dim_circuits
# MAGIC (
# MAGIC circuitId integer
# MAGIC ,circuitRef string
# MAGIC ,name string
# MAGIC ,location string
# MAGIC ,country string
# MAGIC ,alt string
# MAGIC )
# MAGIC using DELTA
# MAGIC location '/mnt/gold_geekcoders_gen2/dim_circuits'