from pydantic import BaseModel, Field
from typing import Optional

# class MovieBase(BaseModel):
#     id: int
#     tconst: str
#     primaryTitle: str
#     startYear: int
#     rank: Optional[int] = None
#     averageRating: float
#     numVotes: int
#     runtimeMinutes: Optional[int] = None
#     directors: Optional[str] = None
#     writers: Optional[str] = None
#     genres: Optional[str] = None
#     IMDbLink: Optional[str] = None
#     Title_IMDb_Link: Optional[str] = None

class MovieBase(BaseModel):
    tconst: str
    primaryTitle: str
    startYear: int
    rank: Optional[int] = None
    averageRating: float
    numVotes: int
    runtimeMinutes: Optional[int] = None
    directors: Optional[str] = None
    writers: Optional[str] = None
    genres: Optional[str] = None
    IMDbLink: Optional[str] = None
    Title_IMDb_Link: Optional[str] = None


class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

class MovieIn(MovieBase):
    pass