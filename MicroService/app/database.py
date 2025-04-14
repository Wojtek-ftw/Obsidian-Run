import re
import pandas as pd
from app.models import Movie, MovieCreate, MovieIn
from typing import List, Optional
import os

MOVIES: List[Movie] = []
MOVIE_ID_COUNTER = 1
CSV_PATH = os.path.join(os.path.dirname(__file__), "../data/imdb_top_5000.csv")

def safe_str(value: Optional[str]) -> Optional[str]:
    """Ensure NaN or float values are converted to None or string."""
    if pd.isna(value):
        return None
    return str(value)

def load_movies():
    global MOVIES, MOVIE_ID_COUNTER
    df = pd.read_csv(CSV_PATH)
    id_was_missing = "id" not in df.columns

    # Add "id" column if it doesn't exist
    if id_was_missing:
        df.insert(0, "id", range(MOVIE_ID_COUNTER, MOVIE_ID_COUNTER + len(df)))

    MOVIES = []
    for _, row in df.iterrows():
        movie = Movie(
            id=int(row["id"]),
            tconst=safe_str(row.get("tconst")),
            primaryTitle=safe_str(row.get("primaryTitle")) or "Unknown Title",
            startYear=int(row.get("startYear", 1900)),
            rank=int(row["rank"]) if not pd.isna(row.get("rank")) else None,
            averageRating=float(row.get("averageRating", 0.0)),
            numVotes=int(row.get("numVotes", 0)),
            runtimeMinutes=int(row["runtimeMinutes"]) if not pd.isna(row.get("runtimeMinutes")) else None,
            directors=safe_str(row.get("directors")),
            writers=safe_str(row.get("writers")),
            genres=safe_str(row.get("genres")),
            IMDbLink=safe_str(row.get("IMDbLink")),
            Title_IMDb_Link=safe_str(row.get("Title_IMDb_Link"))
        )
        MOVIES.append(movie)
        MOVIE_ID_COUNTER = max(MOVIE_ID_COUNTER, movie.id + 1)

    if id_was_missing:
        df.to_csv(CSV_PATH, index=False)


def search_movies(title: Optional[str] = None) -> List[Movie]:
    if title:
        pattern = re.compile(title, re.IGNORECASE)
        return [m for m in MOVIES if pattern.search(m.primaryTitle)]
    return MOVIES

def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    for movie in MOVIES:
        if movie.id == movie_id:
            return movie
    return None

def add_movie(movie_in: MovieIn):
    global MOVIE_ID_COUNTER
    movie = Movie(id=MOVIE_ID_COUNTER, **movie_in.dict())
    MOVIES.append(movie)
    MOVIE_ID_COUNTER += 1
    return movie

