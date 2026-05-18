import streamlit as st
import pandas as pd
import os

st.title("Tango Music Analytics")

st.write("Files in repo root:")
st.write(os.listdir())

df = pd.read_csv("high_popularity_spotify_data.csv")

st.write(df.head())
