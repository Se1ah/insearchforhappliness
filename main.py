import streamlit as st
import pandas
import plotly.express as px

df = pandas.read_csv("happy.csv")
dataset = tuple(df.columns)[1:]
st.header("In search for happiness")

option_x = st.selectbox("Select the data for X-axis", dataset)

option_y = st.selectbox("Select the data for Y-axis", dataset)

st.subheader(f"{option_x} and {option_y}")

figure = px.scatter(x=df[option_x], y=df[option_y], labels={"x": f"{option_x}", "y": f"{option_y}"})
st.plotly_chart(figure)