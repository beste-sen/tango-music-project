import streamlit as st
import pandas as pd

st.set_page_config(page_title="El Recodo Tango Database")

st.title("El Recodo Tango Database")

df = pd.read_csv("data.csv")

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Columns")
st.write(df.columns.tolist())

# İlk text kolonunu orchestra gibi kullan
text_cols = df.select_dtypes(include="object").columns.tolist()

selected_column = st.selectbox(
    "Select column to filter",
    text_cols
)

values = sorted(
    df[selected_column]
    .dropna()
    .astype(str)
    .unique()
)

selected_value = st.selectbox(
    "Select value",
    values
)

filtered = df[
    df[selected_column].astype(str) == selected_value
]

st.subheader("Filtered Data")
st.write(filtered)

# Sayısal kolonlar için grafik
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

if numeric_cols:
    chart_col = st.selectbox(
        "Select numeric column",
        numeric_cols
    )

    st.bar_chart(filtered[chart_col])
