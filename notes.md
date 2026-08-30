
# Project Notes — SQL & Pandas Retail Pipeline

┌────────────────────────────────────────────────────────────────────────┐
│ 1. Raw CSV dataset                                                     │
│    (Day 1 - source files: List of Orders.csv, Order Details.csv,       │
│     Sales target.csv)                                                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 2. Validate and clean                                                  │
│    (Day 1 - drop blank rows, fix data types)                           │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 3. MariaDB staging table                                               │
│    (Day 1 - load validated data into database)                         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 4. SQL layer                                                           │
│    (Day 2 - CTEs and JOINs for aggregation)                            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 5. Pandas dataframe                                                    │
│    (Day 3 - pull data via pd.read_sql())                               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 6. Plotly charts + CSV output                                          │
│    (Day 4 - final visualizations and summary files)                    │
└────────────────────────────────────────────────────────────────────────┘


## Dataset Source
- Kaggle: [https://www.kaggle.com/datasets/benroshan/ecommerce-data]
- Files: List of Orders.csv, Order Details.csv, Sales target.csv
- Known data quality issue: "List of Orders.csv" contains 60 fully-blank rows
  (will be dropped during the validation/cleaning step)

## Architecture
Raw CSV Dataset
       │
       ▼
MariaDB (Staging Table)
       │
       ▼  [SQL Layer: CTEs, JOINs, Aggregations via pd.read_sql()]
Pandas DataFrame
       │
       ▼  [Python Layer: Feature Engineering, Metrics & Formatting]
Plotly Charts (.png) + Summary CSV Output

## 5-Day Plan
- Day 1: Project setup, data ingestion, validation/cleaning
- Day 2: Advanced SQL querying (CTEs, JOINs) — analytics_queries.sql
- Day 3: Python-SQL integration (SQLAlchemy + pandas) — pipeline.py
- Day 4: Visualization export (Plotly charts)
- Day 5: end-to-end roll based DBMS secure pipeline[final project]

## Progress Log
- Day 0: Repo initialized, folder structure set up, requirements.txt generated

