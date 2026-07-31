import streamlit as st
import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

def login():

    st.title("🍗 A1 HomeMade Chicken Center ERP")

    st.subheader("Login")

    username = st.text_input("Username")

    password = st.text_input("Password", type="password")

    if st.button("Login"):

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username,password)
        )

        user = cursor.fetchone()

        if user:

            st.session_state.logged_in=True
            st.session_state.username=user[1]
            st.session_state.role=user[3]

            st.success("Login Successful")
            st.rerun()

        else:
            st.error("Invalid Username or Password")
