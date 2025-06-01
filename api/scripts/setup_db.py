import mysql.connector
from mysql.connector import Error
import sys
import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import time

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings

def wait_for_mysql(max_retries=30, retry_interval=1):
    """Wait for MySQL to be ready."""
    print("Waiting for MySQL to be ready...")
    for i in range(max_retries):
        try:
            engine = create_engine(settings.DATABASE_URL)
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("MySQL is ready!")
            return True
        except SQLAlchemyError as e:
            if i < max_retries - 1:
                print(f"MySQL not ready yet, retrying in {retry_interval} seconds... ({i+1}/{max_retries})")
                time.sleep(retry_interval)
            else:
                print("Failed to connect to MySQL after maximum retries")
                return False

def verify_connection():
    """Verify database connection using SQLAlchemy."""
    try:
        engine = create_engine(settings.DATABASE_URL)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("Database connection verified successfully!")
        return True
    except SQLAlchemyError as e:
        print(f"Error verifying database connection: {e}")
        return False

def setup_database():
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="password"  # Match the MYSQL_ROOT_PASSWORD in docker-compose
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.DATABASE_URL.split('/')[-1]}")

            # Create user if it doesn't exist
            cursor.execute("CREATE USER IF NOT EXISTS 'alphasort'@'%' IDENTIFIED BY 'alphasort_password'")

            # Grant privileges
            cursor.execute(f"GRANT ALL PRIVILEGES ON {settings.DATABASE_URL.split('/')[-1]}.* TO 'alphasort'@'%'")
            cursor.execute("FLUSH PRIVILEGES")

            print("Database setup completed successfully!")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    if wait_for_mysql():
        verify_connection()
    setup_database()
