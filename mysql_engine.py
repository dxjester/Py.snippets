import mysql.connector
from sqlalchemy import create_engine

url = 'www.yourdomain.com'
host = 'localhost'
user_id = 'your_userid'
password = 'your_pw'
db_name = 'db_name'

mydb = mysql.connector.connect(
  host = url,
  user= user_id,
  passwd= password,
  database = db_name
)

print("Successfully connected!")
