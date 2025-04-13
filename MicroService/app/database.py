import pandas as pd
from app.models import Movie, MovieCreate
from typing import List, Optional
import os

MOVIES: List[Movie] = []
MOVIE_ID_COUNTER = 1
CSV_PATH = os.path.join(os.path.dirname(__file__), "../data/imdb_top_5000.csv")

def load_movies():
    global MOVIES, MOVIE_ID_COUNTER
    df = pd.read_csv(CSV_PATH)
    MOVIES = []
    for index, row in df.iterrows():
        movie = Movie(
            id=MOVIE_ID_COUNTER,
            title=row.get("title", "Unknown"),
            genre=row.get("genre", "Unknown"),
            director=row.get("director", "Unknown"),
            year=int(row.get("year", 2000)),
            rating=float(row.get("rating", 5.0))
        )
        MOVIES.append(movie)
        MOVIE_ID_COUNTER += 1

def search_movies(title: Optional[str] = None) -> List[Movie]:
    if title:
        return [m for m in MOVIES if title.lower() in m.title.lower()]
    return MOVIES

def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    for movie in MOVIES:
        if movie.id == movie_id:
            return movie
    return None

def add_movie(movie_data: MovieCreate) -> Movie:
    global MOVIE_ID_COUNTER
    new_movie = Movie(id=MOVIE_ID_COUNTER, **movie_data.dict())
    MOVIES.append(new_movie)
    MOVIE_ID_COUNTER += 1
    return new_movie
