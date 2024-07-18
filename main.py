import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from components import page1, page2
import json

from components import chatbot
# from components import business, land_prediction, strategy, estimation, methodology, about, crime, life_quality

# Apply theme from the config file
st.set_page_config(
    page_title="Ого проект",
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
                menu_title='Начало',
                options=['дом', 'карты', 'Chat-BOT'],
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
        
        # with st.sidebar:
        #     app = option_menu(
        #         menu_title='Начало',
        #         options=['🏷️ Прогноз стоимости', '🏙️ Рекомендации', '🏡 Оценка привлекательности',
        #                  '🎯 Расчет по стратегии','👮🏻‍♂️ Преступность', 
        #                  '🗺️ Карта + AI', '🏙️ Информация по кварталам',
        #                  '📒 Методика','📖 Экономика'],
        #         icons=['house-garden','house-garden','house-garden','house-garden','house-garden', 'house-garden',
        #                'house-garden', 'house-garden', 'house-garden'],
        #         menu_icon='house-garden',
        #         default_index=0,  # Change the default index to 0 for "🏠 Прогноз стоимости"
        #         styles={
        #             "container": {"padding": "5!important", "width": "100%"},  # Adjust width here
        #             # "icon": {"color": "white", "font-size": "0px"},
        #             "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "orange"},
        #             "nav-link-selected": {"background-color": "#44484d"},
        #         }

        #     )


        # Display selected app based on user choice
        if app == "дом":
            page1.app()
        elif app == "карты":
            page2.app()
        elif app == "Chat-BOT":
            chatbot.app()   
        
        
        # if app == "🏷️ Прогноз стоимости":
        #     land_prediction.app()
        # elif app == "🏙️ Рекомендации":
        #     recommendations.app()
        # elif app == "🏡 Оценка привлекательности":
        #     estimation.app()   
        # elif app == "🎯 Расчет по стратегии":
        #     strategy.app()        
        # elif app == '👮🏻‍♂️ Преступность':
        #     crime.app()
        # elif app == '🗺️ Карта + AI':
        #     business.app()
        # elif app == '🏙️ Информация по кварталам':
        #     life_quality.app() 
        # elif app == '📒 Методика':
        #     methodology.app()
        # elif app == '📖 Экономика':
        #     about.app()

# Create an instance of MultiApp and add your apps
multi_app = MultiApp()

# Add your apps to the MultiApp instance
multi_app.add_app("дом", page1.app)
multi_app.add_app("карты", page2.app)
multi_app.add_app("чат-бот", chatbot.app)


# multi_app.add_app("🏷️ Прогноз стоимости", land_prediction.app)
# multi_app.add_app("🏙️ Рекомендации", recommendations.app)
# multi_app.add_app("🏡 Оценка привлекательности", estimation.app)
# multi_app.add_app("🎯 Расчет по стратегии", strategy.app)
# multi_app.add_app("👮🏻‍♂️ Преступность", crime.app)
# multi_app.add_app("🗺️ Карта + AI", business.app)
# multi_app.add_app("🏙️ Информация по кварталам", life_quality.app)
# multi_app.add_app("📒 Методика", methodology.app)
# multi_app.add_app("📖 Экономика", about.app)


# Run the MultiApp
multi_app.run()