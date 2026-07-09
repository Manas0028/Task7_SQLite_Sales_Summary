import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Sample sales data
sales_data = [
    ("Laptop", 3, 50000),
    ("Laptop", 2, 50000),
    ("Mouse", 10, 500),
    ("Mouse", 5, 500),
    ("Keyboard", 7, 1200),
    ("Keyboard", 3, 1200),
    ("Monitor", 4, 15000),
    ("Monitor", 2, 15000),
    ("Printer", 2, 8000),
    ("Printer", 1, 8000)
]

# Insert data into table
cursor.executemany(
    "INSERT INTO sales(product, quantity, price) VALUES (?, ?, ?)",
    sales_data
)

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database created successfully!")


