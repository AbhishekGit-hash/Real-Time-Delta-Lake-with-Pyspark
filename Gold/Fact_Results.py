# Databricks notebook source
df_race=spark.read.table('silver.race').coalesce(1)
df_result=spark.read.table('silver.results').coalesce(1)
df_drivers=spark.read.table('silver.drivers').coalesce(1)
df_teams=spark.read.table('silver.teams')

# COMMAND ----------

from pyspark.sql.functions import *
df_final=df_result.join(broadcast(df_race),df_result.raceId==df_race.raceId,how='inner').\
        join(df_drivers,df_result.driverId==df_drivers.driverId,how='inner').\
        select(df_result.raceId,df_drivers.driverId,df_race.circuitId,df_race.date,df_result.points,df_result.position)
df_final_agg=df_final.groupBy("raceId","driverId","circuitId","date").\
    agg(sum(col("points")).alias("total_points"),count(when(col("position")==1,True)).alias("total_wins"))
df_final_agg.write.mode('overwrite').save('/mnt/gold_geekcoders_gen2/fact_results')