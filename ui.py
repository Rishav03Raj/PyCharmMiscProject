# ui.py: Defines the welcoming interface and navigation menu
import streamlit as st
import base64
import os
import time

def render_home():
    # Encode local background image to base64
    image_path = "header2.jpg"
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            b64_string = base64.b64encode(img_file.read()).decode()

        # Apply background and styles
        st.markdown(f"""
        <style>
          .stApp {{
            background: url('data:image/jpeg;base64,{b64_string}') no-repeat center center fixed;
            background-size: cover;
          }}

          .blurry-overlay {{
            position: absolute;
            top: 0;
            left: 2;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(12px);
            z-index: -1;
          }}

          .welcome {{
            position: absolute;
            top: 1.2rem;
            left: 10%;
            transform: translateX(-50%);
            font-size: 3rem;
            color: white;
            font-family: 'Courier New', Courier, monospace;
            text-shadow: 3px 3px 8px #000;
            overflow: hidden;
            white-space: nowrap;
            border-right: .20em solid orange;
            width: 0;
            animation: typing 3.2s steps(30, end), blink 0.75s step-end infinite alternate;
            animation-fill-mode: forwards;
          }}

          .main-title {{
            font-size: 2.5rem;
            text-align: center;
            color: #FF4081;
            font-family: 'Algerian', serif;
            text-shadow: 4px 4px 10px #000;
            margin-top: 7rem;
            opacity: 0;
            animation: zoomIn 1.5s ease-out 3.2s forwards;
          }}

          .subtitle {{
            font-size: 2.1rem;
            text-align: center;
            color: yellow;
            text-shadow: 2px 2px 6px #000;
            font-family: 'Trebuchet MS', sans-serif;
            margin-top: 0.5rem;
            opacity: 0;
            animation: slideIn 2s ease-out 4.7s forwards;
          }}

          .nav-buttons {{
            display: flex;
            justify-content: left;
            gap: 10rem;
            margin-top: 15rem;
            opacity: 0;
            animation: fadeInBtns 1.5s ease-in 6.7s forwards;
          }}

          .nav-buttons button {{
            font-size: 1.2rem;
            padding: 0.8rem 3rem;
            border-radius: 10px;
          }}

          @keyframes typing {{ from {{ width: 0 }} to {{ width: 100% }} }}
          @keyframes blink {{ from {{ border-color: transparent }} to {{ border-color: orange }} }}
          @keyframes zoomIn {{ from {{ transform: scale(0.5); opacity: 0; }} to {{ transform: scale(1); opacity: 1; }} }}
          @keyframes slideIn {{ from {{ transform: translateX(-100px); opacity: 0; }} to {{ transform: translateX(0); opacity: 1; }} }}
          @keyframes fadeInBtns {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        </style>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"Background image not found at '{image_path}'.")

    # Display animated components
    st.markdown('<div class="blurry-overlay"></div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome">Welcome 😊 too..</div>', unsafe_allow_html=True)
    time.sleep(3.2)
    st.markdown('<div class="main-title">👨‍👩‍👧‍👦 First Family Portfolio Manager 📊</div>', unsafe_allow_html=True)
    time.sleep(1.5)
    st.markdown('<div class="subtitle">🌟 Your Family Financial Planner 💰📈</div>', unsafe_allow_html=True)
    time.sleep(1.5)

    # Navigation buttons using st.query_params
    # Navigation buttons using st.query_params
    if st.button("🔍 Analyze P&L"):
        st.query_params["page"] = "analyze"
        st.rerun()

    if st.button("✏️ Update Data"):
        st.query_params["page"] = "update"
        st.rerun()


def render_analyze():
    st.header("Analyze Profit & Loss")
    st.write("Select 'Analyze P&L' from the Home page to view summaries and charts.")

def render_update():
    st.header("Update Portfolio Data")
    st.write("Select 'Update Data' from the Home page to add manual entries or upload statements.")
