# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.teams
# MAGIC (
# MAGIC id integer
# MAGIC ,name string
# MAGIC ,logo string
# MAGIC ,base string
# MAGIC ,first_team_entry integer
# MAGIC ,world_championships integer
# MAGIC ,position integer
# MAGIC ,number integer
# MAGIC ,pole_positions integer
# MAGIC ,fastest_laps integer
# MAGIC ,president string
# MAGIC ,director string
# MAGIC ,technical_manager string
# MAGIC ,chassis string
# MAGIC ,engine string
# MAGIC ,tyres string
# MAGIC ,input_file_name string
# MAGIC ,date_part date
# MAGIC ,load_timestamp timestamp
# MAGIC  
# MAGIC )
# MAGIC using DELTA
# MAGIC location '/mnt/silver_geekcoders_gen2/teams'