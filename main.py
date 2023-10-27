#importing required packages
import mysql.connector
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

#setting the sql server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='phonepe'
)

mycursor = mydb.cursor(buffered=True)

#function to get data from sql(aggregate transaction table)
def aggregate_transaction(Q,year):
    mycursor.execute("""SELECT state as State, transaction_count as Transactions, transaction_amount as Amount
                     From aggregated_transaction 
                     WHERE quater={} and year={}
                     GROUP BY State""".format(Q,year))
    trans_agg = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return trans_agg

#function to get data from sql(aggregate user table)
def aggregate_user(Q,year):
    mycursor.execute("""SELECT state as State, user_count as Users, brand as Brand
                     From aggregated_user
                     WHERE quater={} and year={}
                     GROUP BY State""".format(Q,year))
    user_agg = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return user_agg

#function to get data from sql(aggregate transaction table)
def state_transaction(Q,year):
    mycursor.execute("""SELECT state as State, transaction_count as Transactions, transaction_amount as Amount
                     FROM aggregated_transaction
                     WHERE quater={} and year ={}
                     GROUP BY State
                     ORDER BY Transaction_count DESC
                     LIMIT 10""".format(Q,year))
    state_trans = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return state_trans

#function to get data from sql(aggregate user table)
def state_user(Q,year):
    mycursor.execute("""SELECT state as State,user_count as Users
                     FROM aggregated_user
                     WHERE quater={} and year={}
                     GROUP BY state
                     ORDER BY user_count DESC
                     LIMIT 10""".format(Q,year))
    state_user = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return state_user

#function to retrive dristrictwise transaction
def district_transaction(Q,year): 
    mycursor.execute("""SELECT district as District, transaction_amount as Transaction_amount, transaction_amount as Amount
                     FROM district_transaction
                     WHERE quater={} and year={}
                     ORDER BY Transaction_amount DESC
                     LIMIT 10""".format(Q,year))
    dis_trans = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return dis_trans

#function to retrive dristrictwise user
def district_user(Q,year):
    mycursor.execute("""SELECT district as District, registereduser as Users
                     FROM district_user
                     WHERE quater={} and year={}
                     ORDER BY registereduser DESC
                     LIMIT 10""".format(Q,year))
    dis_user = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return dis_user

#function to retrive pincodewise transaction
def pincode_transaction(Q,year):
    mycursor.execute("""SELECT pincode as PostalCode, transaction_amount as Transaction_amount, transaction_amount as Amount
                     FROM pincode_transaction
                     WHERE quater={} and year={}
                     ORDER BY transaction_amount DESC
                     LIMIT 10""".format(Q,year))
    pincode_trans = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return pincode_trans 

#function to retrive pincodewise user
def pincode_user(Q,year):
    mycursor.execute("""SELECT pincode as PostalCode, registeredusers as Users
                     FROM pincode_user
                     WHERE quater={} and year={}
                     ORDER BY registeredusers DESC
                     LIMIT 10""".format(Q,year))
    pincode_user = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return pincode_user

#function to retrive typewise transaction
def type_transaction(Q,year):
    mycursor.execute("""SELECT transaction_type as Transaction_type,Transaction_Amount as Amount
                     FROM aggregated_transaction
                     WHERE quater={} AND year={}
                     GROUP BY Transaction_type""".format(Q,year) )
    type_trans = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return type_trans

#function to get precise analysis on transaction
def trans_precise(state):
    mycursor.execute("""SELECT year as Year, transaction_count as Transactions, transaction_amount as Amount
                     From aggregated_transaction 
                     WHERE state='{}'
                     GROUP BY year""".format(state))
    precise_trans = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return precise_trans

#function to get precise analysis on user
def user_precise(state):
    mycursor.execute("""SELECT year as Year,user_count as Users
                     From aggregated_user
                     WHERE state='{}'
                     GROUP BY year""".format(state))
    precise_user = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    return precise_user

#function to get state names
def state_name():
    mycursor.execute("""SELECT state
                     From aggregated_user
                     GROUP BY state""")
    state = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    name = state['state'].tolist()
    return name
    
#streamlit setup
st.button('All India')
operation=st.selectbox('',options=['AGGREGATED','TYPE','TOP','PRECISE'])

#aggregated analysis
if operation=='AGGREGATED':
    option = st.selectbox('',options=['TRANSACTIONS','USERS'])

#transaction analysis
    if option=='TRANSACTIONS':
        y=st.selectbox('year',options=[2018,2019,2020,2021,2022,2023])
        if y == 2023:
            q=st.selectbox('Quater',options=[1,2,3])
        elif y == 2018 or y == 2019 or y == 2020 or y == 2021 or y == 2022:
            q=st.selectbox('Quater',options=[1,2,3,4])
        atdf=aggregate_transaction(q,y)
        atdf=atdf.sort_values(by='Amount',ascending=True)
        opt=st.selectbox('',options=['Payments','Value'])
        if opt=='Value':
            fig = px.bar(atdf,x="Amount", y =atdf["State"], title = 'State transaction amount',text_auto=True,orientation='h')
            st.plotly_chart(fig)
            st.write(atdf[['State','Amount']])
        elif opt=='Payments':
            fig = px.bar(atdf,x="Transactions", y =atdf["State"], title = 'State payment count',text_auto=True,orientation='h')
            st.plotly_chart(fig)
            st.write(atdf[['State','Transactions']])

#user analysis
    if option=='USERS':
        y=st.selectbox('year',options=[2018,2019,2020,2021,2022,2023])
        if y == 2023:
            q=st.selectbox('Quater',options=[1,2,3])
        elif y == 2018 or y == 2019 or y == 2020 or y == 2021 or y == 2022:
            q=st.selectbox('Quater',options=[1,2,3,4])
        audf=aggregate_user(q,y)
        audf=audf.sort_values(by='Users',ascending=True)
        fig = px.bar(audf,x="Users", y =audf["State"], title = 'State Users',text_auto=True,orientation='h')
        st.plotly_chart(fig)
        st.write(audf[['State','Users']])

#type analysis
if operation =='TYPE':
    y = st.selectbox('year',options=[2018,2019,2020,2021,2022,2023])
    if y == 2023:
        q=st.selectbox('Quater',options=[1,2,3])
    elif y == 2018 or y == 2019 or y == 2020 or y == 2021 or y == 2022:
        q=st.selectbox('Quater',options=[1,2,3,4])
    tdf = type_transaction(q,y)
    fig = px.pie(tdf, values='Amount', names='Transaction_type', title='Type of transaction in {}'.format(y))
    st.plotly_chart(fig)
    st.write(tdf[['Transaction_type','Amount']])

#top analysis
if operation =='TOP':
    option = st.selectbox('',options=['TRANSACTIONS','USERS'])
    y = st.radio('year',options=[2018,2019,2020,2021,2022,2023],horizontal=True)
    if y == 2023:
        q=st.select_slider('Quater',options=[1,2,3])
    elif y == 2018 or y == 2019 or y == 2020 or y == 2021 or y == 2022:
        q=st.select_slider('Quater',options=[1,2,3,4])
    if option == 'TRANSACTIONS':
        col1, col2, col3 = st.columns(3)
        with col1:
            button1 = st.button('State')
        with col2:
            button2 = st.button('District')
        with col3:
            button3 = st.button('Postal Code')
        if button1:
            stdf=state_transaction(q,y)
            fig = px.bar(stdf,x="State", y =stdf["Amount"], title = 'Top State Transactions',text_auto=True,orientation='v')
            st.plotly_chart(fig)
            st.write(stdf[['State','Amount']])
        if button2:
            dtdf=district_transaction(q,y)
            fig = px.bar(dtdf,x="District", y =dtdf["Amount"], title = 'Top District Transactions',text_auto=True,orientation='v')
            st.plotly_chart(fig)
            st.write(dtdf[['District','Amount']])
        if button3:
            ptdf=pincode_transaction(q,y)
            fig = go.Figure(data=[go.Pie(labels=ptdf['PostalCode'],values=ptdf['Amount'])])
            fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,marker=dict(line=dict(color='#000000', width=0)))
            st.plotly_chart(fig)
            st.write(ptdf[['PostalCode','Amount']])
    elif option == 'USERS':
        col1, col2, col3 = st.columns(3)
        with col1:
            button1 = st.button('State')
        with col2:
            button2 = st.button('District')
        with col3:
            button3 = st.button('Postal Code')
        if button1:
            sudf=state_user(q,y)
            fig = px.bar(sudf,x="State", y =sudf["Users"], title = 'Top State Transactions',text_auto=True,orientation='v')
            st.plotly_chart(fig)
            st.write(sudf[['State','Users']])
        if button2:
            dudf=district_user(q,y)
            fig = px.bar(dudf,x="District", y =dudf["Users"], title = 'Top District Transactions',text_auto=True,orientation='v')
            st.plotly_chart(fig)
            st.write(dudf[['District','Users']])
        if button3:
            pudf=pincode_user(q,y)
            fig = go.Figure(data=[go.Pie(labels=pudf['PostalCode'],values=pudf['Users'])])
            fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,marker=dict(line=dict(color='#000000', width=0)))
            st.plotly_chart(fig)
            st.write(pudf[['PostalCode','Users']])

#precise analysis
if operation == 'PRECISE':
    name_list = state_name()
    trans=st.selectbox('Select state',options=name_list)
    option = st.selectbox('',options=['TRANSACTIONS','TRANSACTION VALUE','USERS'])
    if option == 'TRANSACTION VALUE':
        tpdf=trans_precise(str(trans))
        fig = px.line(tpdf,x="Year", y =tpdf["Amount"], title = '{} yearly Transaction value'.format(trans))
        st.plotly_chart(fig)
        st.write(tpdf[['Year','Amount']])
    elif option == 'TRANSACTIONS':
        tpdf=trans_precise(str(trans))
        fig = px.line(tpdf,x="Year", y =tpdf["Transactions"], title = '{} yearly Transactions'.format(trans))
        st.plotly_chart(fig)
        st.write(tpdf[['Year','Transactions']])
    elif option == 'USERS':
        tpdf=user_precise(str(trans))
        fig = px.line(tpdf,x="Year", y =tpdf["Users"], title = '{} yearly users'.format(trans))
        st.plotly_chart(fig)
        st.write(tpdf[['Year','Users']])

#===================================================================================================================================================#
