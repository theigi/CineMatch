import streamlit as st
import pandas as pd
import joblib
import os

@st.cache_data
def load_data(folder_path):
    # Join paths using os.path.join for cross-platform compatibility
    data = pd.read_csv(os.path.join(folder_path, 'movie_data_for_app.csv'))
    dataframe = pd.read_csv(os.path.join(folder_path, 'movie_dataframe_for_app.csv'))
    return data, dataframe

@st.cache_resource
def load_models(folder_path):
    # Load the serialized model using joblib
    return joblib.load(os.path.join(folder_path, 'sigmoid_kernel.pkl'))

def get_recommendations(movie_title, sig_kernel, data, dataframe):
    indices = pd.Series(data.index, index=data['original_title'])
    if movie_title not in indices:
        return None
    idx = indices[movie_title]
    sig_scores = sorted(list(enumerate(sig_kernel[idx])), key=lambda x: x[1], reverse=True)
    # Return the top 10 matches, skipping the first one (the movie itself)
    movie_indices = [i[0] for i in sig_scores[1:11]]
    return dataframe.iloc[movie_indices]