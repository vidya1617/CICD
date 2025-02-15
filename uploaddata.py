import boto3
import pymysql
import pandas as pd
import io

s3_client = boto3.client('s3')

BUCKET_NAME = "bucket-for-csvdata"
FILE_NAME = "sample_data.csv"

RDS_HOST = "terraform-20250215093813330500000001.cbikoukme5wo.ap-southeast-1.rds.amazonaws.com"
RDS_USER = "admin"
RDS_PASS = "Vidya2004"
RDS_DB = "rdsdb"

def get_csv_from_s3():
    try:
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=FILE_NAME)
        csv_content = response['Body'].read().decode('utf-8')
        df = pd.read_csv(io.StringIO(csv_content))

        df.columns = ["name", "age", "city"]

        return df
    except Exception as e:
        print(f"Error fetching CSV: {e}")
        return None
        
def insert_into_rds(data):
    try:
        conn = pymysql.connect(host=RDS_HOST, user=RDS_USER, password=RDS_PASS, database=RDS_DB)
        cursor = conn.cursor()

        insert_query = "INSERT INTO file_data (name, age, city) VALUES (%s, %s, %s)"

        records = data.to_records(index=False)
        values = [tuple(row) for row in records]

        cursor.executemany(insert_query, values)
        conn.commit()
        print("Data inserted successfully.")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error inserting data: {e}")
        
if __name__ == "__main__":
    print("Fetching CSV from S3...")
    data = get_csv_from_s3()

    if data is not None:
        print("Inserting data into RDS...")
        insert_into_rds(data)
    else:
        print("No data to insert.")