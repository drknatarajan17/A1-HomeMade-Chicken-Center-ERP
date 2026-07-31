import streamlit as st
from database.crud import (
    add_supplier,
    get_suppliers,
    delete_supplier
)

st.title("🚚 Supplier Management")

with st.form("supplier_form"):

    name = st.text_input("Supplier Name")
    mobile = st.text_input("Mobile Number")
    address = st.text_area("Address")
    gst = st.text_input("GST Number")

    save = st.form_submit_button("Save Supplier")

if save:

    add_supplier(
        name,
        mobile,
        address,
        gst
    )

    st.success("Supplier Added Successfully")

st.divider()

st.subheader("Supplier List")

suppliers = get_suppliers()

if len(suppliers) == 0:

    st.info("No Suppliers Available")

else:

    for s in suppliers:

        c1, c2, c3, c4, c5 = st.columns([3,2,3,2,1])

        c1.write(s["supplier_name"])
        c2.write(s["mobile"])
        c3.write(s["address"])
        c4.write(s["gst"])

        if c5.button("🗑", key=f"sup_{s['id']}"):

            delete_supplier(s["id"])
            st.rerun()
