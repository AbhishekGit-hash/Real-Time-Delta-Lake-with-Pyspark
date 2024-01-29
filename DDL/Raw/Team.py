# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS bronze.teams
# MAGIC (
# MAGIC id long
# MAGIC ,name string
# MAGIC ,logo string
# MAGIC ,base string
# MAGIC ,first_team_entry long
# MAGIC ,world_championships long
# MAGIC ,position long
# MAGIC ,number long
# MAGIC ,pole_positions long
# MAGIC ,fastest_laps long
# MAGIC ,president string
# MAGIC ,director string
# MAGIC ,technical_manager string
# MAGIC ,chassis string
# MAGIC ,engine string
# MAGIC ,tyres string
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC )
# MAGIC using DELTA
# MAGIC partitioned By(date_part)
# MAGIC location '/mnt/bronze_geekcoders_gen2/teams'