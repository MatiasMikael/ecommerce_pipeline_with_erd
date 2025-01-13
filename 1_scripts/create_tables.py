import psycopg2
import logging
from decouple import config

# Configure logging
log_file = "5_logs/create_tables.log"
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

def create_tables():
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

        # SQL commands to create tables
        sql_commands = [
            """
            CREATE TABLE Asiakkaat (
                asiakas_id SERIAL PRIMARY KEY,
                nimi VARCHAR(100) NOT NULL,
                sähköposti VARCHAR(100) NOT NULL UNIQUE,
                puhelin VARCHAR(20),
                osoite TEXT,
                rekisteröitymispäivä TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """,
            """
            CREATE TABLE Tilaukset (
                tilaus_id SERIAL PRIMARY KEY,
                asiakas_id INT REFERENCES Asiakkaat(asiakas_id),
                tilauspäivä TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                kokonaissumma DECIMAL(10, 2)
            );
            """,
            """
            CREATE TABLE Tuotteet (
                tuote_id SERIAL PRIMARY KEY,
                nimi VARCHAR(100) NOT NULL,
                hinta DECIMAL(10, 2) NOT NULL,
                kategoria VARCHAR(50),
                varastosaldo INT DEFAULT 0
            );
            """,
            """
            CREATE TABLE TilauksenRivit (
                rivi_id SERIAL PRIMARY KEY,
                tilaus_id INT REFERENCES Tilaukset(tilaus_id),
                tuote_id INT REFERENCES Tuotteet(tuote_id),
                määrä INT NOT NULL,
                rivisumma DECIMAL(10, 2) NOT NULL
            );
            """,
            """
            CREATE TABLE Varasto (
                varasto_id SERIAL PRIMARY KEY,
                tuote_id INT REFERENCES Tuotteet(tuote_id),
                saatavilla INT DEFAULT 0,
                päivitetty TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        ]

        # Execute SQL commands
        for command in sql_commands:
            cursor.execute(command)
            logging.info(f"Executed: {command.strip()}")

        # Commit changes and close connection
        connection.commit()
        print("All tables created successfully.")
        logging.info("All tables created successfully.")
        connection.close()

    except Exception as e:
        print(f"Error creating tables: {e}")
        logging.error(f"Error creating tables: {e}")

if __name__ == "__main__":
    print("Creating tables...")
    logging.info("Starting table creation process.")
    create_tables()