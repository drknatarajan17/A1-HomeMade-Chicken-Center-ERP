import streamlit as st
import pandas as pd
import plotly.express as px
from database.crud import get_products, total_products, total_stock

st.title("🏠 Dashboard")

# ============================================
# Load Products
# ============================================

products = get_products()

if products:
    df = pd.DataFrame([dict(row) for row in products])
else:
    df = pd.DataFrame(columns=[
        "id",
        "product_name",
        "category",
        "purchase_price",
        "selling_price",
        "stock",
        "unit"
    ])

# ============================================
# KPI Cards
# ============================================

total_product_count = total_products()
stock_available = total_stock()

inventory_value = 0

if not df.empty:
    inventory_value = (
        df["purchase_price"] * df["stock"]
    ).sum()

col1, col2, col3 = st.columns(3)

col1.metric(
    "📦 Total Products",
    total_product_count
)

col2.metric(
    "🥚 Total Stock",
    f"{stock_available:.2f}"
)

col3.metric(
    "💰 Inventory Value",
    f"₹ {inventory_value:,.2f}"
)

st.divider()

# ============================================
# Product Table
# ============================================

st.subheader("📋 Product Master")

if df.empty:

    st.info("No products available.")

else:

    st.dataframe(
        df,
        use_container_width=True
    )

st.divider()

# ============================================
# Stock by Category
# ============================================

if not df.empty:

    category_stock = (
        df.groupby("category")["stock"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_stock,
        x="category",
        y="stock",
        title="Stock by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ============================================
# Category Distribution
# ============================================

if not df.empty:

    pie = px.pie(
        df,
        names="category",
        title="Category Distribution"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

st.divider()

# ============================================
# Low Stock Alert
# ============================================

st.subheader("⚠ Low Stock Products")

if not df.empty:

    low = df[df["stock"] <= 10]

    if low.empty:

        st.success("No Low Stock Products")

    else:

        st.dataframe(
            low,
            use_container_width=True
        )
