import psycopg2
import logging
import random
from faker import Faker
from decouple import config

# Configure logging
log_file = "5_logs/generate_data.log"
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

# Faker instance for generating fake data
fake = Faker()

def generate_data():
    connection = None
    try:
        # Connect to the database
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = connection.cursor()

        # Generate data for asiakkaat
        logging.info("Generating data for asiakkaat...")
        inserted_ids = []
        for _ in range(200):  # Generate 200 customers
            cursor.execute("""
                INSERT INTO asiakkaat (nimi, sähköposti, puhelin, osoite, rekisteröitymispäivä)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING asiakas_id
            """, (fake.name(), fake.email(), fake.phone_number()[:20], fake.address(), fake.date_this_decade()))
            asiakas_id = cursor.fetchone()[0]
            inserted_ids.append(asiakas_id)
            logging.info(f"Added asiakas ID: {asiakas_id}")
        connection.commit()
        logging.info(f"Committed data for asiakkaat. Inserted IDs: {inserted_ids}")

        # Debugging: Fetch and log all customers
        cursor.execute("SELECT * FROM asiakkaat")
        all_customers = cursor.fetchall()
        logging.info(f"All customers in table: {all_customers}")

        # Generate data for tilaukset
        logging.info("Generating data for tilaukset...")
        for _ in range(500):
            asiakas_id = random.choice(inserted_ids)  # Ensure valid asiakas_id
            cursor.execute("""
                INSERT INTO tilaukset (asiakas_id, tilauspäivä, kokonaissumma)
                VALUES (%s, %s, %s)
            """, (asiakas_id, fake.date_this_decade(), round(random.uniform(50, 2000), 2)))
            logging.info(f"Added tilaus for asiakas ID: {asiakas_id}")
        connection.commit()
        logging.info("Committed data for tilaukset.")

        # Continue with other tables (tuotteet, tilauksenrivit, varasto)

        print("Data generation completed successfully.")
        logging.info("Data generation completed successfully.")

    except Exception as e:
        print(f"Error generating data: {e}")
        logging.error(f"Error generating data: {e}")
    finally:
        if connection:
            connection.close()
            logging.info("Database connection closed.")

if __name__ == "__main__":
    print("Generating data...")
    logging.info("Starting data generation process.")
    generate_data()