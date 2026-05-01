from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("AvgFarePerClass") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv(
    "dataset/TitanicData.txt",
    header=False,
    inferSchema=True,
    quote='"',
    escape='"'
)

print("Column count:", len(df.columns))
print(df.columns)

# ✅ FIX: Force correct number of columns
df = df.select(df.columns[:12])

# Rename properly
df = df.toDF(
    "PassengerId", "Survived", "Pclass", "Name", "Sex",
    "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"
)

df.createOrReplaceTempView("titanic")

print("\n===== Task 1: Average Fare per Class =====")

result = spark.sql("""
    SELECT 
        Pclass, 
        ROUND(AVG(Fare), 2) AS AverageFare
    FROM titanic
    GROUP BY Pclass
    ORDER BY Pclass
""")

result.show()

spark.stop()