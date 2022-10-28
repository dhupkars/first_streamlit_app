import streamlit
import pandas

streamlit.title("My Parents new Healthy Dinner")
streamlit.header("Breakfast Menu!")
streamlit.text("🥣 Chocolate Chip Oatmeal!")
streamlit.text("Kande Batate Pohe")
streamlit.text("Omelette Bread")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
