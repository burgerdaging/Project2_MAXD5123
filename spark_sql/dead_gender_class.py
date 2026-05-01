from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DeadByGenderClass") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Load data safely
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

print("\n===== Task 3: Dead by Gender and Class =====")

# SQL query
result = spark.sql("""
    SELECT 
        Pclass,
        Sex,
        COUNT(*) AS TotalDied
    FROM titanic
    WHERE Survived = 0
    GROUP BY Pclass, Sex
    ORDER BY Pclass, Sex
""")

result.show()

spark.stop()