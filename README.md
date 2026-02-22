# Cinematch – AI-Powered Movie Recommendation System

🎯 **Purpose**  
Cinematch is an AI-driven movie discovery application that recommends similar movies based on plot descriptions using Natural Language Processing and content-based filtering.

🚀 **Why this project matters**
- Demonstrates practical NLP techniques for recommendation systems
- Shows end-to-end ML application development
- Deployed as a user-facing web app on Render

🔗 **Live Demo**
- 🎬 App: https://cinematch-6sic.onrender.com

🧠 **Key Skills Demonstrated**
- Machine Learning (TF-IDF, similarity modeling)
- Natural Language Processing (NLP)
- Python-based Web Apps (Streamlit)
- Data processing & model serialization
- Cloud deployment (Render)

---

## Project Overview
Cinematch analyzes plot summaries from over 5,000 movies to compute semantic similarity and recommend movies with comparable themes and narratives.

---

## Key Features
- **Content-Based Recommendations** using plot similarity
- **NLP Pipeline** with TF-IDF vectorization
- **Fast Predictions** via precomputed similarity matrix
- **Clean UI** inspired by Netflix-style dark themes
- **Production Deployment** using Render Blueprints

---

## Architecture Overview
- **UI Layer**: Streamlit web application
- **ML Layer**: TF-IDF vectorizer + Sigmoid Kernel similarity model
- **Data Layer**: Preprocessed TMDB movie datasets
- **Deployment**: Render using `render.yaml`

---

## Tech Stack

**Frontend / UI**
- Streamlit
- Custom CSS

**Machine Learning & Data**
- Scikit-learn (TF-IDF, Sigmoid Kernel)
- Pandas, NumPy
- Joblib (model serialization)

**DevOps**
- Render (Infrastructure as Code)

---

## Project Structure
```text
movie-recommender-system/
├── app.py               # Streamlit UI entry point
├── render.yaml          # Render deployment configuration
├── requirements.txt     # Python dependencies
├── modules/
│   ├── logic.py         # Recommendation engine
│   ├── styles.py        # Custom CSS
│   └── ui_components.py # UI components
├── dumped_obj/          # Serialized models & data
└── notebooks/           # EDA & model training
```

---

## How It Works (ML Pipeline)
1. **Data Preprocessing**: Merge and clean TMDB datasets
2. **Feature Engineering**: Convert movie plots into TF-IDF vectors
3. **Similarity Modeling**: Compute Sigmoid Kernel similarity scores
4. **Serialization**: Persist models and matrices using Joblib
5. **Inference**: Load artifacts instantly for fast recommendations

---

## Running the Project Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Evaluation Notes
This project highlights:
- Practical application of NLP in recommendation systems
- Clean separation between ML logic and UI
- Efficient use of precomputation for performance
- Real-world deployment of an ML-powered application
