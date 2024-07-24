import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import json

def app():
    st.title("Карта г. Алматы")
    st.markdown("Это мое болото, и я вас сюда не приглашал!")

    # Optional: Add Streamlit widgets or interaction here
    layer1 = st.checkbox('Layer 1')
    
    # Read and embed the HTML map
    with open("components/mapp.html", "r", encoding="utf-8") as f:
        map_html = f.read()

    components.html(map_html, height=600)

    # sidebar_slider = st.sidebar.slider("Slider in Sidebar", 0, 100)
    # st.sidebar.write("This is a sidebar text")
    # sidebar_checkbox = st.sidebar.checkbox("Checkbox in Sidebar")

    # st.write("Sidebar Slider Value:", sidebar_slider)
    # st.write("Sidebar Checkbox Value:", sidebar_checkbox)

    with st.sidebar:
        with open("data/urban.json", "r", errors='ignore') as f:
            data = json.load(f)
        st_lottie(data)


if __name__ == "__main__":
    app()
