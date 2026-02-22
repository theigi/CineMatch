# 🎬 Cinematch: AI-Powered Movie Recommender

Cinematch is a full-stack movie discovery application that utilizes **Natural Language Processing (NLP)** and **Content-Based Filtering** to provide personalized recommendations. The system analyzes plot summaries of 5,000+ movies to find mathematical similarities.



## 🚀 Live Demo
**Link:** [https://cinematch-6sic.onrender.com](https://cinematch-6sic.onrender.com)

## 🛠️ Tech Stack
- **Frontend/UI:** Streamlit (Python-based Web Framework)
- **Styling:** Custom CSS (Netflix-inspired Dark Theme)
- **Machine Learning:** Scikit-learn (TF-IDF Vectorization, Sigmoid Kernel)
- **Data Handling:** Pandas, NumPy, Joblib
- **DevOps:** Render Blueprints (Infrastructure as Code via `render.yaml`)

## 🧠 System Architecture
The project is built using a **Modular Architecture**, separating the core recommendation engine from the user interface for high maintainability.

1.  **Data Preprocessing:** Cleaning and merging TMDB datasets to create a unified metadata pool.
2.  **Feature Engineering:** Transforming movie overviews into a high-dimensional vector space using **TF-IDF**.
3.  **Similarity Modeling:** Computing a **Sigmoid Kernel** similarity matrix to determine plot-based scores.
4.  **Serialization:** Using Joblib to "dump" the heavy matrix into a `.pkl` file for instant loading in production.



## 📂 Project Structure
```text
movie-recommender-system/
├── app.py              # Main Entry Point (Streamlit UI)
├── render.yaml         # Infrastructure as Code for Render Deployment
├── requirements.txt    # Production Dependencies
├── modules/            # Decoupled Python Modules
│   ├── logic.py        # Recommendation Engine
│   ├── styles.py       # Custom CSS Handlers
│   └── ui_components.py# UI Card Renderers
├── dumped_obj/         # Serialized Models and Processed Data
└── notebooks/          # Exploratory Data Analysis & Model Training