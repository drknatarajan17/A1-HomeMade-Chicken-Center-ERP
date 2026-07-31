import streamlit as st
from database.crud import (
    add_customer,
    get_customers,
    delete_customer
)

st.title("👤 Customer Management")

with st.form("customer"):

    name = st.text_input("Customer Name")

    mobile = st.text_input("Mobile Number")

    address = st.text_area("Address")

    save = st.form_submit_button("Save Customer")

if save:

    add_customer(
        name,
        mobile,
        address
    )

    st.success("Customer Saved")

st.divider()

st.subheader("Customer List")

customers = get_customers()

if len(customers)==0:

    st.info("No Customers")

else:

    for c in customers:

        col1,col2,col3,col4 = st.columns([3,2,3,1])

        col1.write(c["customer_name"])

        col2.write(c["mobile"])

        col3.write(c["address"])

        if col4.button("Delete",key=c["id"]):

            delete_customer(c["id"])

            st.rerun()
