#imprt libraries e init spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
print(spark)

#load data
df_device = spark.read.json("/Users/diegomendesbrasil/Library/CloudStorage/OneDrive-Personal/Projetos/DMB Data Analytics/git/dataeng/python-study-projects/Spark/files/device/device_2022_6_7_19_39_24.json")
#print df
df_device.show()
#print schema
df_device.printSchema()
#print columns
df_device.columns()
#
df_device.show()


df_device.select

