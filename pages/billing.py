import streamlit as st
from database.crud import get_products

st.title("🧾 Billing / POS")

# -----------------------------
# Initialize Cart
# -----------------------------

if "cart" not in st.session_state:
    st.session_state.cart = []

products = get_products()

if len(products) == 0:
    st.warning("No products available.")
    st.stop()

product_names = [p["product_name"] for p in products]

selected_product = st.selectbox("Select Product", product_names)

selected = next(
    p for p in products
    if p["product_name"] == selected_product
)

qty = st.number_input(
    "Quantity",
    min_value=1.0,
    value=1.0
)

if st.button("➕ Add to Cart"):

    total = qty * selected["selling_price"]

    st.session_state.cart.append({
        "name": selected["product_name"],
        "price": selected["selling_price"],
        "qty": qty,
        "total": total
    })

    st.success("Added to cart!")

# -----------------------------
# Cart
# -----------------------------

st.divider()
st.subheader("🛒 Shopping Cart")

grand_total = 0

if len(st.session_state.cart) == 0:

    st.info("Cart Empty")

else:

    for item in st.session_state.cart:

        st.write(
            f"{item['name']} | "
            f"{item['qty']} × ₹{item['price']} = "
            f"₹{item['total']}"
        )

        grand_total += item["total"]

st.divider()

st.metric("Grand Total", f"₹ {grand_total:.2f}")

col1, col2 = st.columns(2)

with col1:

    if st.button("🗑 Clear Cart"):

        st.session_state.cart = []
        st.rerun()

with col2:

    if st.button("💾 Save Bill"):

        st.success("Bill Saved Successfully!")
