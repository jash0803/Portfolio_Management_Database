import mysql.connector
import streamlit as st
import pandas as pd
from datetime import datetime

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user=st.secrets["db_username"],
    password=st.secrets["db_password"],
    database="portfolio"
)
mycursor = mydb.cursor()

def main():
    st.title("Portfolio Management - CRUD App")

    # Sidebar for selecting table and operation
    table = st.sidebar.selectbox("Select Table", (
        "users", "login", "stock_indices", "stock", "portfolio", 
        "favourite", "news", "currency", "commodity"
    ))
    operation = st.sidebar.selectbox("Select Operation", ("Create", "Read", "Update", "Delete"))

    if operation == "Create":
        create_record(table)
    elif operation == "Read":
        read_records(table)
    elif operation == "Update":
        update_record(table)
    elif operation == "Delete":
        delete_record(table)

def create_record(table):
    st.subheader(f"Create a Record in {table}")
    
    if table == "users":
        user_name = st.text_input("User Name")
        mobile_number = st.text_input("Mobile Number")
        user_email = st.text_input("Email")
        user_pancard = st.text_input("PAN Card")
        bank_acc_number = st.text_input("Bank Account Number")
        dob = st.date_input("Date of Birth")
        
        if st.button("Create"):
            sql = """INSERT INTO users 
                     (user_name, mobile_number, user_email, user_pancard, bank_acc_number, dob) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (user_name, mobile_number, user_email, user_pancard, bank_acc_number, dob)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Created Successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")

    elif table == "portfolio":
        portfolio_type = st.text_input("Portfolio Type")
        purchased_price = st.number_input("Purchased Price", min_value=0.0, step=0.01)
        quantity_owned = st.number_input("Quantity", min_value=1, step=1)
        user_id = st.number_input("User ID", min_value=1, step=1)
        asset_symbol = st.text_input("Asset Symbol")
        asset_type = st.selectbox("Asset Type", ["Stock", "Currency", "Commodity"])
        
        if st.button("Create"):
            sql = """INSERT INTO portfolio 
                     (portfolio_type, purchased_price, quantity_owned, user_id, asset_symbol, asset_type) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (portfolio_type, purchased_price, quantity_owned, user_id, asset_symbol, asset_type)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Created Successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")

    elif table == "stock":
        stock_symbol = st.text_input("Stock Symbol")
        stock_name = st.text_input("Stock Name")
        stock_price = st.number_input("Current Price", min_value=0.0, step=0.01)
        opening_price = st.number_input("Opening Price", min_value=0.0, step=0.01)
        closing_price = st.number_input("Closing Price", min_value=0.0, step=0.01)
        stock_type = st.text_input("Stock Type")
        index_symbol = st.text_input("Index Symbol")
        
        if st.button("Create"):
            sql = """INSERT INTO stock 
                     (stock_symbol, stock_name, stock_price, opening_price, closing_price, stock_type, index_symbol) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            val = (stock_symbol, stock_name, stock_price, opening_price, closing_price, stock_type, index_symbol)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Created Successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")

    elif table == "currency":
        currency_symbol = st.text_input("Currency Symbol")
        currency_name = st.text_input("Currency Name")
        conversion_rate = st.number_input("Conversion Rate", min_value=0.0001, step=0.0001)
        
        if st.button("Create"):
            sql = """INSERT INTO currency 
                     (currency_symbol, currency_name, conversion_rate) 
                     VALUES (%s, %s, %s)"""
            val = (currency_symbol, currency_name, conversion_rate)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Created Successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")

    elif table == "commodity":
        commodity_name = st.text_input("Commodity Name")
        commodity_type = st.text_input("Commodity Type")
        last_traded_price = st.number_input("Last Traded Price", min_value=0.0, step=0.01)
        
        if st.button("Create"):
            sql = """INSERT INTO commodity 
                     (commodity_name, commodity_type, last_traded_price) 
                     VALUES (%s, %s, %s)"""
            val = (commodity_name, commodity_type, last_traded_price)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Created Successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")

def read_records(table):
    st.subheader(f"Records from {table}")
    try:
        mycursor.execute(f"SELECT * FROM {table}")
        columns = [desc[0] for desc in mycursor.description]
        records = mycursor.fetchall()
        df = pd.DataFrame(records, columns=columns)
        st.dataframe(df)
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

def update_record(table):
    st.subheader(f"Update a Record in {table}")
    
    if table == "users":
        user_id = st.number_input("User ID", min_value=1, step=1)
        user_name = st.text_input("New User Name")
        user_email = st.text_input("New Email")
        mobile_number = st.text_input("New Mobile Number")
        
        if st.button("Update"):
            sql = """UPDATE users 
                     SET user_name=%s, user_email=%s, mobile_number=%s 
                     WHERE user_id=%s"""
            val = (user_name, user_email, mobile_number, user_id)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Updated Successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")

    elif table == "portfolio":
        portfolio_id = st.number_input("Portfolio ID", min_value=1, step=1)
        portfolio_type = st.text_input("New Portfolio Type")
        quantity_owned = st.number_input("New Quantity", min_value=1, step=1)
        
        if st.button("Update"):
            sql = """UPDATE portfolio 
                     SET portfolio_type=%s, quantity_owned=%s 
                     WHERE portfolio_id=%s"""
            val = (portfolio_type, quantity_owned, portfolio_id)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Updated Successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")

def delete_record(table):
    st.subheader(f"Delete a Record from {table}")
    
    id_field_map = {
        "users": "user_id",
        "portfolio": "portfolio_id",
        "news": "news_id"
    }
    
    if table in id_field_map:
        id_field = id_field_map[table]
        record_id = st.number_input(f"Enter {id_field} to Delete", min_value=1, step=1)
        
        if st.button("Delete"):
            sql = f"DELETE FROM {table} WHERE {id_field} = %s"
            val = (record_id,)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Record Deleted Successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")
    else:
        st.warning("Please implement delete operation for this table")

if __name__ == "__main__":
    main()