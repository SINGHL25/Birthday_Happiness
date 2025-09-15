import streamlit as st

st.set_page_config(page_title="Virtual LEGO Mini Builder", page_icon="🧱")
st.title("🧱 Virtual LEGO Minifigure Builder")
st.write("Mix and match colors and accessories for your birthday LEGO minifigure!")

body_color = st.color_picker("Choose body color:", "#FFD700")
headwear = st.selectbox("Pick a hat/hair:", ["None", "Red Cap", "Blonde Hair", "Wizard Hat"])

st.markdown(f"""
<div style='
    width:120px;height:200px;
    background:{body_color};margin:auto;border-radius:30px 30px 40px 40px;'>
    <div style='width:80px;height:70px;background:#FEEBC8;margin:20px auto 0 auto;border-radius:50%;'></div>
    <div style='width:100px;height:15px;background:{"#B22222" if headwear=="Red Cap" else "#F0E68C" if headwear=="Blonde Hair" else "#8A2BE2" if headwear=="Wizard Hat" else body_color};margin:-10px auto 0 auto;border-radius:20px 20px 0 0;'></div>
</div>
""", unsafe_allow_html=True)

st.write("Happy Birthday! 🎉 Build more? Just reload!")
