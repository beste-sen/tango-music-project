import pandas as pd

df = pd.read_csv("../data/high_popularity_spotify_data.csv")

print(df.head())

# Example tango filter
tango = df[
    df["track_artist"].str.contains(
        "Di Sarli|D'Arienzo|Troilo|Pugliese|Canaro",
        case=False,
        na=False
    )
]

print(tango.head())
print("Tango rows:", len(tango))
