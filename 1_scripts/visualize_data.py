from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import logging
from decouple import config

# Configure logging
log_file = "5_logs/visualize_data.log"
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

# Create SQLAlchemy engine
db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

def fetch_monthly_revenue():
    """Fetches monthly revenue from the database."""
    query = """
    SELECT DATE_TRUNC('month', tilauspäivä) AS month, SUM(kokonaissumma) AS total_revenue
    FROM tilaukset
    GROUP BY month
    ORDER BY month;
    """
    try:
        df = pd.read_sql_query(query, engine)
        logging.info("Fetched monthly revenue successfully.")
        return df
    except Exception as e:
        logging.error(f"Error fetching monthly revenue: {e}")
        return pd.DataFrame()

def fetch_customer_orders():
    """Fetches the number of orders per customer."""
    query = """
    SELECT asiakkaat.nimi AS customer_name, COUNT(tilaukset.tilaus_id) AS total_orders
    FROM tilaukset
    JOIN asiakkaat ON tilaukset.asiakas_id = asiakkaat.asiakas_id
    GROUP BY asiakkaat.nimi
    ORDER BY total_orders DESC
    LIMIT 10;
    """
    try:
        df = pd.read_sql_query(query, engine)
        logging.info("Fetched customer orders successfully.")
        return df
    except Exception as e:
        logging.error(f"Error fetching customer orders: {e}")
        return pd.DataFrame()

def plot_monthly_revenue(df):
    """Plots monthly revenue as a line chart."""
    if df.empty:
        logging.warning("No data to visualize for monthly revenue.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(df['month'], df['total_revenue'], marker='o', color='orange')
    plt.title("Kuukausittaiset tulot", fontsize=16)
    plt.xlabel("Kuukausi", fontsize=12)
    plt.ylabel("Tulot (€)", fontsize=12)
    plt.grid(visible=True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("3_results/monthly_revenue.png")
    plt.show()
    logging.info("Visualized monthly revenue successfully.")

def plot_customer_orders(df):
    """Plots the number of orders per customer as a bar chart."""
    if df.empty:
        logging.warning("No data to visualize for customer orders.")
        return

    plt.figure(figsize=(10, 6))
    plt.bar(df['customer_name'], df['total_orders'], color='lightgreen')
    for i, val in enumerate(df['total_orders']):
        plt.text(i, val + 0.2, str(val), ha='center', fontsize=10)
    plt.title("Top 10 asiakkaat tilausten määrällä", fontsize=16)
    plt.xlabel("Asiakas", fontsize=12)
    plt.ylabel("Tilausten määrä", fontsize=12)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.tight_layout()
    plt.savefig("3_results/customer_orders.png")
    plt.show()
    logging.info("Visualized customer orders successfully.")

if __name__ == "__main__":
    logging.info("Fetching and visualizing monthly revenue...")
    monthly_revenue_df = fetch_monthly_revenue()
    plot_monthly_revenue(monthly_revenue_df)

    logging.info("Fetching and visualizing customer orders...")
    customer_orders_df = fetch_customer_orders()
    plot_customer_orders(customer_orders_df)