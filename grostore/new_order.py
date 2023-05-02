import pandas as pd
import streamlit as st
from streamlit.components.v1 import html
import streamlit.components.v1 as components
import plotly.express as px
from database import get_value
from database import product_data
from database import add_order

def new_order():
    with open('/Users/manas/Desktop/grostore/style2.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 
    #st.header("New order")
    cust_name=st.text_input("Enter your Name")
    k=product_data()
    #print(k)
    all_products=[]
    for i in range(0,len(k)):
        all_products.append(k[i][0])
    # print(all_products)
    product_name=st.selectbox('select itmes',all_products)
    product_costs=[]
    #print(product_name)
    col1,col2=st.columns((1,0.3))
    with col1:
        st.write(product_name+'-'+str(get_value(product_name)))
    with col2:
        qnt=st.number_input('number',min_value=1,step=1,label_visibility='hidden')
    total=st.write('Total='+str(qnt*get_value(product_name)))
    if st.button("add item"):
        add_order(cust_name,product_name,qnt)
if __name__ == '__main__':
    new_order()