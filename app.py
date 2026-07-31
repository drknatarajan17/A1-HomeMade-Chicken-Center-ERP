import streamlit as st
from login import login

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="A1 HomeMade Chicken Center ERP",
    page_icon="🍗",
    layout="wide"
)

# ----------------------------
# Session State
# ----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------------------
# Login Page
# ----------------------------
if not st.session_state.logged_in:

    login()

# ----------------------------
# Main Application
# ----------------------------
else:

    st.sidebar.success(f"Welcome {st.session_state.username}")

    menu = st.sidebar.radio(
        "📋 Menu",
        [
            "Dashboard",
            "Billing",
            "Inventory",
            "Suppliers",
            "Expenses",
            "Reports",
            "Settings",
            "Logout"
        ]
    )

    # ---------------- Dashboard ----------------
    if menu == "Dashboard":

        from pages.dashboard import *

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Today's Sales", "₹18,500", "+12%")
        col2.metric("Today's Profit", "₹6,200", "+9%")
        col3.metric("Customers", "86", "+7")
        col4.metric("Chicken Stock", "132 Kg", "-18 Kg")

        st.divider()

        st.info("📊 Dashboard charts will be added in the next module.")

    # ---------------- Billing ----------------
    elif menu == "Billing":

        try:
            from pages.billing import *

        except Exception as e:
            st.error("Billing module not found.")
            st.code(str(e))

    # ---------------- Inventory ----------------
    elif menu == "Inventory":

        from pages.inventory import *

    # ---------------- customers ----------------
    elif menu=="Customers":

        from pages import customers

    # ---------------- Suppliers ----------------
    elif menu == "Suppliers":

        from pages import suppliers

    # ---------------- Expenses ----------------
    elif menu == "Expenses":

        st.title("💰 Expenses")
        st.info("Expense Module Coming Soon")

    # ---------------- Reports ----------------
    elif menu == "Reports":

        st.title("📈 Reports")
        st.info("Reports Module Coming Soon")

    # ---------------- Settings ----------------
    elif menu == "Settings":

        st.title("⚙️ Settings")
        st.info("Settings Module Coming Soon")

    # ---------------- Logout ----------------
    elif menu == "Logout":

        st.session_state.logged_in = False
        st.rerun()
