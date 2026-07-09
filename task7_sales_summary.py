import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("sales_data.db")

# SQL query
query = """
SELECT
    product,
    SUM(quantity) AS Total_Quantity,
    SUM(quantity * price) AS Revenue
FROM sales
GROUP BY product
"""

# Load data into a DataFrame
df = pd.read_sql_query(query, conn)

# Display the result
print("Sales Summary:")
print(df)

# Create a bar chart
plt.figure(figsize=(8,5))
plt.bar(df["product"], df["Revenue"])

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

# Save the chart
plt.savefig("sales_chart.png")

# Show the chart
plt.show()

# Close database connection
conn.close()
