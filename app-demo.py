import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('Clifornia Housing Data (1990 )by Jinhao Hu ')
df = pd.read_csv('housing.csv')



# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Population (Millions):', 0.0, 500001.0, 1000.0)  # min, max, default

# create a multi select
ocean_proximaity_filter = st.sidebar.multiselect(
    'ocean_proximity Selector',
     df.ocean_proximaity.unique(),
     df.ocean_proximaity.unique())




# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('choose input level', ('Low','Medium','high'))
form.form_submit_button("submit")



df = df[df.median_house_value <= price_filter]


df = df[df.cocean_proximity.isin(ocean_proximaity_filter)]

if country_filter!='Low':
    df = df[df.median_income <= 2.5]
elif country_filter!='Medium':
    df = df[df.median_income >= 2.5 & df.median_income <= 4.5 ]
elif country_filter!='high':
    df = df[df.median_income > 4.5 ]


st.subheader('see more filters in the sidebar')
# show on map
st.map(df)


st.subheader('Histogram of the Median House Value')
fig,ax=plt.subplot(figsize=(15,15))
df.median_house_value.hist(bins=30)
ax.set_title('Histogram of the Median House Value')
st.pyplot(fig)