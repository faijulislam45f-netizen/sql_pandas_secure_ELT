# 🚀 Retail Sales & Target Analytics Pipeline

A production-ready retail data analytics and ETL pipeline built with **Python, Pandas, and Plotly**. This project demonstrates end-to-end data processing, key performance indicator (KPI) tracking, and automated interactive dashboard generation for sales target performance analysis.

---

## 📊 Executive Summary & Key Metrics

* **Total Revenue:** ₹4,31,502.00
* **Total Profit:** ₹23,955.00
* **Overall Profit Margin:** 5.55%
* **Total Unique Orders:** 500 orders (1,500 line items)

---

## 📈 Interactive EDA Dashboard Preview

> **Note:** GitHub does not render interactive HTML files natively. You can view the live interactive Plotly report directly by clicking here: 
> 👉 **[View Live Interactive Dashboard](https://htmlpreview.github.io/?https://github.com/faijulislam45f-netizen/sql_pandas_secure_ELT/blob/main/eda_dashboard.html)**

<img src="./Screenshot 2026-10-26 7.42.23 PM.png" alt="Retail Sales & Target Analytics Dashboard" width="100%">

### 🔍 Business Insights & Key Findings:
1. **Category Performance:** **Electronics** leads in total revenue (₹1.65L), whereas **Clothing** generates the highest profit (₹11.16K). **Furniture** maintains high sales volume but suffers from compressed profit margins (1.81%).
2. **Regional Drivers:** **Madhya Pradesh** (₹1.05L) and **Maharashtra** (₹95.3K) serve as the primary revenue engines, contributing to over 46% of total revenue.
3. **Target vs. Actual Gap:** Sales performance against targets varies significantly by month and category, highlighting critical seasonal demand shifts and stock allocation requirements.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Data Engineering & Analysis:** Pandas, NumPy
* **Data Visualization:** Plotly Express, Plotly Graph Objects
* **Version Control:** Git & GitHub

---

## 📁 Repository Structure

```text
├── data/
│   ├── cleaned_orders.csv
│   ├── cleaned_order_details.csv
│   └── cleaned_sales_target.csv
├── eda_dashboard.py         # Main script for data processing & dashboard generation
├── eda_dashboard.html       # Standalone interactive Plotly HTML dashboard
├── dashboard_preview.png    # Dashboard preview image for documentation
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
