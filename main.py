import mysql.connector
import streamlit as st
import plotly.express as px
import pandas as pd
import dash as d

from dash import dcc
from dash import html

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='phonepe'
)

mycursor = mydb.cursor(buffered=True)

def aggregate_transaction(Q,year):
    mycursor.execute("""SELECT state as State, transaction_count as Transaction_count
                     From aggregated_transaction
                     WHERE quater={} and year={}
                     GROUP BY State""".format(Q,year))
    trans_agg = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return trans_agg

def aggregate_user(Q,year):
    mycursor.execute("""SELECT state as State, user_count as Users
                     From aggregated_user
                     WHERE quater={} and year={}
                     GROUP BY State""".format(Q,year))
    user_agg = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return user_agg

def state_transaction(Q,year):
    mycursor.execute("""SELECT state as State, transaction_count as Transactions
                     FROM aggregated_transaction
                     WHERE quater={} and year ={}
                     GROUP BY State
                     ORDER BY Transaction_count DESC
                     LIMIT 10""".format(Q,year))
    state_trans = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return state_trans

def state_user(Q,year):
    mycursor.execute("""SELECT state as State,user_count as Users
                     FROM aggregated_user
                     WHERE quater={} and year={}
                     GROUP BY state
                     ORDER BY user_count DESC
                     LIMIT 10""".format(Q,year))
    state_user = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return state_user

def district_transaction(Q,year): 
    mycursor.execute("""SELECT district as District, transaction_amount as Transaction_amount
                     FROM district_transaction
                     WHERE quater={} and year={}
                     ORDER BY Transaction_amount DESC
                     LIMIT 10""".format(Q,year))
    dis_trans = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return dis_trans

def district_user(Q,year):
    mycursor.execute("""SELECT district as District, registereduser as Users
                     FROM district_user
                     WHERE quater={} and year={}
                     ORDER BY registereduser DESC
                     LIMIT 10""".format(Q,year))
    dis_user = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return dis_user

def pincode_transaction(Q,year):
    mycursor.execute("""SELECT pincode as PostalCode, transaction_amount as Transaction_amount
                     FROM pincode_transaction
                     WHERE quarter={} and year={}
                     ORDER BY transaction_amount DESC
                     LIMIT 10""".format(Q,year))
    pincode_trans = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return pincode_trans 

def pincode_user(Q,year):
    mycursor.execute("""SELECT pincode as PostalCode, registeredusers as users
                     FROM pincode_user
                     WHERE quarter={} and year={}
                     ORDER BY registeredusers DESC
                     LIMIT 10""".format(Q,year))
    pincode_user = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return pincode_user

def type_transaction():
    mycursor.execute("""SELECT transaction_type as Transaction_Type,Transaction_Amount
                     FROM aggregated_transaction
                     GROUP BY Transaction_type""" )
    type_trans = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return type_trans

