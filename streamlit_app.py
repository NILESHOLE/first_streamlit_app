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

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets create some user interaction
# Put a pick list here so customer can pick the fruit they want to include
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado','Apple'])

# display the table on the page
streamlit.dataframe(my_fruit_list)
