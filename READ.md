# This is Postgraduate Project 2 
# Group Members:-
# Abdul Rahman Auf Bin Azhar M152520014
# Nur Ain Athirah Binti Mohd Hanafi M152520013
# Nur Hani Binti Abdul Rani M152520016


# Big Data Processing — Titanic Dataset Analysis

A student project demonstrating Hadoop MapReduce and Apache Spark (Spark Core + Spark SQL) using the classic Titanic passenger dataset.

## 📊 Dataset
- **File:** `dataset/TitanicData.txt` (CSV-formatted, 891 rows)
- **Columns:** PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

## 🛠️ Environment
- **OS:** Windows 10/11
- **Python:** 3.10+
- **Java:** JDK 11
- **PySpark:** 3.5.1
- **Editor:** Visual Studio Code

> **Note:** This project simulates the Hadoop ecosystem on Windows. HDFS is represented by the local filesystem, and MapReduce is run via Python streaming pipes (`type | mapper | sort | reducer`). Spark runs in local mode (`local[*]`), using all CPU cores to mimic distributed processing. The logic is identical to a real cluster.

## 📦 Setup

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running the Tasks

### MapReduce: Total passengers per class
```cmd
run_mapreduce.bat
```

### Spark Core: Total passengers per gender
```cmd
python spark_core\gender_count.py
```

### Spark SQL: Four analytical queries
```cmd
python spark_sql\avg_fare_class.py
python spark_sql\alive_southampton.py
python spark_sql\dead_gender_class.py
python spark_sql\female_age20.py
```

## 📁 Project Structure