import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# create datadrame
df = pd.DataFrame({
    'name':['John', 'Mary', 'Tom'],
    'gender':['male', 'female', 'male'],
    'age':[20, 22, 21],
})

# set title
st.title('first app')

# show dataframe
st.write(df)

# show a plot

fig, ax = plt.subplots()
df.age.plot(ax=ax)
st.pyplot(fig)
print(5)