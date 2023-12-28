import pickle
import streamlit as st
import requests
import pandas as pd
st.header("Movie recommender System")
movies_list = pickle.load(open('movie_list_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open("similarity.pkl", 'rb'))

def fetch_poster(index):
    movie_id = movies.iloc[index].id
    
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e4f3b9d61f3e5e3a6d42cd1122fd23f7".format(movie_id)
    response = requests.get(url=url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/{}".format(data["poster_path"])

def recommend(movie_name):
    index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key=lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(i[0]))
    return recommended_movies, recommended_movies_posters


selected_movie_name = st.selectbox(
    'Make A selection', movies["title"].values)
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])
    
    with col3:

        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    # with col2:
    #     st.header("A dog")
    #     st.image("https://static.streamlit.io/examples/dog.jpg")

    # with col3:
    #     st.header("An owl")
    #     st.image("https://static.streamlit.io/examples/owl.jpg")

