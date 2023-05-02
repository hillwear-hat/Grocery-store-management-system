# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gs"
)

c = mydb.cursor()


def view_all_data():
    c.execute('SELECT products.product_name,uom.uom_name,products.price_per_unit,products.product_id FROM products INNER JOIN uom on products.uom_id=uom.uom_id')
    data=c.fetchall()
    return data

def view_all_data2():
    c.execute('SELECT products.product_id,products.product_name,products.uom_id,products.price_per_unit,uom.uom_name FROM products INNER JOIN uom on products.uom_id=uom.uom_id')
    data=c.fetchall()
    
    return data


def delete_data(product_id):
    #print('DELETE FROM products where product_id='+str(product_id))
    c.execute('DELETE FROM products where product_id='+str(product_id))
    mydb.commit()
    
def add_data(product_name,uom_name,price_per_unit):
    # print(f"select uom.uom_id from uom WHERE uom_name='{uom_name}'")
    c.execute(f"SELECT unit_of_mes_names('{uom_name}')")
    k=c.fetchmany()
    k=k[0][0]
    print(k)
    #print(f"INSERT INTO products (product_name, uom_id, price_per_unit) VALUES ('{product_name}','{k}','{price_per_unit}');")
    c.execute(f"INSERT INTO products (product_name, uom_id, price_per_unit) VALUES ('{product_name}','{k}','{price_per_unit}');")
    mydb.commit()
    
def edit_data(product_name,new_uom_name,new_price):
    c.execute(f"select uom.uom_id from uom WHERE uom_name='{new_uom_name}'")
    k=c.fetchmany()
    k=k[0][0]
    c.execute(f"select products.product_id from products where product_name='{product_name}'")
    product_id=c.fetchall()
    product_id=product_id[0][0]
    #print(f"UPDATE products SET uom_id='{k}',price_per_unit='{new_price}' WHERE products.product_id ='{product_id}' ")
    c.execute(f"UPDATE products SET uom_id='{k}',price_per_unit='{new_price}' WHERE products.product_id ='{product_id}' ")


   
def product_data():
    c.execute('SELECT products.product_name from products')
    data=c.fetchall()
    return data
def get_value(product_name):
    #print(f"select products.price_per_unit from products where product_name='{product_name}'")
    c.execute(f"select get_price_perunit('{product_name}')")
    
    ppu=c.fetchall()
    ppu=ppu[0][0]
    # print(ppu)
    return ppu
    
       
def add_order(cust_name,product_name,qnt):
    # print(product_name)
    c.execute(f"select products.product_id from products where product_name='{product_name}'")
    product_id=c.fetchall()
    product_id=product_id[0][0]
    #print(product_id)
    c.execute(f"insert into order_details (customer_name,product_id,quantity,order_date) values('{cust_name}','{product_id}','{qnt}',curdate());")
    #print(f"insert into order_details (customer_name,product_id,quantity,order_date) values('{cust_name}','{product_id}','{qnt}',curdate());")
    mydb.commit()


def pname(product_id):
    c.execute(f"select get_pname({product_id})")  
    product_name=c.fetchall()
    product_name=product_name[0][0]
    #print(product_name)
    return product_name
      
def show_order():
    c.execute('select * from order_details')
    data=c.fetchall()
    # print(data[1][4])
    
    return data


def update_deliverd(order_id):
    c.execute(f'call delivery_update({order_id})')
    c.execute(f'call delete_delivered({order_id})')
    mydb.commit()
    
def exe_query(sql_query):
    if "select" in sql_query:
        c.execute(sql_query)
        k=c.fetchall()
        return(k)
    else:
        c.execute(sql_query)
        mydb.commit()
    


# if __name__ == '__main__':
#     exe_query("DELETE FROM  products WHERE product_id='90';")
