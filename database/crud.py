from database.database import get_connection

conn = get_connection()
cursor = conn.cursor()

# =====================================
# PRODUCTS
# =====================================

def add_product(name, category, purchase, selling, stock, unit):

    cursor.execute("""
        INSERT INTO products
        (
            product_name,
            category,
            purchase_price,
            selling_price,
            stock,
            unit
        )
        VALUES (?,?,?,?,?,?)
    """, (
        name,
        category,
        purchase,
        selling,
        stock,
        unit
    ))

    conn.commit()


def get_products():

    cursor.execute("""
        SELECT *
        FROM products
        ORDER BY product_name
    """)

    return cursor.fetchall()


def delete_product(product_id):

    cursor.execute(
        "DELETE FROM products WHERE id=?",
        (product_id,)
    )

    conn.commit()


# =====================================
# DASHBOARD FUNCTIONS
# =====================================

def total_products():

    cursor.execute("SELECT COUNT(*) FROM products")

    return cursor.fetchone()[0]


def total_stock():

    cursor.execute("SELECT COALESCE(SUM(stock),0) FROM products")

    return cursor.fetchone()[0]
# =====================================
# CUSTOMER FUNCTIONS
# =====================================

def add_customer(name, mobile, address):

    cursor.execute("""
    INSERT INTO customers
    (customer_name,mobile,address)
    VALUES (?,?,?)
    """,(name,mobile,address))

    conn.commit()
# =====================================
# SUPPLIER FUNCTIONS
# =====================================

def add_supplier(name, mobile, address, gst):

    cursor.execute("""
    INSERT INTO suppliers
    (supplier_name,mobile,address,gst)
    VALUES (?,?,?,?)
    """, (name, mobile, address, gst))

    conn.commit()


def get_suppliers():

    cursor.execute("""
    SELECT *
    FROM suppliers
    ORDER BY supplier_name
    """)

    return cursor.fetchall()


def delete_supplier(supplier_id):

    cursor.execute(
        "DELETE FROM suppliers WHERE id=?",
        (supplier_id,)
    )

    conn.commit()

def get_customers():

    cursor.execute("""
    SELECT *
    FROM customers
    ORDER BY customer_name
    """)

    return cursor.fetchall()


def delete_customer(customer_id):

    cursor.execute(
        "DELETE FROM customers WHERE id=?",
        (customer_id,)
    )

    conn.commit()
