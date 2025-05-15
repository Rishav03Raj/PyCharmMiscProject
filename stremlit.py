from http.client import responses

import streamlit as st
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine ",("Indian","Italian","Mexican","French","Arabic","American"))

def restaurant_name_and_menu_generator(cuisine):
    return{
        'restaurant_name' : 'Curry Delight',
        'menu_items' : 'samosa , paneer tikka'
    }

if cuisine:
    response = restaurant_name_and_menu_generator(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")

    st.write("**Menu items**")
    for item in menu_items:
        st.write("*",item)