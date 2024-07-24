from openai import OpenAI
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster  # Import MarkerCluster for clustering
import plotly.express as px
from streamlit_lottie import st_lottie
import random
import time
import json

# api_key = st.secrets["OPENAI_API_KEY"]

def app():
    #Create the Streamlit app interface
    st.title("Chat-BOT")
    st.subheader("Твой личный ассистент по построению бизнеса.")

    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
        "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"
        with open("data/bot.json", "r", errors='ignore') as f:
            data = json.load(f)
        st_lottie(data)


    st.title("📎 Бот-консультант")
    st.caption("💭 Задай вопросы по бизнесу")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Что ты хочешь узнать?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        # Добавляем контекст о городе Алматы к сообщению пользователя
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        try:
            client = OpenAI(api_key=openai_api_key)  # Используем api_key, так как openai_api_key уже определен
            # Создаем запрос с контекстом о городе Алматы
            response = client.chat.completions.create(model="gpt-3.5-turbo-0125", messages=st.session_state.messages)
            msg = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)
        except Exception as e:
            st.error(f"OpenAI Error: {e}")

