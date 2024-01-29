# Databricks notebook source
def f_get_secret(key):
    try:
       return dbutils.secrets.get(scope = "geekcoders-deltalake", key = f"{key}")
    except Exception as err:
        print("Error Occured", str(err))
    

# COMMAND ----------

def f_get_primary_key(df):
    try:
        import mack as mk
        primary_key=mk.find_composite_key_candidates(df)
        merge_condition=" "
        for i in range(len(primary_key)):
            if(i==len(primary_key)-1):
                merge_condition+="tgt."+primary_key[i]+"=src."+primary_key[i]
            else:
                merge_condition+="tgt."+primary_key[i]+"=src."+primary_key[i]+" AND "
        return (merge_condition)
    except Exception as err:
        print("Error occured ",str(err))

# COMMAND ----------

from datetime import datetime
def f_get_latest_type3(path:str):
    try:
        list_file_path=[(i.path,i.name.split('=')[1].replace('/','')) for i in dbutils.fs.ls(f'{path}') if (i.name!='_delta_log/')]
        list_file_path.sort(key=lambda x:datetime.strptime(x[1],"%Y-%m-%d"),reverse=True)
        return (list_file_path[0][0])
    except Exception as err:
        print("Error occured", str(err))

# COMMAND ----------

from datetime import datetime
def f_get_latest(path:str):
    try:
        list_file_path=[(i.path,i.name.split('=')[1].replace('/','')) for i in dbutils.fs.ls(f'{path}')]
        list_file_path.sort(key=lambda x:datetime.strptime(x[1],"%Y-%m-%d"),reverse=True)
        return dbutils.fs.ls(list_file_path[0][0])[0][0]
    except Exception as err:
        print("Error occured", str(err))

# COMMAND ----------

def f_add_input_file_name_loadtime(df,date_part=None,file_name=None):
    from pyspark.sql.functions import input_file_name,split,current_timestamp,lit,to_date
    if(file_name is None and date_part is None):
        df_final=df.select("*").\
            withColumn("input_file_name",split(input_file_name(),'/')[4]).\
            withColumn("date_part",to_date(regexp_replace(regexp_extract(split(split(input_file_name(),'/')[4],'.csv')[0],r'([0-9]+_[0-9]+_[0-9]+)',1),'_','-'))).\
            withColumn("load_timestamp",current_timestamp())
    elif(file_name is None):
        df_final=df.select("*").\
            withColumn("input_file_name",split(input_file_name(),'/')[4]).\
            withColumn("date_part",lit(date_part)).\
            withColumnRenamed("date_part",to_date(date_part)).\
            withColumn("load_timestamp",current_timestamp())
    else:
        df_final=df.select("*").\
            withColumn("input_file_name",lit(file_name)).\
            withColumn("date_part",to_date(lit(date_part))).\
            withColumn("load_timestamp",current_timestamp())
    return df_final

# COMMAND ----------

from pyspark.sql.types import *
def f_validate_schema(df,sink_schema):
    no_rows=df.count()
    if(no_rows<=100000):
       no_files=1
    elif(no_rows>100000 and no_rows<=1000000):
       no_files=3
    elif(no_rows>1000000 and no_rows<=10000000):
       no_files=5
    source_schema=df.limit(1).dtypes
    if(source_schema==sink_schema):
        return no_files
    else:
        raise Exception("Schema is not matched")

# COMMAND ----------

def f_get_latest_type2(source_path):
    from datetime import datetime
    list_datepart=[]
    for i in dbutils.fs.ls(f'{source_path}'):
        list_datepart.append((datetime.strptime(i.name.split('.')[0][-10:].replace('_','-'),"%Y-%m-%d"),i.path))
    list_datepart.sort(key=lambda x:x[0],reverse=True)
    return(list_datepart[0])
    

# COMMAND ----------

from delta.tables import DeltaTable
def f_merge(source_path,target_table):
    path=f_get_latest_type3(source_path)
    df_staging=spark.read.format('delta').load(f'{path}')
    merge_condition=f_get_primary_key(df_staging)
    deltaTable=DeltaTable.forName(spark,f'{target_table}')
    deltaTable.alias('tgt').\
        merge(df_staging.alias('src'),f'{merge_condition}').\
            whenMatchedUpdateAll().\
            whenNotMatchedInsertAll().\
            execute()