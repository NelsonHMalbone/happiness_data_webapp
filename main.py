import streamlit as st
import pandas as pd
import plotly.express as pe


# importing the data
df = pd.read_csv('happy.csv')
print(df.columns)

# setting up the website


st.title('Happiness Data App')


# setting up selection boxes

selection_X = st.selectbox("Select data for x-axis", ["gdp", "happiness", "generosity"], key='axis-x')

selection_Y = st.selectbox("Select data for y-axis", ["gdp", "happiness", "generosity"], key='axis-y')





match selection_X:
    case "happiness":
        x_array = df['happiness']
    case "generosity":
        x_array = df['generosity']
    case "gdp":
        x_array = df['gdp']

match selection_Y:
    case "happiness":
        y_array = df['happiness']
    case "generosity":
        y_array = df['generosity']
    case 'gdp':
        y_array = df['gdp']

st.subheader(f"{selection_X} and {selection_Y}")
# adding a plot
figure = pe.scatter(x=x_array, y=y_array, labels={"x": selection_X, "y": selection_Y})
st.plotly_chart(figure)
