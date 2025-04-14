import streamlit as st
import pandas as pd


if not "df" in st.session_state:
    df = st.session_state['df'] = pd.read_csv("../data/stock_details_5_years.csv")
else:
    df = st.session_state['df']
st.markdown("Streamlit Demo")
# option = st.selectbox("Choose column", df.columns) 
st.dataframe(df)

