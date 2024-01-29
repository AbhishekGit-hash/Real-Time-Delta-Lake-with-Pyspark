# Databricks notebook source
# MAGIC %run /DeltaLake/Utilities/Common_Functions

# COMMAND ----------

# MAGIC %py
# MAGIC configs = {"fs.azure.account.auth.type": "OAuth",
# MAGIC           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
# MAGIC           "fs.azure.account.oauth2.client.id": f_get_secret(key = "client-id"),
# MAGIC           "fs.azure.account.oauth2.client.secret":  f_get_secret(key = "client-secret"),
# MAGIC           "fs.azure.account.oauth2.client.endpoint":  f_get_secret(key = "tenantid")}
# MAGIC #Optionally, you can add <directory-name> to the source URI of your mount point.
# MAGIC mountPoint="/mnt/source_geekcoders_gen2/"
# MAGIC if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
# MAGIC   dbutils.fs.mount(
# MAGIC     source =  f_get_secret(key = "source-geekcoders-gen2"),
# MAGIC     mount_point = mountPoint,
# MAGIC     extra_configs = configs)

# COMMAND ----------

mountPoint='/mnt/source_geekcoders_blob'
if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
   dbutils.fs.mount(
   source = f_get_secret('source-geekcoders-blob'),
   mount_point = mountPoint,
   extra_configs = {f_get_secret('source-geekcoders-blob-config'): f_get_secret('source-geekcoders-blob-accesskey')})

# COMMAND ----------

# MAGIC %py
# MAGIC """
# MAGIC creating mount point for sink-datalake gen2
# MAGIC """
# MAGIC #Optionally, you can add <directory-name> to the source URI of your mount point.
# MAGIC mountPoint="/mnt/bronze_geekcoders_gen2/"
# MAGIC if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
# MAGIC   dbutils.fs.mount(
# MAGIC     source =  f_get_secret(key = "bronze-geekcoders-gen2"),
# MAGIC     mount_point = mountPoint,
# MAGIC     extra_configs = configs)

# COMMAND ----------

# MAGIC %py
# MAGIC """
# MAGIC creating mount point for sink-datalake gen2
# MAGIC """
# MAGIC #Optionally, you can add <directory-name> to the source URI of your mount point.
# MAGIC mountPoint="/mnt/silver_geekcoders_gen2/"
# MAGIC if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
# MAGIC   dbutils.fs.mount(
# MAGIC     source =  f_get_secret(key = "silver-geekcoders-gen2"),
# MAGIC     mount_point = mountPoint,
# MAGIC     extra_configs = configs)

# COMMAND ----------

# MAGIC %py
# MAGIC """
# MAGIC creating mount point for sink-datalake gen2
# MAGIC """
# MAGIC #Optionally, you can add <directory-name> to the source URI of your mount point.
# MAGIC mountPoint="/mnt/gold_geekcoders_gen2/"
# MAGIC if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
# MAGIC   dbutils.fs.mount(
# MAGIC     source =  f_get_secret(key = "gold-geekcoders-gen2"),
# MAGIC     mount_point = mountPoint,
# MAGIC     extra_configs = configs)