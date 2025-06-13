import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

# Load the dataset
movies = pd.read_csv("movies.csv")

# Check if 'combined_features' column exists
if 'combined_features' not in movies.columns:
    st.error("⚠️ 'combined_features' column missing. Please run prepare_data.py first.")
    st.stop()

# TF-IDF vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix)

# Recommendation function
def recommend_movie(movie_name):
    movie_list = movies['title'].tolist()
    close_match = difflib.get_close_matches(movie_name, movie_list)
    
    if not close_match:
        return ["❌ Koi matching movie nahi mila. Check spelling."]
    
    index = movies[movies.title == close_match[0]].index[0]
    similarity_scores = list(enumerate(cosine_sim[index]))
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:6]
    
    recommended = [movies.iloc[i[0]].title for i in sorted_movies]
    return recommended

# --- Streamlit UI Design ---

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🍿 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a movie you like and get similar movie suggestions below.</p>", unsafe_allow_html=True)

st.write("### 🎥 Enter your favourrite Movie :")
movie_input = st.text_input("Example: Titanic, Iron Man, Dhoom", key="movie_input")

if movie_input:
    with st.spinner("🔍 Recommendations dhoondh rahe hain..."):
        recommendations = recommend_movie(movie_input)

    st.success("✨ You might like these types of movies.:")

    for i, movie in enumerate(recommendations, start=1):
        st.markdown(f"<div style='padding: 8px 0; font-size:18px;'>👉 {i}. <strong>{movie}</strong></div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Made with ❤️ by Sumit</p>", unsafe_allow_html=True)
