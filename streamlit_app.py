import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Parents new Healthy Dinner")
streamlit.header("Breakfast Menu!")
streamlit.text("🥣 Chocolate Chip Oatmeal!")
streamlit.text("Kande Batate Pohe")
streamlit.text("Omelette Bread")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

def getFruityViceData(fruitOfChoice):
  fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  


streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error('Please enter fruit name')
  else: 
    streamlit.write('The user entered ', fruit_choice)
    streamlit.dataframe(getFruityViceData(fruit_choice))
except URLError as e:
  streamlit.error()

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Fruit Load list:")
streamlit.dataframe(my_data_row)

streamlit.header("Adding Fruit!")
fruit_choice = streamlit.text_input('What fruit would you like to add?')
streamlit.write('The user entered ', fruit_choice)
streamlit.text("Thank you for adding fruit: " + fruit_choice)
my_cur.execute("insert into fruit_load_list values ('from streamlit!!!')")
