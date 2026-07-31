import sqlite3

# ----------------------------------------
# Database Connection
# ----------------------------------------

def get_connection():
    conn = sqlite3.connect("database.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


conn = get_connection()
cursor = conn.cursor()

# ----------------------------------------
# Users Table
# ----------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    role TEXT
)
""")

# ----------------------------------------
# Products Table
# ----------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    category TEXT,
    purchase_price REAL,
    selling_price REAL,
    stock REAL,
    unit TEXT
)
""")

# ----------------------------------------
# Sales Table
# ----------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    qty REAL,
    amount REAL,
    bill_date TEXT
)
""")
# ----------------------------------------
# Customer Table
# ----------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    mobile TEXT,
    address TEXT
)
""")

# ----------------------------------------
# Supplier Table
# ----------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS suppliers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT,
    mobile TEXT,
    address TEXT,
    gst TEXT
)
""")

# ----------------------------------------
# Default Admin User
# ----------------------------------------

cursor.execute("""
INSERT OR IGNORE INTO users(username,password,role)
VALUES ('admin','admin123','Owner')
""")

conn.commit()
