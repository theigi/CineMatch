import streamlit as st

def render_movie_card(title, rank):
    st.markdown(f"""
        <div class="movie-card">
            <h4 style='margin:0; color:white;'>{title}</h4>
            <p style='color:#bdc3c7; font-size: 0.8em; margin-top:5px;'>
                Similarity Rank: #{rank}
            </p>
        </div>
    """, unsafe_allow_html=True)