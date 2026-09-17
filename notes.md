![Pipeline Architecture](asset/pipeline_diagram (1).png)


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

