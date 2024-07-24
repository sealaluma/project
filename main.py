import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from components import page1, page2
import json
import base64

from components import chatbot
# from components import business, land_prediction, strategy, estimation, methodology, about, crime, life_quality

# Apply theme from the config file
st.set_page_config(
    page_title="Бизнес планирование",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded"
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Create a sidebar option menu
      
        with st.sidebar:
            app = option_menu(
                menu_title='📌Меню',
                options=['📍Главная', 'карты', '🤖Chat-BOT'],
                icons=['house-garden','house-garden','house-garden'],
                menu_icon='house-garden',
                default_index=0,  # Change the default index to 0 for "🏠 Прогноз стоимости"
                styles={
                    "container": {"padding": "5!important", "width": "100%"},  # Adjust width here
                    # "icon": {"color": "white", "font-size": "0px"},
                    "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "orange"},
                    "nav-link-selected": {"background-color": "#44484d"},
                }

            )


        # Display selected app based on user choice
        if app == "📍Главная":
            page1.app()
        elif app == "карты":
            page2.app()
        elif app == "🤖Chat-BOT":
            chatbot.app()   
        


# Create an instance of MultiApp and add your apps
multi_app = MultiApp()

# Add your apps to the MultiApp instance
multi_app.add_app("дом", page1.app)
multi_app.add_app("карты", page2.app)
multi_app.add_app("чат-бот", chatbot.app)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Укажите путь к вашему файлу изображения
set_background('image/ata3.png')


# Run the MultiApp
multi_app.run()
