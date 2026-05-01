import os
import sys

# Fix Python path for Spark workers
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from pyspark.sql import SparkSession

print(">>> Starting Spark Core task...")

spark = SparkSession.builder \
    .appName("GenderCount") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print(">>> [1] Spark Session created")

# Fix file path
base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "dataset", "TitanicData.txt")

# Read CSV safely using Spark
df = spark.read.csv(file_path, header=False, inferSchema=True)

print(">>> [2] DataFrame loaded")

# Column index reference:
# Column 5 = Sex → index 4
df = df.withColumnRenamed("_c4", "Sex")

# Group by gender
result = df.groupBy("Sex").count()

print(">>> [3] Computing results...")

result.show()

spark.stop()

print(">>> Done! ✅")