import streamlit as st

st.set_page_config(page_title="Knitting Pattern Visualizer", page_icon="🧶")
st.title("🧶 Knitting Pattern Visualizer")

pattern = st.selectbox("Choose a pattern:", ["Heart", "Zigzag", "Stripe"])

def draw_pattern(pattern):
    if pattern == "Heart":
        return "\n".join([
            "  **   **  ",
            " **** **** ",
            "***********",
            " ********* ",
            "  *******  ",
            "   *****   ",
            "    ***    ",
            "     *     "
        ])
    if pattern == "Zigzag":
        return "\n".join([
            "/\\/\\/\\/\\/\\",
            "\\/\\/\\/\\/\\/"
        ] * 4)
    if pattern == "Stripe":
        return "\n".join([
            "##########",
            "##########",
            "          ",
            "##########",
            "##########"
        ] * 2)

st.code(draw_pattern(pattern))
st.info("Share your favorite pattern for a custom design!")
