import streamlit as st
from database.crud import add_product, get_products, delete_product

st.title("📦 Inventory Management")

# ------------------------------
# Add Product
# ------------------------------

st.subheader("➕ Add New Product")

with st.form("product_form"):

    name = st.text_input("Product Name")
    category = st.selectbox(
        "Category",
        ["Chicken", "Egg", "Masala", "Feed", "Other"]
    )

    purchase = st.number_input(
        "Purchase Price",
        min_value=0.0
    )

    selling = st.number_input(
        "Selling Price",
        min_value=0.0
    )

    stock = st.number_input(
        "Stock",
        min_value=0.0
    )

    unit = st.selectbox(
        "Unit",
        ["Kg", "Piece", "Pack"]
    )

    submit = st.form_submit_button("Save Product")

if submit:

    add_product(
        name,
        category,
        purchase,
        selling,
        stock,
        unit
    )

    st.success("Product Added Successfully!")

# ------------------------------
# Product List
# ------------------------------

st.divider()

st.subheader("📋 Product List")

products = get_products()

if len(products) == 0:

    st.info("No Products Found")

else:

    for p in products:

        col1, col2, col3, col4 = st.columns([4,2,2,1])

        with col1:
            st.write(f"**{p['product_name']}**")

        with col2:
            st.write(f"₹ {p['selling_price']}")

        with col3:
            st.write(f"{p['stock']} {p['unit']}")

        with col4:

            if st.button(
                "🗑",
                key=f"delete_{p['id']}"
            ):

                delete_product(p["id"])
                st.rerun()
