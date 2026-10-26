"""
Script: ingest.py
Author: Faijul Islam
Purpose: Load raw CSVs, validate, and clean the data
Output: Cleaned CSVs saved in data/ folder
"""

import pandas as pd

print("Loading raw CSV files...")

orders = pd.read_csv("data/List of Orders.csv")
details = pd.read_csv("data/Order Details.csv")
target = pd.read_csv("data/Sales target.csv")

# --- Validation ---
print("\nMissing values in orders:")
print(orders.isnull().sum())

print("\nDtypes before cleaning:")
print(orders.dtypes)

# --- Cleaning ---
orders_clean = orders.dropna()
orders_clean['Order Date'] = pd.to_datetime(orders_clean['Order Date'], format='%d-%m-%Y')

print(f"\nRows before: {len(orders)} | After cleaning: {len(orders_clean)}")

# --- Save cleaned versions ---
orders_clean.to_csv("data/cleaned_orders.csv", index=False)
details.to_csv("data/cleaned_order_details.csv", index=False)
target.to_csv("data/cleaned_sales_target.csv", index=False)

print("\nMissing values in orders:")
print(orders.isnull().sum())

print("\nMissing values in details:")
print(details.isnull().sum())

print("\nMissing values in target:")
print(target.isnull().sum())

print("\n✅ Cleaning complete. Cleaned files saved in data/")
