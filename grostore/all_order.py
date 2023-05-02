import pandas as pd
import streamlit as st
from streamlit.components.v1 import html
import streamlit.components.v1 as components
import plotly.express as px
from database import show_order
from database import pname
from database import update_deliverd

def all_order():
    with open('/Users/manas/Desktop/grostore/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 
    data=show_order()
    col1,col2,col3,col4,col5=st.columns((2,3,2,2,2))
    with col1:
        st.write("order id")
        for i in range(0,len(data)):
            st.write(str(data[i][0]))
    with col2:
        st.write("customer name")
        for i in range(0,len(data)):
            st.write(data[i][1])
    with col3:
        st.write("item name")
        for i in range(0,len(data)):
            st.write(pname(data[i][2]))
    with col4:
        st.write("date")
        for i in range(0,len(data)):
            st.write(str(data[i][4]))
    with col5:
        st.write("delivered")
        for i in range(len(data)):
            if (st.button("deliver",key="deliver"+str(data[i][0]))):
                update_deliverd(str(data[i][0]))
                st.experimental_rerun()

            