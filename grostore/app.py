# Importing pakages
import streamlit as st
import mysql.connector

from manage_products import manage_products
from manage_products import add_products
from manage_products import edit_products
from new_order import new_order
from all_order import all_order
from enter_query import enter_query


def main():
    st.title("Grocery store")
    menu = ["Manage products", "new order", "all orders","query"]
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == "Manage products":
        st.subheader("Manage products:")
        manage_products()
        st.subheader("Add new products")
        add_products()
        st.subheader("Edit product")
        edit_products()


    elif choice == "new order":
        st.subheader("orders")
        new_order()

    elif choice == "all orders":
        st.subheader("Manage orders")
        all_order()

    elif choice=="query":
        st.subheader("Query")
        enter_query()
        

if __name__ == '__main__':
    main()
