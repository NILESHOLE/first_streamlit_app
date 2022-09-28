import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('1. Omega 3 & Blueberry Oatmeal')
streamlit.text('2. Sandwich')
streamlit.text('3. Omlet')

streamlit.header('My Mom''s New Healthy Diner')
streamlit.text('1. 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('2. 🥗 Kale, Spinach')
streamlit.text('3. 🐔 Boiled Egg')
streamlit.text('4. 🥑🍞 Avocado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
