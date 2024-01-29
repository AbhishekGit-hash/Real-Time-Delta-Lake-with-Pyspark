# Databricks notebook source
# MAGIC %sql
# MAGIC create database if not exists silver;

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists bronze;

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists gold;

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists gold_vw;