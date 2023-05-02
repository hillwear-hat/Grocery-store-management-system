import pandas as pd
import streamlit as st
from streamlit.components.v1 import html
import streamlit.components.v1 as components
import plotly.express as px
from database import exe_query

def enter_query():
    with open('/Users/manas/Desktop/grostore/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    # exe_query("DELETE FROM  products WHERE product_id='90';")
    with st.form("query_form"):
        sql_query=st.text_input("Enter SQL query")
        submitted=st.form_submit_button("submit")
        if submitted:
            if "select" in sql_query:
                st.write(sql_query)
                k=exe_query(sql_query)
                df = pd.DataFrame(k)
                st.dataframe(df)
            else:
                exe_query(sql_query)

            