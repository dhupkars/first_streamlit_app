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


streamlit.header("Fruit List contains!")
def getAllFruitList():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from fruit_load_list")
      return my_cur.fetchall()    
if streamlit.button("Get Fruit List!") :  
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  streamlit.text("Fruit Load list:")
  streamlit.dataframe(getAllFruitList())

def insertFruit(fruit_name):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values ('" + fruit_name +"')")
      return streamlit.text('Thanks for adding fruit: ' + fruit_name)

streamlit.header("Adding Fruit!")
fruit_choice = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add new fruit'): 
  streamlit.write('Adding New fruit ', fruit_choice)
  streamlit.text(insertFruit(fruit_choice))

