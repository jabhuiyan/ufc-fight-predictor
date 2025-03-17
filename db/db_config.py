import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="ufc_db",
            user="postgres",
            password="your_password",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        raise
