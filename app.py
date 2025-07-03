import streamlit as st
from sentiment_analysis import get_sentiment_textblob
from recommender import load_dataset, recommend_songs

st.title("🎵 Song Recommender Based on Your Mood")

user_input = st.text_area("How are you feeling today?", "Type your mood or a sentence...")

if st.button("Recommend Songs"):
    mood = get_sentiment_textblob(user_input)
    st.write(f"Detected Mood: **{mood.capitalize()}**")

    df = load_dataset('data/songs.csv')
    songs = recommend_songs(df, mood)

    st.write("### 🎧 Here are your song recommendations:")
    for _, row in songs.iterrows():
        st.write(f"**{row['track_name']}** by *{row['artist_name']}*")
