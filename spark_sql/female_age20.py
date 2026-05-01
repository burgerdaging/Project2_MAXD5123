from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FemaleAge20") \
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

print("\n===== Task 4: Female Age ≤ 20 =====")

# SQL Query
result = spark.sql("""
    SELECT 
        COUNT(*) AS FemaleUnder20
    FROM titanic
    WHERE Sex = 'female'
      AND Age IS NOT NULL
      AND Age <= 20
""")

result.show()

spark.stop()