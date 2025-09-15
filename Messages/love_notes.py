
import streamlit as st
import random

st.set_page_config(page_title="Love Notes", page_icon="💌")
st.title("💌 Sweet Love Notes")

notes = [
    "You make every day brighter. Happy Birthday! 💖",
    "Your smile is my favorite thing in the world.",
    "Thank you for being my best friend and partner.",
    "I love you more than chocolate (and that's a lot!).",
    "You are my everything. Here's to many more birthdays together!"
]

if st.button("Show me a note"):
    st.success(random.choice(notes))
