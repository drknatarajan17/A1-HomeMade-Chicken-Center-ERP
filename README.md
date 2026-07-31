# 🍗 A1 HomeMade Chicken Center ERP

A complete ERP (Enterprise Resource Planning) system developed using **Python**, **Streamlit**, and **SQLite** for managing a chicken retail shop. This application simplifies inventory, billing, customer management, supplier management, and business reporting through a user-friendly web interface.

---

# 📌 Features

## 🔐 User Authentication
- Secure Login
- Admin Dashboard
- Role-based architecture (Future)

---

## 📊 Dashboard
- Total Products
- Total Stock
- Sales Summary
- Business Overview
- Quick Navigation

---

## 📦 Inventory Management
- Add Products
- Update Products
- Delete Products
- View Product List
- Stock Management

---

## 🧾 Billing / POS
- Select Products
- Add to Cart
- Quantity Selection
- Grand Total Calculation
- Save Bill (Upcoming)
- Print Invoice (Upcoming)

---

## 👤 Customer Management
- Add Customer
- Customer List
- Delete Customer
- Mobile Number
- Address

---

## 🚚 Supplier Management
- Add Supplier
- Supplier Contact
- GST Details
- Address
- Supplier List

---

# 💻 Technologies Used

- Python 3.x
- Streamlit
- SQLite3
- Pandas
- Plotly (Future)
- Matplotlib (Future)

---

# 📂 Project Structure

```
A1_HomeMade_Chicken_Center/
│
├── app.py
├── database.db
├── login.py
│
├── database/
│   ├── __init__.py
│   ├── database.py
│   └── crud.py
│
├── pages/
│   ├── __init__.py
│   ├── dashboard.py
│   ├── inventory.py
│   ├── billing.py
│   ├── customers.py
│   └── suppliers.py
│
└── assets/
```

---

# 🗄 Database Tables

## Users

- id
- username
- password
- role

---

## Products

- id
- product_name
- category
- purchase_price
- selling_price
- stock
- unit

---

## Customers

- id
- customer_name
- mobile
- address

---

## Suppliers

- id
- supplier_name
- mobile
- address
- gst

---

## Sales

- id
- product
- qty
- amount
- bill_date

---

# ▶ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/A1_HomeMade_Chicken_Center.git
```

Move into project

```bash
cd A1_HomeMade_Chicken_Center
```

Install packages

```bash
pip install streamlit pandas
```

Run the application

```bash
streamlit run app.py
```

---

# 🔑 Default Login

Username

```
admin
```

Password

```
admin123
```

---

# 🚀 Upcoming Features

- Purchase Entry
- Expense Management
- Profit & Loss Report
- Sales Analytics
- Customer Credit
- Supplier Payments
- Barcode Scanner
- QR Code Billing
- Thermal Printer Support
- PDF Invoice
- GST Billing
- WhatsApp Bill Sharing
- SMS Notifications
- Backup & Restore
- Multi-User Login
- Role-Based Access Control
- Cloud Database Support
- Mobile Responsive UI

---

# 📈 Future Enhancements

- AI Demand Forecasting
- Sales Prediction
- Inventory Alerts
- Auto Purchase Suggestions
- Multi-Branch Management
- Employee Payroll
- Attendance Management
- Online Order Integration
- Android Application
- Customer Loyalty Program

---

# 👨‍💻 Developed By

**Dr. K. Natarajan**

Ph.D. in Power Electronics

AI Researcher | EV Charging Systems | Python Developer

---

# 📄 License

This project is developed for educational and commercial business purposes.

© 2026 Dr. K. Natarajan. All Rights Reserved.