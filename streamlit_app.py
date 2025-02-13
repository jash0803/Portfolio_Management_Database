import mysql.connector
import streamlit as st
import pandas as pd

# Establish a connection to MySQL Server

mydb = mysql.connector.connect(
    host="localhost",
    user=st.secrets["db_username"],
    password=st.secrets["db_password"],
    database="portfolio"
)
mycursor=mydb.cursor()

def main():
    st.title("Portfolio Management - CRUD App")

    # Sidebar for selecting table and operation
    table = st.sidebar.selectbox("Select Table", (
        "users", "login", "stock_indices", "stock", "portfolio", 
        "favourite", "news", "currency", "commodity", "contains_commodity", 
        "contains_currency", "contains_stock"
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
        user_id = st.number_input("User ID", min_value=1, step=1)
        user_name = st.text_input("User Name")
        mobile_number = st.text_input("Mobile Number")
        user_email = st.text_input("Email")
        user_pancard = st.text_input("PAN Card")
        bank_acc_number = st.text_input("Bank Account Number")
        dob = st.date_input("Date of Birth")
        if st.button("Create"):
            sql = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (user_id, user_name, mobile_number, user_email, user_pancard, bank_acc_number, dob)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!")
    elif table == "login":
        login_id = st.number_input("Login ID", min_value=1, step=1)
        login_password = st.text_input("Password", type="password")
        if st.button("Create"):
            sql = "INSERT INTO login VALUES (%s, %s)"
            val = (login_id, login_password)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!")
    elif table == "stock_indices":
        index_symbol = st.text_input("Index Symbol")
        index_name = st.text_input("Index Name")
        if st.button("Create"):
            sql = "INSERT INTO stock_indices VALUES (%s, %s)"
            val = (index_symbol, index_name)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!")
    elif table == "stock":
        stock_symbol = st.text_input("Stock Symbol")
        stock_name = st.text_input("Stock Name")
        stock_price = st.number_input("Stock Price", min_value=0)
        opening_price = st.number_input("Opening Price", min_value=0)
        closing_price = st.number_input("Closing Price", min_value=0)
        stock_type = st.text_input("Stock Type")
        stock_gain_loss = st.number_input("Stock Gain/Loss", min_value=-100000, max_value=100000)
        index_symbol = st.text_input("Index Symbol")
        if st.button("Create"):
            sql = "INSERT INTO stock VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), %s)"
            val = (stock_symbol, stock_name, stock_price, opening_price, closing_price, stock_type, stock_gain_loss, index_symbol)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!")

def read_records(table):
    st.subheader(f"Records from {table}")
    mycursor.execute(f"SELECT * FROM {table}")
    columns = [desc[0] for desc in mycursor.description]  # Fetch column names
    records = mycursor.fetchall()
    df = pd.DataFrame(records, columns=columns)
    st.dataframe(df)  # Display the records as a table with headers

def update_record(table):
    st.subheader(f"Update a Record in {table}")
    if table == "users":
        user_id = st.number_input("User ID", min_value=1, step=1)
        user_name = st.text_input("New User Name")
        user_email = st.text_input("New Email")
        if st.button("Update"):
            sql = "UPDATE users SET user_name=%s, user_email=%s WHERE user_id=%s"
            val = (user_name, user_email, user_id)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!")

def delete_record(table):
    st.subheader(f"Delete a Record from {table}")
    record_id = st.number_input("Enter ID to Delete", min_value=1, step=1)
    if st.button("Delete"):
        sql = f"DELETE FROM {table} WHERE {table}_id = %s"
        val = (record_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        st.success("Record Deleted Successfully!")

if __name__ == "__main__":
    main()


