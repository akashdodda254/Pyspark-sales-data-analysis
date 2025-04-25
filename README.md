# Pyspark-sales-data-analysis
PySpark Sales Data Analysis

This is a beginner-friendly PySpark project that performs simple data analysis on a sales dataset using Apache Spark with Python.

## Project Overview

- Read sales data from a CSV file
- Filter and transform the data
- Group by category and calculate total sales
- Save the final output in Parquet format

## Folder Structure

pyspark-sales-data-analysis/ ├── input/                # Input CSV files ├── output/               # Output Parquet files ├── main.py               # Main PySpark script ├── requirements.txt      # Python dependencies └── README.md             # Project documentation

## Sample Dataset Columns

- order_id  
- product  
- category  
- amount  
- order_date

## Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/YOUR_USERNAME/pyspark-sales-data-analysis.git
   cd pyspark-sales-data-analysis

2. Install dependencies

pip install -r requirements.txt


3. Place the CSV file in the input/ folder


4. Run the script

python main.py


5. Check the output in the output/ folder



Technologies Used

Python

PySpark

CSV and Parquet formats
