import streamlit as st
import pandas as pd
import plotly.express as pe


# importing the data
df = pd.read_csv('happy.csv')
print(df.columns)

# setting up the website


st.title('Happiness Data App')


# setting up selection boxes

selection_X = st.selectbox("Select data for x-axis", ["GDP", "Happiness", "Generasity"], key='axis-x')

selection_Y = st.selectbox("Select data for y-axis", ["GDP", "Happiness", "Generasity"], key='axis-y')


st.subheader(f"{selection_X} and {selection_Y}")

def get_data(data):


# adding a plot
figure = pe.scatter(x=selection_X, y=selection_Y, labels={"x": selection_X, "y": selection_Y})
st.plotly_chart(figure)
