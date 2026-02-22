import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        .main { background-color: #0e1117; }
        .stButton>button {
            width: 100%; border-radius: 5px; height: 3em;
            background-color: #e50914; color: white;
            font-weight: bold;
        }
        .movie-card {
            background-color: #262730; padding: 20px;
            border-radius: 10px; border-left: 5px solid #e50914;
            margin-bottom: 10px; transition: 0.3s;
        }
        .movie-card:hover { transform: scale(1.02); }
        </style>
        """, unsafe_allow_html=True)