import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

movies = {
    1: {'title': 'Space Odyssey', 'genre': 'Sci-Fi', 'release_year': 1970, 'director': 'Stanley Kubrick', 'keywords': ['spaceship', 'artificial intelligence', 'existential']},
    2: {'title': 'Happy Feet', 'genre': 'Animation', 'release_year': 2006, 'director': 'Stanley Kubrick', 'keywords': ['penguins', 'dancing', 'Antarctica']},
    3: {'title': 'The Godfather', 'genre': 'Drama', 'release_year': 1972, 'director': 'Francis Ford Coppola', 'keywords': ['mafia', 'crime', 'family'], 'popularity': 'high'},
    4: {'title': 'Spirited Away', 'genre': 'Animation', 'release_year': 2001, 'director': 'Hayao Miyazaki', 'keywords': ['fantasy', 'spirits', 'Japanese'], 'popularity': 'medium'},
    5: {'title': 'Singin in the Rain', 'genre': 'Musical', 'release_year': 1952, 'director': 'Stanley Donen', 'keywords': ['Hollywood', 'romance', 'classic']},
    6: {'title': 'The Shining', 'genre': 'Horror', 'release_year': 1980, 'director': 'Stanley Kubrick', 'keywords': ['psychological', 'hotel', 'supernatural']},
    7: {'title': 'Pulp Fiction', 'genre': 'Crime', 'release_year': 1994, 'director': 'Quentin Tarantino', 'keywords': ['gangsters', 'violence', 'nonlinear']},
    8: {'title': 'Parasite', 'genre': 'Thriller', 'release_year': 2019, 'director': 'Bong Joon-ho', 'keywords': ['social commentary', 'dark humor', 'Korean'], 'popularity': 'high'},
    9: {'title': 'Bicycle Thieves', 'genre': 'Drama', 'release_year': 1948, 'director': 'Vittorio De Sica', 'keywords': ['poverty', 'realism', 'Italian']},
    10:{'title': 'Monty Python and the Holy Grail', 'genre': 'Comedy', 'release_year': 1975, 'director': 'Terry Gilliam & Terry Jones', 'keywords': ['absurd', 'British humor', 'knights']}
}


def preprocess_movie_data(movies):
    genres = []
    directors = []
    keywords_list = []

    for item_id, details in movies.items():
        genres.append(details['genre'])
        directors.append(details['director'])
        keywords_list.append(' '.join(details['keywords']))

    cv = CountVectorizer() 
    genre_vectors = cv.fit_transform(genres).toarray()
    director_vectors = cv.fit_transform(directors).toarray()
    keywords_vectors = cv.fit_transform(keywords_list).toarray()

    # Combine features into a single matrix
    movie_features = np.concatenate([genre_vectors, director_vectors, keywords_vectors], axis=1)
    return movie_features

def get_recommendations(movie_title, movie_features, movies, n_recommendations=5):
    movie_index = None
    for item_id, details in movies.items():
        if details['title'] == movie_title:
            movie_index = item_id - 1  # Adjust for 0-based indexing 
            break

    if movie_index is not None:
        similarities = cosine_similarity(movie_features[movie_index].reshape(1, -1), movie_features)[0]
        top_indices = similarities.argsort()[::-1][1:n_recommendations+1]  # Exclude the movie itself
        recommended_movies = [movies[i+1]['title'] for i in top_indices]
        return recommended_movies
    else:
        print(f"Movie '{movie_title}' not found in the dataset.")

# Example Usage
liked_movie = 'Space Odyssey'
recommendations = get_recommendations(liked_movie, preprocess_movie_data(movies), movies)

print(f"Recommendations based on '{liked_movie}':")
for movie in recommendations:
    print(movie)
