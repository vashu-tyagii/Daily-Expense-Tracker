import pandas as pd  # type: ignore
from datetime import date
import streamlit as st
from data import database as db

# Define Page Style
st.set_page_config(page_title="Daily Expense Tracker",
                   page_icon="🔐", layout="centered")

# Page Heading
st.markdown("<h1 style='text-align: center;'>Daily Expense Tracker</h1>",
            unsafe_allow_html=True)
# Basic information about app
st.markdown("<h5 style='text-align: center;'>This application is Dedicated to manage our daily expenses </h5>", unsafe_allow_html=True)
st.divider()

with st.container(border=True):
    # creating two columns
    left_column, middle_column, right_column = st.columns(3)

# defining content of first col
    with left_column:
        with st.container(border=True):
            st.subheader('Total Expense')

    with middle_column:
        with st.container(border=True):
            st.subheader('Total Expense By CASH')

    with right_column:
        with st.container(border=True):
            st.subheader('Total Expense By UPI')
st.divider()

with st.container(border=True):
    st.subheader('Adding New Expense :')
    # Id Input
    NAME = st.text_input('ENTER YOUR EXPENSE ITEM NAME :',
                         placeholder='Like (Milk, Fruits, Food, Etc )')
    DATE = st.date_input('ENTER EXPENSE DATE :', value=date(2026, 1, 1))
    TYPE = st.selectbox('CHOOSE EXPENSE TYPE :', ['CASH', 'UPI'])
    AMOUNT = st.number_input('ENTER AMOUNT :', min_value=0.0, step=1.0)

with st.container():
    left_button, right_button = st.columns(2)
    expense_data = pd.DataFrame(
        {
            "name": [NAME],
            "date": [DATE],
            "type": [TYPE],
            "amount": [AMOUNT]
        }
    )
if st.button("SHOW DATA PREVIEW", use_container_width=True):
    st.dataframe(expense_data, use_container_width=True)  # type: ignore

if st.button("INSERT DATA", use_container_width=True):
    if not NAME.strip():
        st.error('EXPENSE ITEM NAME IS REQUIRED')
        st.stop()
    db.insert_expense(NAME,DATE,TYPE,AMOUNT)  # type: ignore
    st.success('Data SuccessFully Inserted !!')
st.divider()

# Show Data Preview
with st.container(border=True):
    st.subheader('Daily Expense Table')
    st.write('Here is Your all Expense Data ')
    st.table(db.get_expense())  # type: ignore
