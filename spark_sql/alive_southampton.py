from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("AliveSouthampton") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Load data (same safe method)
df = spark.read.csv(
    "dataset/TitanicData.txt",
    header=False,
    inferSchema=True,
    quote='"',
    escape='"'
)

# Fix incorrect column count
df = df.select(df.columns[:12])

# Rename columns
df = df.toDF(
    "PassengerId", "Survived", "Pclass", "Name", "Sex",
    "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"
)

# Create SQL view
df.createOrReplaceTempView("titanic")

print("\n===== Task 2: Alive + Southampton =====")

# SQL Query
result = spark.sql("""
    SELECT 
        Pclass,
        COUNT(*) AS AliveCount
    FROM titanic
    WHERE Survived = 1 AND Embarked = 'S'
    GROUP BY Pclass
    ORDER BY Pclass
""")

result.show()

spark.stop()