import pandas as pd
import streamlit as st
from streamlit.components.v1 import html
import streamlit.components.v1 as components
import plotly.express as px
from database import view_all_data
from database import view_all_data2
from database import delete_data
from database import add_data
from database import edit_data

# with open('/Users/manas/Desktop/grostore/style.css') as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 
        
def manage_products():
    with open('/Users/manas/Desktop/grostore/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 
    result=view_all_data()
    # df=pd.DataFrame(result, columns=['Name','Unit','price per unit'])
    # st.table(df)
     #for i in range(0,len(result)):
    col1,col2,col3,col4=st.columns((1,1,2,1))
    with col1:
        st.header('Name')
        for i in range(0,len(result)):
            st.write(result[i][0])
    with col2:
        st.header('Unit')
        for i in range(0,len(result)):
            st.write(result[i][1])        
    with col3:
        st.header('price per unit')
        for i in range(0,len(result)):
            st.write(str(result[i][2]))
    with col4:
        st.header('delete')
        for i in range(len(result)):
            if (st.button("delete",key="del_btn"+str(result[i][3]))):
                delete_data(str(result[i][3]))
                st.experimental_rerun()        



def add_products():
    with open('/Users/manas/Desktop/grostore/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 
    result=view_all_data2()
    mesname=[]
    for i in range(0,len(result)):
        if result[i][-1] not in mesname:
            mesname.append(result[i][-1])
    
    product_name=st.text_input("Item name:")
    uom_name=st.selectbox("Unit",mesname)
    price_per_unit=st.text_input("Cost of the item")
    if st.button("Add item"):
        add_data(product_name,uom_name,price_per_unit)
        st.success(f"successfully inserted item:{product_name}")
        st.experimental_rerun()
        
        
            
def edit_products():
    with open('/Users/manas/Desktop/grostore/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    result=view_all_data2()
    products=[]
    uoms=[]
    costs=[]    
    for i in range(0,len(result)):
        products.append(result[i][1])
        if result[i][-1] not in uoms:
            uoms.append(result[i][-1])
    product_name=st.selectbox("product name",products)
    new_uom_name=st.selectbox("unit of measurement",uoms)
    new_price=st.text_input("New price")
    if st.button("Edit item"):
        edit_data(product_name,new_uom_name,new_price)
        st.experimental_rerun()
        st.success("successfully edited item") 
          
          

        
        
        
# if __name__ == '__main__':
#     add_products()