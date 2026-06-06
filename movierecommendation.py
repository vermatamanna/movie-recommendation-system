import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.DataFrame({
    "title": [
        "Avengers",
        "Iron Man",
        "Batman",
        "Superman",
        "Doctor Strange"
    ],
    "genre": [
        "action superhero",
        "action superhero",
        "action dc",
        "action dc",
        "magic superhero"
    ]
})

cv = CountVectorizer()
matrix = cv.fit_transform(movies["genre"])

similarity = cosine_similarity(matrix)

def recommend(movie_name):
    idx = movies[movies["title"] == movie_name].index[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommendations for {movie_name}:\n")

    for i in scores[1:4]:
        print(movies.iloc[i[0]]["title"])

recommend("Avengers")