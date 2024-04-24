import pandas as pd

import streamlit as st

import plotly.express as px

st.header('Tossing a Coin')
st.write('It is not a functional application yet. Under construction.')

# Load data
cars = pd.read_csv(r'C:\Users\tonyr\steve\repo2\vehicles_us (1).csv')

# Create a checkbox to filter data
new_models = st.checkbox("Show only cars from 2013 or older")

if new_models:
    cars = cars[cars['model_year'] <= 2013]

# Create a checkbox to filter expensive cars
expensivecars = st.checkbox("Show only cars over $50k")

if expensivecars:
    cars = cars[cars['price'] > 50000]

# Create two columns for displaying the graphs
col1, col2 = st.columns(2)

# Display histogram in the first column
with col1:
    st.subheader('Histogram')
    fig = px.histogram(cars, x='model_year', y='price')
    st.plotly_chart(fig)

# Display scatter plot in the second column
with col2:
    st.subheader('Scatter Plot')
    fig2 = px.scatter(cars, x='model_year', y='price')
    st.plotly_chart(fig2)
