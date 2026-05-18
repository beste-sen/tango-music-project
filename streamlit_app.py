import streamlit as st
import pandas as pd

st.title("Tango Music Analytics")

df = pd.read_csv("high_popularity_spotify_data.csv")

tango_artists = [
    "Carlos Di Sarli",
    "Juan D'Arienzo",
    "Osvaldo Pugliese",
    "Anibal Troilo",
    "Francisco Canaro"
]

tango_df = df[
    df["track_artist"].str.contains(
        "|".join(tango_artists),
        case=False,
        na=False
    )
]

st.write(tango_df)

st.bar_chart(tango_df["danceability"])
