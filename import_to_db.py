"""
Script: import_to_db.py
Author: Faijul Islam
Role: Data loading script — imports cleaned CSVs into MariaDB staging (retail_db)
Runs as: db_importer (scoped role — INSERT + CREATE only)
"""

from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

print(f"Running as DB user: {DB_USER}")

orders = pd.read_csv("data/cleaned_orders.csv")
details = pd.read_csv("data/cleaned_order_details.csv")
target = pd.read_csv("data/cleaned_sales_target.csv")

try:
    orders.to_sql('orders', engine, if_exists='replace', index=False)
    details.to_sql('order_details', engine, if_exists='replace', index=False)
    target.to_sql('sales_target', engine, if_exists='replace', index=False)
    print(f"✅ Data loaded into '{DB_NAME}' by '{DB_USER}'")
except Exception as e:
    print(f"❌ Error while loading (user: {DB_USER}):", e)
