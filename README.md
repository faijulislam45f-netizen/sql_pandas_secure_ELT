##                     Project Overview

```mermaid
flowchart TD
    %% Wireframe Black & White Styling
    classDef wireframe fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000;
    linkStyle default stroke:#000000,stroke-width:2px;

    A["<b>1. Raw CSV dataset</b><br><i>(Day 1 - source files: List of Orders.csv, Order Details.csv, Sales target.csv)</i>"]
    B["<b>2. Validate and clean</b><br><i>(Day 1 - drop blank rows, fix data types)</i>"]
    C["<b>3. MariaDB staging table</b><br><i>(Day 1 - load validated data into database)</i>"]
    D["<b>4. SQL layer</b><br><i>(Day 2 - CTEs and JOINs for aggregation)</i>"]
    E["<b>5. Pandas dataframe</b><br><i>(Day 3 - pull data via pd.read_sql())</i>"]
    F["<b>6. Plotly charts + CSV output</b><br><i>(Day 4 - final visualizations and summary files)</i>"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F

    class A,B,C,D,E,F wireframe;
