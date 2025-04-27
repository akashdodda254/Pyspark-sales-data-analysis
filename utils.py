
from pyspark.sql import DataFrame

def display_schema(df: DataFrame):
    """Prints the schema of the DataFrame"""
    df.printSchema()

def show_sample_data(df: DataFrame, num_rows: int = 5):
    """Displays a few rows from the DataFrame"""
    df.show(num_rows)
