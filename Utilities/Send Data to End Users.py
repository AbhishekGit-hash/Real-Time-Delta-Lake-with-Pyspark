# Databricks notebook source
import email,smtplib,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

sender_email="geekcoders9@gmail.com"
password=dbutils.secrets.get(scope = "geekcoders-deltalake", key = "gmail-password")
receiver_email="ssagarprajapati2212@gmail.com"
month=datetime.today().month
year=datetime.today().year
subject="Formula 1 result data {0} {1}".format(month,year)
body="Please find out formula 1 result data in CSV file attached in the email"
message=MIMEMultipart()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]=subject
message["Bcc"]=receiver_email

message.attach(MIMEText(body,'plain'))
# df=spark.sql("""select  b.full_name,total_points from gold.fact_results a inner join gold.dim_driver b on a.driverId=b.driverId  where year(date)=year(current_date()) and month(date)=month(current_date()) order by total_points desc limit 10""")
df=spark.sql("""select  b.full_name,total_points from gold.fact_results a inner join gold.dim_driver b on a.driverId=b.driverId  where year(date)=2022 and month(date)=08 order by total_points desc limit 10""")
df.toPandas().to_csv('/dbfs/FileStore/tables/race.csv',index=False)
with open('/dbfs/FileStore/tables/race.csv','rb') as attachment:
    part=MIMEBase("application","octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
file_name='race.csv'
part.add_header("Content-Disposition",f"attachment; filename={file_name}")
message.attach(part)
text=message.as_string()
context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,text)

# COMMAND ----------

# MAGIC %sql
# MAGIC select  b.full_name,total_points from gold.fact_results a inner join gold.dim_driver b on a.driverId=b.driverId  where year(date)=2022 and month(date)=08 order by total_points desc limit 10