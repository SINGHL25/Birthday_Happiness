import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="Birthday Painting Canvas", page_icon="🎨")
st.title("🎨 Digital Birthday Canvas")
st.write("Paint something fun!")

w, h = 400, 300
canvas = Image.new("RGB", (w, h), "white")
draw = ImageDraw.Draw(canvas)

# Draw birthday message
draw.text((50, 30), "Happy Birthday!", fill="pink")
draw.ellipse((140, 100, 260, 220), fill="yellow", outline="orange", width=5)  # "balloon"
draw.line((200, 220, 200, 270), fill="orange", width=2)                       # string

st.image(canvas, caption="Your virtual birthday painting 🎂")
st.info("Want a real painting tool? Try [Aggdraw Streamlit](https://github.com/andfanilo/streamlit-drawable-canvas) for advanced features!")
