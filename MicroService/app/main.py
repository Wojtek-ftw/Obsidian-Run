from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from app.models import Movie, MovieCreate
from app.database import load_movies, add_movie, get_movie_by_id, search_movies

app = FastAPI()

@app.on_event("startup")
def startup_event():
    load_movies()

@app.get("/movies", response_model=List[Movie])
def get_movies(title: Optional[str] = Query(None)):
    return search_movies(title)

@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    movie = get_movie_by_id(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.post("/movies", response_model=Movie, status_code=201)
def create_movie(movie: MovieCreate):
    return add_movie(movie)
