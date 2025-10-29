import streamlit as st
import requests
from data_utils import load_data
from recommendation import get_closest_character

st.title("Game Of Thrones Personality Matcher")

# Load data
df = load_data()
characters = df['character'].values

# API data for images
api_data = requests.get("https://thronesapi.com/api/v2/Characters").json()

def fetch_image(name, api_data):
    for item in api_data:
        if item['fullName'] == name:
            return item['imageUrl']
    return None

# User selects character
selected_character = st.selectbox("Select a character", characters)

# Find recommended character
recommended_character = get_closest_character(df, selected_character)

# Fetch images
image_url = fetch_image(selected_character, api_data)
recommended_image_url = fetch_image(recommended_character, api_data)

# Display side by side
col1, col2 = st.columns(2)
with col1:
    st.header(selected_character)
    if image_url:
        st.image(image_url)
with col2:
    st.header(recommended_character)
    if recommended_image_url:
        st.image(recommended_image_url)
