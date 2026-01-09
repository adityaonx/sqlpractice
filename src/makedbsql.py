import sqlite3
import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Setup Database
conn = sqlite3.connect("training.db")
cursor = conn.cursor()

# 2. Create Tables
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY, name TEXT, country TEXT, join_date DATE)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY, category TEXT, price REAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER, 
    quantity INTEGER, order_date DATE)''')

# 3. Generate Dummy Data
users = [(i, f"User_{i}", random.choice(['USA', 'IND', 'UK', 'CAN']), 
          (datetime.now() - timedelta(days=random.randint(0, 1000))).strftime('%Y-%m-%d')) 
         for i in range(1, 21)]

products = [(i, random.choice(['Electronics', 'Clothing', 'Home', 'Books']), 
             round(random.uniform(10, 500), 2)) for i in range(101, 121)]

orders = []
for i in range(1001, 1101):
    orders.append((i, random.randint(1, 20), random.randint(101, 120), 
                   random.randint(1, 5), 
                   (datetime.now() - timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d')))

# 4. Insert & Save
cursor.executemany("INSERT INTO Users VALUES (?,?,?,?)", users)
cursor.executemany("INSERT INTO Products VALUES (?,?,?)", products)
cursor.executemany("INSERT INTO Orders VALUES (?,?,?,?,?)", orders)

conn.commit()
print("✅ Database 'training.db' created with 100 orders!")
conn.close()