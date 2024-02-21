from pyspark.sql import SparkSession

def main(spark):
    print("HelloWorld")

if __name__ == "__main__":
    main(SparkSession.builder.getOrCreate())