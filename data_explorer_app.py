import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


# first add title
st.title('California housing dataset')

# Fetch data
DATA_URL = ('https://raw.githubusercontent.com/yogesh1612/mlbm-datasets/master/califHousing.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data = data.iloc[:, 1:12] 
    return data

# test above function
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(100)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(data)

st.subheader("Summary")
summary = np.round(data.describe(),2)
agree = st.checkbox('Show summary')
if agree:
    st.write(summary)


# Draw plots
st.subheader("Plots")
var_type = st.radio(
     "Select type of variable to plot",
     ('Numeric', 'Categorical'))

if var_type == 'Numeric':
    colnames = data.select_dtypes(np.number).columns
    #st.write(colnames)
    option = st.selectbox("Select variable to plot ",
                    colnames)
else:
    colnames = data.select_dtypes('object').columns
    #st.write(colnames)
    option = st.selectbox("Select variable to plot ",
                    colnames)

fig = px.histogram(data, x=option)
st.plotly_chart(fig)