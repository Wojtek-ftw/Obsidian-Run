"""
Filename: main.py
Description: Server that hosts movie data.
https://www.kaggle.com/datasets/tiagoadrianunes/imdb-top-5000-movies?select=results_with_crew.csv

Author: Wojciech Zacherek
Created: 2025/04/12
Last Modified: 2025/04/13

Copyright © 2025 Wojciech Zacherek
All rights reserved. This file may not be copied, modified, distributed, or used in any form without express written permission.

Contact: w.zacherek@outlook.com
"""

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
    print(f"Move title {title}")
    return search_movies(title)

@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    print(f"Move id {movie_id}")
    movie = get_movie_by_id(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.post("/movies", status_code=201)
def create_movie(movie: MovieCreate):
    print("Here")
    return add_movie(movie)
