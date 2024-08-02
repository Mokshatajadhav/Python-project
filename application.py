import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Weather Data Analysis')


try:
    df = pd.read_csv('Weather_Data[1].csv')
except FileNotFoundError:
    st.error('File not found. Please check the file path.')
    st.stop()
except Exception as e:
    st.error(f'An unexpected error occurred: {e}')
    st.stop()

df = pd.read_csv('Weather_Data[1].csv')
st.header("Weather File")

try:
    st.header('Dataset:')
    dataset = pd.read_csv('Weather_Data[1].csv')
    st.subheader(f'[records before cleaning:-  {len(dataset)}]')
    dataset = dataset.drop_duplicates()
    st.subheader(f'[records after removing duplicates:-  {len(dataset)}]')
    st.write('')
    st.subheader('Head Function')
    st.write('')
    
    st.write(dataset.head(20))
    st.write('')    
    st.subheader('Tail Function')
    st.write('')
    
    st.write(dataset.tail(15))
    st.write('')    
    st.subheader('Describe')
    st.write('')
    
    st.write(dataset.describe())
    st.write('')    
        
except Exception as e:
    st.error(f'An error occurred while cleaning the dataset: {e}')
    st.stop()




st.subheader('Bar Chart ')
column = st.selectbox('Select Column', df.columns,index=2)

if column == 0:
    st.error('Please select different column')
else:
    st.subheader('Line Chart Graph')
    st.subheader('Line Chart')
    st.line_chart(df[column].tail(15))

    st.subheader('Bar Graph')
    st.bar_chart(df[column].head(5))
    
    st.subheader('Scatter Plot Graph ')
    st.subheader('Scatter Plot')
    st.scatter_chart(df[column].head(20))


    st.subheader("Pie chart using matplotlib")
    plt.pie(df['Rel Hum_%'].value_counts(10).values,autopct='%1.1f%%',labels=df['Rel Hum_%'].value_counts(10).index)
    st.pyplot(plt)
    
