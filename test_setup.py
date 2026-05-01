"""
Test to verify Spark + dataset are working.
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SetupTest") \
    .master("local[*]")\
    .getOrCreate()

spark.sparkContext.setLogLevel("Error")

#Read the .txt file as CSV (.txt extension)
df = spark.read.csv("dataset/TitanicData.txt", header = True, inferSchema=True)

print(f"\n Total Rows: {df.count()}" )
print(f" Total Columns: {df.columns}\n" )
df.show(3)

spark.stop()