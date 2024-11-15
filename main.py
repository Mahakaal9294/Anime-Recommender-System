# importing the libraries
import streamlit as st
from streamlit_option_menu import option_menu

# importimg the python files
import About_us, Information, Home, Recommender

# Setting up the page
st.set_page_config(
    page_title='Epic-Recommender',
    page_icon=":space_invader:"
)

# Settingup the siderbar
with st.sidebar:
    option = option_menu(
                menu_title='Main Menu',
                menu_icon='menu-app-fill',
                options=['Home','Information','Recommender','About us'],
                icons=['house-fill','info-circle','search-heart','file-earmark-person']  
                )
    

#loading the selected Page
if option == 'Home':
    Home.app()
elif option == 'Recommender':
    Recommender.app()
elif option == 'Information':
    Information.app()
elif option == 'About us':
    About_us.app()