
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum

def main():
    # Step 1: Start Spark session
    spark = SparkSession.builder \
        .appName("Sales Data Analysis") \
        .getOrCreate()

    # Step 2: Read CSV file
    input_path = "input/sales_data.csv"
    sales_df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_path)

    # Step 3: Basic transformations
    # Group by 'category' and sum the 'amount'
    category_sales_df = sales_df.groupBy("category").agg(_sum("amount").alias("total_sales"))

    # Step 4: Write output to Parquet format
    output_path = "output/category_sales"
    category_sales_df.write.mode("overwrite").parquet(output_path)

    # Step 5: Stop Spark session
    spark.stop()

if __name__ == "__main__":
    main()
