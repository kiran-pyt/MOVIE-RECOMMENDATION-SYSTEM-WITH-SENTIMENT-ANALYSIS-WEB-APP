import streamlit as st
import pickle
import pandas as pd
import requests
from imdb import IMDb
import requests
import bs4 as bs
#from bs4 import BeautifulSoup
import numpy as np
import urllib.request
from urllib.error import HTTPError
# load the nlp model and tfidf vectorizer from disk
filename = 'nlp_model.pkl'
clf = pickle.load(open(filename, 'rb'))
vectorizer = pickle.load(open('tranform.pkl','rb'))


def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=f624751b7e87903422e65d03e58b9364".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/"+ poster_path
    return full_path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies=[]
    recommend_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        # fe
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_posters

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name=st.selectbox('select the movie',movies['title'].values)

##################################



def get_imdb_id(movie_title):
    ia = IMDb()

    # Search for the movie
    movies = ia.search_movie(movie_title)

    if movies:
        # Get the IMDb ID of the first result (you may want to improve error handling)
        imdb_id = movies[0].getID()
        return imdb_id

    return None


# Example usage:
movie_title =selected_movie_name
imdb_id = get_imdb_id(movie_title)
print(f"IMDb ID for '{movie_title}': {'tt' + imdb_id}")
#################################################################################################

imdb_id = 'tt'+imdb_id
#url = 'https://www.imdb.com/title/{}/reviews?ref_=tt_ov_rt'.format(imdb_id)
url='https://www.imdb.com/title/{}/reviews?ref_=tt_urv'.format(imdb_id)
print(url)
try:
    sauce = urllib.request.urlopen(url).read()
    # Process the content as needed
except HTTPError as e:
    print(f"Error fetching URL: {url}")
    print(f"HTTP Error Code: {e.code}")
soup = bs.BeautifulSoup(sauce,'lxml')
soup_result = soup.find_all("div",{"class":"text show-more__control"})
reviews_list = [] # list of reviews
reviews_status = [] # list of comments (good or bad)
for reviews in soup_result:
    if reviews.string:

        reviews_list.append(reviews.string)
        # passing the review to our model
        movie_review_list = np.array([reviews.string])
        movie_vector = vectorizer.transform(movie_review_list)
        pred = clf.predict(movie_vector)
        reviews_status.append('Good' if pred else 'Bad')
# Print the output
for review, status in zip(reviews_list, reviews_status):
    print(f"Review: {review}")
    print(f"Status: {status}")
    print("\n---\n")


if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    #print(names)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        #st.header(names[0])
        st.markdown(f'<h1 style="text-align:center;color:blue;font-size:15px;height:60px;">{names[0]}</h1>', unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        #st.header(names[1])
        st.markdown(f'<h1 style="text-align:center;color:blue;font-size:15px;height:60px;">{names[1]}</h1>', unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        #st.header(names[2])
        st.markdown(f'<h1 style="text-align:center;color:blue;font-size:15px;height:60px;">{names[2]}</h1>', unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        #st.header(names[3])
        st.markdown(f'<h1 style="text-align:center;color:blue;font-size:15px;height:60px;">{names[3]}</h1>', unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        #st.header(names[4])
        st.markdown(f'<h1 style="text-align:center;color:blue;font-size:15px;height:60px;">{names[4]}</h1>', unsafe_allow_html=True)
        st.image(posters[4])
    # Display movie reviews
    st.title('Movie Reviews')
    #for review, status in zip(reviews_list, reviews_status):

        #st.write(f"Review: {review}")
        #st.write(f"Status: {status}")
        #st.write("---")
    for i, (review, status) in enumerate(zip(reviews_list, reviews_status), start=1):
        st.markdown(f'<div style="border:1px solid #ccc; padding:10px; border-radius:5px; margin-bottom:10px;">'
                    f'<p><strong>Review {i}:</strong> {review}</p>'
                    f'<p><strong>Status:</strong> {status}</p>'
                    f'</div>', unsafe_allow_html=True)

