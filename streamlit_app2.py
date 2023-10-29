import streamlit as st
import datetime


#st.title('Hello Streamlit')

#st.image('streamlit.jpeg', caption='Image Caption', use_column_width=True)

#st.write("Choose a number")

#number = st.slider('Number', min_value = 1,max_value=100, value=50)
#st.write(f'You choose{number}')

#if st.button("Click me"):
 # st.write('you clicked the buttom')

check_box_value = st.checkbox('Show Content')

if check_box_value:
    st.write('Content Displayed')

    name = st.text_input('Enter Your Name' , 'Type Name')
    st.write(f'Hello,{name}')

    feedback = st.text_area('Your Feedback:', 'Type your feedback here')
    st.write(f"Thank you for your feedback:{feedback}")

    age = st.number_input("Enter Your Age",min_value=0,max_value=120,value)
    st.write(f'Selected age is {age}')

date = st.date_input('Select a date',None)
st.write(f'Selected date is {date}')

time=st.time_input('Select a time',datetime.time(12,00))
st.write(f'Selected time is {time}')


options = ["Option 1","Option 2","Option 3"]

choice = st.selectbox("Choose an option", options)

st.write(f'You choose:{choice}')

selections = st.multiselect("Choose Multiple Option", options)
st.write(f'You chose:{",".join (selections)}')