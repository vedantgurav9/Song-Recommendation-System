import pandas as pd

def load_dataset(path='data/songs.csv'):
    return pd.read_csv(path)

def recommend_songs(df, mood, top_n=5):
    mood = mood.lower()
    filtered = df[df['mood'].str.lower().str.contains(mood)]
    return filtered.sample(n=min(top_n, len(filtered)))
