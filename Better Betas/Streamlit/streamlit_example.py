import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")
option = st.selectbox("Choose column", df.columns)
st.line_chart(df[option])
