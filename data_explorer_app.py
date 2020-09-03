import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report




# Side bar settings
st.sidebar.title("California housing dataset EDA")

st.write("""

![calif_housing](https://nationalmortgageprofessional.com/sites/default/files/CA_Home_Sales_05_14_19.jpg)

# California housing EDA App

This app explores the **California Housing Dataset**!

""")

#st.markdown('''#### This app helps in performing EDA on *California housing dataset* ''')
# first add title
#st.title('California housing dataset')
#st.markdown("App performs exploratory data analysis on **California housing** dataset")


# Fetch data
DATA_URL = ('https://raw.githubusercontent.com/yogesh1612/mlbm-datasets/master/califHousing.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data = data.iloc[:, 1:12] 
    return data

# test above function
st.markdown("Dataset for this app is available on [github](https://raw.githubusercontent.com/yogesh1612/mlbm-datasets/master/califHousing.csv). Dataset has 20640 observations and 10 columns")
st.markdown("[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1ZsmTv9B-IVIJymHAijJC2Wh2GeA0cG_8/view?usp=sharing)")

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(100000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.sidebar.subheader('Data')
agree = st.sidebar.checkbox('Show Head & Tail')
if agree:
    st.text("Head")
    st.write(data.head())
    st.text("Tail")
    st.write(data.tail())


st.sidebar.subheader("Summary")
summary = np.round(data.describe(),2)
agree = st.sidebar.checkbox('Show summary')
if agree:
    st.write(summary)


#Draw plots
st.sidebar.subheader("Plots")
var_type = st.sidebar.radio(
     "Select type of variable to plot",
     ('Numeric', 'Categorical'))

if var_type == 'Numeric':
    st.write("Showing numeric variables plot")
    colnames = data.select_dtypes(np.number).columns
    #st.write(colnames)
    option = st.sidebar.selectbox("Select variable to plot ",
                    colnames)
else:
    st.write("Showing categorical variable plot")
    colnames = data.select_dtypes('object').columns
    #st.write(colnames)
    option = st.sidebar.selectbox("Select variable to plot ",
                    colnames)

fig = px.histogram(data, x=option)
st.plotly_chart(fig)


## Dataframe profiling code
## select variables for profiling

# st.sidebar.subheader("Generate dataframe profile report")
# if st.sidebar.button("Generate Profile Report"):
#     options = st.sidebar.multiselect(
#     'Select columns for generating profiling report',
#      data.columns)
# agree = st.sidebar.checkbox('Show profile report')
# if agree:
#     pr = ProfileReport(data[options], explorative=True,minimal=False)
#     #st.title("Pandas Profiling in Streamlit")
#     #st.write(data)
#     st_profile_report(pr)


# Draw map

st.sidebar.subheader("Map")
agree = st.sidebar.checkbox('Show Map')
if agree:
    data.plot(kind="scatter", x="longitude", y="latitude", 
             alpha=0.4,  # for degree of transparency
             
             s=data["population"]/100,  # size of dot
             label="population", figsize=(10,7),
             
             c="median_house_value",  # setting color to median_house_value
             cmap=plt.get_cmap("jet"), colorbar=True,           
    sharex=False)
    plt.legend()
    st.pyplot()