"""
Project 3 - SQL Data Analysis
DecodeLabs Internship

Loads the dataset into a real SQLite database and runs SQL queries
covering SELECT, WHERE, GROUP BY, HAVING, ORDER BY, and aggregations
(COUNT, SUM, AVG) -- the exact requirements from the brief.

Why SQLite: it's a real, standard SQL engine built into Python (no
server setup needed), so every query here is genuine SQL, not pandas
pretending to be SQL.
"""

import pandas as pd
import sqlite3

# ------------------------------------------------------------------
# 1. LOAD DATA INTO A REAL SQL DATABASE
# ------------------------------------------------------------------
df = pd.read_excel("Dataset_for_Data_Analytics__1_.xlsx")
conn = sqlite3.connect("orders.db")
df.to_sql("orders", conn, if_exists="replace", index=False)
cur = conn.cursor()
print(f"Loaded {len(df)} rows into the 'orders' table.\n")


def run_query(title, sql):
    """Run a query, print it, print the results."""
    print(f"--- {title} ---")
    print(sql.strip())
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    print(cols)
    for r in rows[:10]:
        print(r)
    if len(rows) > 10:
        print(f"... ({len(rows)} rows total)\n")
    else:
        print()
    return rows


# ------------------------------------------------------------------
# QUERY 1: Basic SELECT + WHERE + ORDER BY
# Business question: which delivered orders were worth over $2000?
# ------------------------------------------------------------------
run_query(
    "Q1: High-value delivered orders",
    """
    SELECT OrderID, Product, TotalPrice
    FROM orders
    WHERE OrderStatus = 'Delivered' AND TotalPrice > 2000
    ORDER BY TotalPrice DESC
    """,
)

# ------------------------------------------------------------------
# QUERY 2: GROUP BY + COUNT
# Business question: how many orders per product?
# ------------------------------------------------------------------
run_query(
    "Q2: Order count per product",
    """
    SELECT Product, COUNT(*) AS order_count
    FROM orders
    GROUP BY Product
    ORDER BY order_count DESC
    """,
)

# ------------------------------------------------------------------
# QUERY 3: GROUP BY + SUM + AVG (two aggregations at once)
# Business question: which product earns the most revenue,
# and what's the average order size for each?
# ------------------------------------------------------------------
run_query(
    "Q3: Revenue and avg order value per product",
    """
    SELECT Product,
           SUM(TotalPrice) AS total_revenue,
           ROUND(AVG(TotalPrice), 2) AS avg_order_value
    FROM orders
    GROUP BY Product
    ORDER BY total_revenue DESC
    """,
)

# ------------------------------------------------------------------
# QUERY 4: HAVING (filtering AFTER aggregation -- different from WHERE)
# Business question: which referral sources brought in more than
# 150 orders?
# ------------------------------------------------------------------
run_query(
    "Q4: Referral sources with more than 150 orders",
    """
    SELECT ReferralSource, COUNT(*) AS order_count
    FROM orders
    GROUP BY ReferralSource
    HAVING COUNT(*) > 150
    ORDER BY order_count DESC
    """,
)

# ------------------------------------------------------------------
# QUERY 5: WHERE + GROUP BY + AVG + COUNT together
# Business question: for delivered orders only, which payment method
# has the highest average order value?
# ------------------------------------------------------------------
run_query(
    "Q5: Avg order value by payment method (delivered only)",
    """
    SELECT PaymentMethod,
           ROUND(AVG(TotalPrice), 2) AS avg_value,
           COUNT(*) AS num_orders
    FROM orders
    WHERE OrderStatus = 'Delivered'
    GROUP BY PaymentMethod
    ORDER BY avg_value DESC
    """,
)

conn.close()
print("All queries executed successfully.")
