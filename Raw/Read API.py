# Databricks notebook source
# MAGIC %run /DeltaLake/Utilities/Common_Functions

# COMMAND ----------

df=spark.read.table('bronze.teams')
schema_input=df.dtypes[0:-3]

# COMMAND ----------

import requests
from datetime import datetime
from pyspark.sql.functions import col
headers = {
    'x-rapidapi-host': f_get_secret('api-host'),
    'x-rapidapi-key': f_get_secret('api-key')
    }
response=requests.get('https://v1.formula-1.api-sports.io/teams',headers=headers)
data=response.json()['response']
data_list=[]
columns=['id', 'name', 'logo', 'base', 'first_team_entry', 'world_championships','position','number', 'pole_positions', 'fastest_laps', 'president', 'director', 'technical_manager', 'chassis', 'engine', 'tyres']
for response in data:
    data_list.append((response['id'],response['name'],response['logo'],response['base'],response['first_team_entry'],response['world_championships'],response['highest_race_finish']['position'],response['highest_race_finish']['number'],response['pole_positions'],response['fastest_laps'],response['president'],response['director'],response['technical_manager'],response['chassis'],response['engine'],response['tyres']))

df=spark.createDataFrame(data_list,schema=columns).cache()
no_files=f_validate_schema(df,schema_input)
df=f_add_input_file_name_loadtime(df,datetime.today().date(),"https://v1.formula-1.api-sports.io/teams'")
df.repartition(no_files).write.mode('overwrite').option("replaceWhere","date_part='{0}'".format(datetime.today().date())).save('/mnt/bronze_geekcoders_gen2/teams/')
df.unpersist()