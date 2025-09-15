import streamlit as st
import datetime
import time
from PIL import Image, ImageDraw, ImageFont
import io
import base64

# Page configuration
st.set_page_config(
    page_title="🎉 Birthday Celebration App 🎂",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for festive styling
def load_css():
    st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
    }
    
    .birthday-title {
        font-size: 4rem;
        font-weight: bold;
        text-align: center;
        color: #ff1493;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: bounce 2s infinite;
        margin: 20px 0;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-20px); }
        60% { transform: translateY(-10px); }
    }
    
    .balloon-animation {
        font-size: 3rem;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    .confetti {
        font-size: 2rem;
        animation: spin 2s linear infinite;
    }
    
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .birthday-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        margin: 15px 0;
        color: white;
    }
    
    .countdown-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-size: 1.5rem;
        margin: 10px 0;
    }
    
    .cake-container {
        text-align: center;
        margin: 30px 0;
    }
    
    .wishes-container {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .photo-frame {
        border: 10px solid gold;
        border-radius: 20px;
        padding: 10px;
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        margin: 20px auto;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to create animated decorations
def create_decorations():
    col1, col2, col3, col4, col5 = st.columns(5)
    
    decorations = ["🎈", "🎉", "🎊", "🎁", "🍰"]
    colors = ["balloon-animation", "confetti", "confetti", "balloon-animation", "balloon-animation"]
    
    for i, (col, decoration, css_class) in enumerate(zip([col1, col2, col3, col4, col5], decorations, colors)):
        with col:
            st.markdown(f'<div class="{css_class}">{decoration}</div>', unsafe_allow_html=True)
            time.sleep(0.1)  # Small delay for animation effect

# Function to calculate days until birthday
def calculate_days_to_birthday(birth_date):
    today = datetime.date.today()
    this_year_birthday = birth_date.replace(year=today.year)
    
    # If birthday has passed this year, calculate for next year
    if this_year_birthday < today:
        next_birthday = birth_date.replace(year=today.year + 1)
    else:
        next_birthday = this_year_birthday
    
    days_left = (next_birthday - today).days
    return days_left, next_birthday

# Function to create a birthday cake ASCII art
def create_cake_display():
    cake = """
    🕯️🕯️🕯️🕯️🕯️
    🍰🍰🍰🍰🍰
    🎂🎂🎂🎂🎂
    🍰🍰🍰🍰🍰
    """
    return cake

# Function to create photo frame effect
def create_photo_frame(uploaded_image):
    if uploaded_image is not None:
        # Open the uploaded image
        image = Image.open(uploaded_image)
        
        # Resize image to fit frame
        image = image.resize((300, 300))
        
        # Create a new image with frame
        frame_size = (340, 340)
        frame_image = Image.new('RGB', frame_size, color='gold')
        
        # Paste the original image in the center
        frame_image.paste(image, (20, 20))
        
        return frame_image
    return None

# Main app function
def main():
    load_css()
    
    # Header decorations
    create_decorations()
    
    # Main title
    st.markdown('<h1 class="birthday-title">🎉 BIRTHDAY CELEBRATION 🎂</h1>', unsafe_allow_html=True)
    
    # Sidebar for inputs
    st.sidebar.header("🎈 Birthday Details")
    
    # Input fields
    name = st.sidebar.text_input("🎯 Enter Birthday Person's Name:", placeholder="e.g., John Doe")
    age = st.sidebar.number_input("🎂 Enter Age:", min_value=1, max_value=150, value=25)
    birth_date = st.sidebar.date_input("📅 Select Birth Date:", datetime.date.today())
    
    # Photo upload
    st.sidebar.header("📸 Upload Birthday Photo")
    uploaded_photo = st.sidebar.file_uploader("Choose a photo...", type=['png', 'jpg', 'jpeg'])
    
    # Custom wishes input
    st.sidebar.header("💌 Personal Wishes")
    custom_wish = st.sidebar.text_area("Write your birthday wishes:", 
                                      placeholder="May all your dreams come true...",
                                      height=100)
    
    if name:
        # Main birthday greeting
        st.markdown(f"""
        <div class="birthday-card">
            <h1 style="text-align: center; font-size: 3rem;">
                🎉 Happy Birthday {name}! 🎂
            </h1>
            <p style="text-align: center; font-size: 1.5rem;">
                Wishing you an amazing {age}{'st' if age == 1 else 'nd' if age == 2 else 'rd' if age == 3 else 'th'} birthday! 🎈
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create columns for layout
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            # Birthday cake display
            st.markdown('<div class="cake-container">', unsafe_allow_html=True)
            st.markdown("### 🍰 Your Birthday Cake 🍰")
            
            cake_display = create_cake_display()
            st.markdown(f"<pre style='font-size: 2rem; text-align: center;'>{cake_display}</pre>", 
                       unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Photo frame display
        if uploaded_photo:
            st.markdown("### 📸 Birthday Star")
            framed_image = create_photo_frame(uploaded_photo)
            if framed_image:
                col_photo1, col_photo2, col_photo3 = st.columns([1, 2, 1])
                with col_photo2:
                    st.image(framed_image, caption=f"Happy Birthday {name}! 🎉", use_column_width=True)
        
        # Countdown to birthday
        if birth_date:
            days_left, next_birthday = calculate_days_to_birthday(birth_date)
            
            if days_left == 0:
                st.markdown("""
                <div class="countdown-box">
                    🎉 IT'S YOUR BIRTHDAY TODAY! 🎉<br>
                    Have an absolutely wonderful day!
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="countdown-box">
                    ⏰ Countdown to Next Birthday ⏰<br>
                    <strong>{days_left} days</strong> until {next_birthday.strftime('%B %d, %Y')}
                </div>
                """, unsafe_allow_html=True)
        
        # Custom wishes display
        if custom_wish:
            st.markdown(f"""
            <div class="wishes-container">
                <h3 style="text-align: center; color: #333;">💌 Special Birthday Wishes 💌</h3>
                <p style="font-size: 1.2rem; text-align: center; color: #555; font-style: italic;">
                    "{custom_wish}"
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Birthday song section
        st.markdown("### 🎵 Birthday Song")
        
        col_song1, col_song2, col_song3 = st.columns([1, 2, 1])
        with col_song2:
            if st.button("🎵 Play Happy Birthday Song! 🎵", key="song_button"):
                st.balloons()  # Streamlit's built-in balloon effect
                
                # Display lyrics
                st.markdown("""
                <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); 
                           padding: 20px; border-radius: 15px; text-align: center;">
                    <h4>🎵 Happy Birthday Song 🎵</h4>
                    <p><em>Happy birthday to you,<br>
                    Happy birthday to you,<br>
                    Happy birthday dear {name},<br>
                    Happy birthday to you!</em> 🎶</p>
                </div>
                """.format(name=name), unsafe_allow_html=True)
                
                # Show celebration message
                st.success("🎉 Playing Happy Birthday Song! 🎉")
        
        # Additional fun features
        st.markdown("### 🎮 Fun Activities")
        
        col_fun1, col_fun2, col_fun3 = st.columns(3)
        
        with col_fun1:
            if st.button("🎊 Confetti Shower"):
                st.snow()  # Streamlit's snow effect for confetti
                st.success("🎊 Confetti everywhere!")
        
        with col_fun2:
            if st.button("🎈 Balloon Release"):
                st.balloons()
                st.success("🎈 Balloons flying high!")
        
        with col_fun3:
            if st.button("🎉 Celebration Mode"):
                st.balloons()
                time.sleep(1)
                st.snow()
                st.success("🎉 PARTY TIME!")
        
        # Birthday facts
        st.markdown("### 🎯 Fun Birthday Facts")
        
        facts = [
            f"🎂 {name} has lived approximately {age * 365} days!",
            f"🌍 You share your birthday with about 21 million people worldwide!",
            f"🎈 The tradition of birthday cakes dates back to ancient Greece!",
            f"🎵 'Happy Birthday' is the most recognized song in English!",
            f"✨ Your birthday is special - make this year count!"
        ]
        
        for fact in facts:
            st.info(fact)
    
    else:
        # Welcome message when no name is entered
        st.markdown("""
        <div class="birthday-card">
            <h2 style="text-align: center;">
                🎈 Welcome to the Birthday Celebration App! 🎈
            </h2>
            <p style="text-align: center; font-size: 1.2rem;">
                👈 Please enter the birthday person's details in the sidebar to start the celebration! 🎉
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show demo cake
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### 🍰 Birthday Cake Preview 🍰")
            cake_display = create_cake_display()
            st.markdown(f"<pre style='font-size: 2rem; text-align: center;'>{cake_display}</pre>", 
                       unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 50px;">
        <p>🎉 Made with ❤️ using Streamlit | Have a wonderful birthday! 🎂</p>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
