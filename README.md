# Task 7 - Basic Sales Summary using SQLite and Python

## 📌 Objective

The objective of this project is to connect Python with an SQLite database, execute SQL queries to summarize sales data, and visualize the results using a bar chart.

---

## 🛠 Tools Used

- Python 3.x
- SQLite3
- Pandas
- Matplotlib
- VS Code

---

## 📂 Project Structure

```
Task7_SQLite_Sales_Summary/
│── create_database.py
│── task7_sales_summary.py
│── sales_data.db
│── sales_chart.png
│── requirements.txt
│── README.md
└── screenshots/
```

---

## 📊 Database

The SQLite database contains one table named **sales** with the following columns:

- id
- product
- quantity
- price

---

## 📝 SQL Query Used

```sql
SELECT
    product,
    SUM(quantity) AS Total_Quantity,
    SUM(quantity * price) AS Revenue
FROM sales
GROUP BY product;
```

---

## 📈 Output

The program displays:

- Total Quantity Sold
- Revenue by Product

It also generates a bar chart named:

```
sales_chart.png
```

---

## 📚 Learning Outcomes

- Connected Python with SQLite database
- Executed SQL queries inside Python
- Imported SQL data using Pandas
- Visualized data using Matplotlib
- Created a simple sales summary report

---

## 👨‍💻 Author

**Manas Aswal**

B.Tech Information Technology
