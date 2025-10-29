import streamlit as st
from data_utils import load_data
from apiutils import fetch_api_data, fetch_image
from recommender import recommed_character
st.title("Game of Thrones Character Recommender")
df=load_data()
api_data=fetech_api_data()
characters=df['character'].values
selected_character=st.selectbox("select a character", characters)
recommended_character=recommend_character(selected_character,df)
col1,col2=st.columns(2)
with col1:
    st.header(selected_character)
    st.image(fetch_image(selected_character,api_data))
with col2:
    st.header(recommended_character)
    st.image(fetch_image(recommended_character, api_data))