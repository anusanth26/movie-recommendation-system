import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.markdown("""
    <h1 style="text-align:center; color: #4CAF50; font-family: 'Helvetica';">
        🎬 Movie Recommender System
    </h1>
""", unsafe_allow_html=True)

st.write("") 

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]

    top_movies = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i, score in top_movies:
        recommended_movies.append(movies_list.iloc[i].title)

    return recommended_movies

st.markdown("### 🔎 Select a movie you like:")
selected_movie_name = st.selectbox("", movies_list['title'].values)

st.write("")  

if st.button("Recommend Movies", use_container_width=True):
    names = recommend(selected_movie_name)

    st.markdown("---")

    st.markdown("## 🎥 Top Recommendations For You:")

    cols = st.columns(5)

    for idx, col in enumerate(cols):
        if idx < len(names):
            with col:
                st.markdown(
                    f"""
                    <div style="
                        padding: 15px; 
                        background-color: #f2f2f2; 
                        border-radius: 10px; 
                        text-align:center;
                        margin-bottom: 20px;
                        height: 100px;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        font-size: 16px;
                        font-weight: 600;
                        color:#333;">
                        {names[idx]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


