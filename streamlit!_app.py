import streamlit as st
import datetime
import pandas as pd #for creating a data frame
import io
import matplotlib .pyplot as plt
import plotly.express as px
import time

#import options

st.title('Hello Streamlit')
#st.write('Hello word')
#st.image('streamlitpng.png', caption='My Image', use_column_width=True)

#t.write("Choose a number")
#number=st.slider('Number',min_value=1,max_value=100,value=50)
#st.write(f'You chose {number})')

#if st.button('Click me'):
#    st.write('You clicked the button')

#use check box
#check_box_value = st.checkbox('Show content')

#if check_box_value:
 #   st.write('Show content')

#text input
#name = st.text_input('Enter Your Name', 'Type here')
#st.write(f'Hello,{name}')

#feedback
#feedback = st.text_area('Your Feedback:','Type your feedback here')
#st.write(f'Thank you for your feedback:{feedback}')

#age = st.number_input('Enter Your Age',min_value=0,max_value=120,value=32,step=1)

#st.write(f"Your Age is{age}")

#select the date
#date= st.date_input('Select a date', None)
#st.write(f'Selected date is {date}')

#Time input
#time = st.time_input('Select a time',datetime.time(12,00))

#st.write(f'Selected time is {time}')

#Options
options = ["Option 1","Option 2","Option 3"]

#choice = st.selectbox("Choose an Option",options)

#st.write(f'You chose:{choice}')

#choice = st.radio("Choose one Option", options)
#st.write(f'You chose:{choice}')

#selections
#selections = st.multiselect("Choose Multiple Option",options)

#st.write(f'You chose: {",".join(selections)}')

#File uploader
#st.title('File Uploaded')

#uploaded_file = st.file_uploader('Choose a file to upload:', type=['csv','txt','xlsx'])

#if uploaded_file is not None:
 #   st.write(f'File Uploaded: {uploaded_file.name}')

#Download file

#create a dataframe
#

#data processing and visualisation
#Read and manipulate data using the Pandas library.
#data = {'categories':['A', 'B', 'C','D'],'values':[10,15,12,8]}

#uploaded_file = st.file_uploader('Upload a CSV or Excel file', type = ['csv', 'xlsx'])

#if uploaded_file is not None:
#Read the uploaded file into DataFrame
 #df = pd.read_csv(uploaded_file)

#else:
    # Use the default data if no file is uploaded
 #df = pd.DataFrame(data)

 #Display the data
 #st.write("Data:")
 #st.dataframe(df)
#create a bar chart
#st.write("Bar chart:")
#plt.bar(df['categories'], df['values'])
#plt.xlabel('Category')
#plt.ylabel('Value')
#st.pyplot(plt)

#creating an interactive scatter plot with Plotly:
#st.write("Scatter plot:")
#fig = px.scatter(df, x='categories', y='values', color='categories')
#st.plotly_chart(fig)

#Organize content into multiple columns using st.columns().

#col1, col2, col3 = st.columns(3)

#col1.write("Column 1")
#col2.write("Column 2")
#col3.write("Column 3")

#Add content to a sidebar using st.sidebar
#st.write("Main content")
#st.sidebar.write("Sidebar content")

#create collapsible sections using st.expand()
#with st.expander("Section 1"):
#     st.write("Content for Section 1")

#with st.expander("Section 2"):
 #    st.write("Content for Section 2")

#Display progress using st.progress()
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.1)

#show a loading indicator while executing a time-consuming task using st.spinner

with st.spinner("Please wait..."):
    time.sleep(5)
st.write("Task completed.")
