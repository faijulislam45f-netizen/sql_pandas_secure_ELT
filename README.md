graph TD
    %% Styling definitions for minimalist black & white wireframe look
    classDef wireframe fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000;
    linkStyle default stroke:#000000,stroke-width:2px;

    1("<b>1. Raw CSV dataset</b><br/><small>(Day 1 - source files: List of Orders.csv, Order Details.csv, Sales target.csv)</small>")
    2("<b>2. Validate and clean</b><br/><small>(Day 1 - drop blank rows, fix data types)</small>")
    3("<b>3. MariaDB staging table</b><br/><small>(Day 1 - load validated data into database)</small>")
    4("<b>4. SQL layer</b><br/><small>(Day 2 - CTEs and JOINs for aggregation)</small>")
    5("<b>5. Pandas dataframe</b><br/><small>(Day 3 - pull data via pd.read_sql())</small>")
    6("<b>6. Plotly charts + CSV output</b><br/><small>(Day 4 - final visualizations and summary files)</small>")

    1 --> 2
    2 --> 3
    3 --> 4
    4 --> 5
    5 --> 6

    class 1,2,3,4,5,6 wireframe;
