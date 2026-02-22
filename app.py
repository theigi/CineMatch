import streamlit as st
import os
from modules.styles import apply_custom_css
from modules.logic import load_data, load_models, get_recommendations
from modules.ui_components import render_movie_card

def main():
    st.set_page_config(page_title="Cinematch", page_icon="🎬", layout="wide")
    apply_custom_css()
    
    st.title("🎬 Cinematch")
    
    # Dynamically find the project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(current_dir, "dumped_obj")

    if not os.path.exists(base_path):
        st.error(f"Directory not found: {base_path}")
        return

    try:
        # Load data using the logic module
        data, dataframe = load_data(base_path)
        sig = load_models(base_path)

        movie_list = data['original_title'].sort_values().unique()
        selected_movie = st.sidebar.selectbox("Choose a movie:", movie_list)
        
        if st.sidebar.button('Find Similar Movies'):
            results = get_recommendations(selected_movie, sig, data, dataframe)
            if results is not None:
                st.write(f"### Results for **{selected_movie}**:")
                cols = st.columns(2)
                for i, (idx, row) in enumerate(results.iterrows()):
                    with cols[i % 2]:
                        render_movie_card(row['original_title'], i + 1)
    except Exception as e:
        st.error(f"Critical Error: {e}")

if __name__ == "__main__":
    main()