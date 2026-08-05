import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('movies.pkl', 'rb'))
new_df = pd.DataFrame(movies)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(new_df.iloc[i[0]].title)

    return recommended_movies

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie",
    new_df['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)

    for movie in recommendations:
        st.write(movie)