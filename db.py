import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('DATABASE_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    database=os.getenv('DATABASE_NAME')
)

cursor = conn.cursor()