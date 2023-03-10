import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard boiled free range eggs')
streamlit.text('🐔 Poached free range eggs')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#create the function

def get_fruityvice_data(this_fruit_choice): fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice) 
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) return fruityvice_normalized



#New selection to display fruityvice api response

streamlit.header('Fruityvice Fruit Advice!') try: fruit_choice = streamlit.text_input('What fruit would you like information about?') if not fruit_choice: streamlit.error("Please select a fruit to get information.") else: back_from_function = get_fruityvice_data(fruit_choice) streamlit.dataframe(back_from_function)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi') streamlit.write('The user entered ', fruit_choice)

#import request

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#normalize json?

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output ot screen

streamlit.dataframe(fruityvice_normalized) streamlit.dataframe(fruityvice_normalized)

except URLError as e: 
  streamlit.error()



#import requests


# take the json version of the response and normalize it

# output on the screen as a table


# don't run anything past here while we troubleshoot
streamlit.stop()
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
#Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)
#This will not work but go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")







