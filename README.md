# 🎬 Movie Recommendation System

A Streamlit-based web app that recommends movies based on user input using **TF-IDF Vectorization** and **Cosine Similarity**. Built using Python and deployed online via Streamlit Cloud.

🚀 **Live App:**  
👉 [Click here to try it out!](https://sh11movierecomendation.streamlit.app/)

---

## 🔍 Features

- 🔎 Movie recommendation based on similarity
- 🤖 Uses NLP (TF-IDF) + Cosine Similarity
- ⚡ Clean Streamlit interface
- 🧪 Tested with real movie data
- 🌐 Deployed via Streamlit Cloud

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn

---

## 📂 Project Structure

📁 movie-recommendation/
├── app.py # Streamlit app
├── prepare_data.py # Prepares feature column
├── movies.csv # Movie dataset
├── requirements.txt # Python dependencies



---

## ▶️ Run it Locally

```bash
git clone https://github.com/sumit2631/movie-recommendation.git
cd movie-recommendation
pip install -r requirements.txt
python prepare_data.py
streamlit run app.py


