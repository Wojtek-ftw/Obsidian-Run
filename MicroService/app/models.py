from pydantic import BaseModel, Field
from typing import Optional

class MovieBase(BaseModel):
    title: str
    genre: str
    director: Optional[str]
    year: int = Field(..., ge=1878, le=2100)
    rating: float = Field(..., ge=0.0, le=10.0)

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
