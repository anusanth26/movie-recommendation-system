# 🎬 CineSimilarity – Movie Recommendation System

CineSimilarity is a content-based movie recommendation system built using Streamlit.
It recommends movies similar to the one selected.The system analyzes metadata such as **genres, keywords, cast, crew, and plot summaries** to find similarities using Vectorization and Cosine Similarity.



🔗 **Live Demo:** https://cine-similarity.streamlit.app/

---

## 📌 Overview

The recommendation engine is built using the **TMDB 5000 Movie Dataset**. It creates a "tag" for every movie by combining its overview, genres, keywords, top 3 actors, and the director. These tags are then vectorized to calculate the mathematical similarity between movies.

---

### ✨ Features
* Select a movie from a dropdown of 5000+ titles.
* Recommends top 5 similar movies
* Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning (Preprocessing):** Scikit-Learn (CountVectorizer, Cosine Similarity), NLTK (PorterStemmer)
* **Utilities:** Pickle (Serialization), Gdown (File handling)

---

## ⚙️ How It Works

1.  **Data Cleaning:** * Datasets (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) are merged.
    * Columns like JSON-formatted genres and cast are processed to extract required names.
    * Spaces are removed (e.g., "Science Fiction" → "ScienceFiction") to create unique tag tokens.

2.  **Text Processing:**
    * All metadata (Overview, Genre, Keywords, Cast, Director) is concatenated into a single `tags` string.
    * Text is stemmed using NLTK's `PorterStemmer` (e.g., "activity" and "activities" become "activ").

3.  **Vectorization:**
    * I use `CountVectorizer` to convert the text tags into numeric vectors (Bag of Words technique).
    * I limit the vector space to the top 5000 most frequent words.

4.  **Similarity Calculation:**
    * **Cosine Similarity** is calculated between all movie vectors to determine the angle between them. A smaller angle means higher similarity.

---

## 🚀 Local Installation & Setup

If you want to run this app on your local machine, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/anusanth26/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv myenv
```

### 3. Activate the Virtual Environment

Windows:
```bash
myenv\Scripts\activate
```

Mac/Linux:
```bash
source myenv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
streamlit run app.py
```

### 👨‍💻 Author

**Anusanth R**
B.Tech CSE – Amrita Vishwa Vidyapeetham
Passionate about **ML, DL, and Computer Vision**

---

### ⭐ Show Your Support

If you like this project, consider giving the repo a ⭐ **star**!
