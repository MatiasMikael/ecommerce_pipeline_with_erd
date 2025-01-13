import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from decouple import config
import logging
from datetime import datetime

# Configure logging

log_file = "5_logs/test_connection.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load database credentials from .env
db_name = config("DB_NAME")
db_user = config("DB_USER")
db_password = config("DB_PASSWORD")
db_host = config("DB_HOST")
db_port = config("DB_PORT")

def create_database():
    try:
        # Connect to PostgreSQL server
        connection = psycopg2.connect(
            dbname="postgres",  # Connect to the default database
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # Allow CREATE DATABASE to bypass transaction restrictions
        cursor = connection.cursor()

        # Create database
        cursor.execute(f"CREATE DATABASE {db_name};")
        print(f"Database '{db_name}' created successfully.")
        logging.info(f"Database '{db_name}' created successfully.")
        connection.close()
    except psycopg2.errors.DuplicateDatabase:
        print(f"Database '{db_name}' already exists.")
        logging.warning(f"Database '{db_name}' already exists.")
    except Exception as e:
        print(f"Error creating database: {e}")
        logging.error(f"Error creating database: {e}")

if __name__ == "__main__":
    print("Creating database...")
    logging.info("Starting database creation process.")
    create_database()