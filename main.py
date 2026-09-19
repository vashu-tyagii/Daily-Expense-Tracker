import pandas as pd 
import streamlit as st
from data import database
st.set_page_config(page_title="Daily Expense Tracker",
                   page_icon="🔐", layout="centered")

st.markdown("<h1 style='text-align: center;'>Daily Expense Tracker</h1>", unsafe_allow_html=True)

with st.container(border=True):
    st.subheader('DataFrame Preview')
    st.table(database.get_expense())  # type: ignore