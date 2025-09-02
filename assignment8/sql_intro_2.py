# task5
import pandas as pd
import sqlite3

try:
    # Connect to the lesson database
    conn = sqlite3.connect("../db/lesson.db")

    # SQL query to get line items with product info
    sql_query = """
    SELECT li.line_item_id, li.quantity, li.product_id, p.product_name, p.price
    FROM line_items li
    JOIN products p ON li.product_id = p.product_id
    """

    # Read data into DataFrame
    df = pd.read_sql_query(sql_query, conn)

    # Print first 5 lines
    print("First 5 lines of the DataFrame:")
    print(df.head())

    # Add total column
    df["total"] = df["quantity"] * df["price"]
    print("\nDataFrame with total column:")
    print(df.head())

    # Group by product and calculate summary statistics
    summary_df = (
        df.groupby("product_id")
        .agg({"line_item_id": "count", "total": "sum", "product_name": "first"})
        .rename(columns={"line_item_id": "order_count"})
    )

    print("\nSummary by product:")
    print(summary_df.head())

    # Sort by product name and save to CSV
    summary_df = summary_df.sort_values("product_name")
    summary_df.to_csv("order_summary.csv")
    print("\nSummary saved to order_summary.csv")

except Exception as e:
    print(f"Error: {e}")
finally:
    if conn:
        conn.close()
