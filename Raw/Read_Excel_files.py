# Databricks notebook source
# MAGIC %run /DeltaLake/Utilities/Common_Functions

# COMMAND ----------

try: import openpyxl
except ImportError:
    from pip._internal import main as pip
    pip(['install','openpyxl'])
    import openpyxl
    

# COMMAND ----------

df=spark.read.table('bronze.constructor')
schema_input=df.dtypes[0:-3]

# COMMAND ----------

from pyspark.sql.types import *
schema=StructType([
    StructField('constructorId',IntegerType(),True),
    StructField('constructorRef',StringType(),True),
    StructField('name',StringType(),True),
    StructField('nationality',StringType(),True),
    StructField('url',StringType(),True)
    ])

# COMMAND ----------

import openpyxl as xl
import pandas as pd
path=f_get_latest('/mnt/source_geekcoders_blob').replace('dbfs:','/dbfs')
sheet_excel=xl.load_workbook(f'{path}')
df_final=spark.createDataFrame([],schema)
for sheet_name in sheet_excel.sheetnames:
    df_excel=pd.read_excel(f'{path}',engine='openpyxl',sheet_name=f'{sheet_name}')
    df_temp=spark.createDataFrame(df_excel,schema)
    df_final=df_final.unionByName(df_temp)
df_final.cache()
f_validate_schema(df_final,schema_input)
df_final=f_add_input_file_name_loadtime(df_final,path.split('/')[-2].split('=')[1],path.split('/')[-1])
df_final.write.mode('overwrite').option("replaceWhere","date_part"==path.split('/')[-2].split('=')[1]).save('/mnt/bronze_geekcoders_gen2/constructor/')
df_final.unpersist()