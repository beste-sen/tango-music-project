import streamlit as st
import pandas as pd

st.title("Tango Music Analytics")

df = pd.read_csv("data/high_popularity_spotify_data.csv")

st.write(df.head())
