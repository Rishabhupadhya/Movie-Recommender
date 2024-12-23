import pickle
import streamlit as st
import requests
import random
import gzip


st.set_page_config(
    page_title="Movies Recommendation System",  # App title
    page_icon="🎥",  # Optional emoji or icon
    layout="wide",   # Optional layout setting
)

def set_background_image():
    random_image_url = "https://picsum.movies/1600/900"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{random_image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the background function
set_background_image()




# Movie Recommendation System Header
st.header("Movies Recommendation System")
movies = pickle.load(open('/Users/rishabhupadhyay/Downloads/PROJECTS/Move Recommendation System/movie_list.pkl','rb'))
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)
# similarity = pickle.load(open('/Users/rishabhupadhyay/Downloads/PROJECTS/Move Recommendation System/similarity.pkl.gz','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'SELECT A MOVIE',
    movie_list
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
