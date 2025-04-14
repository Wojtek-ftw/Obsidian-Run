# 🎬 IMDb Micro-Microservice

This project is a Python-based FastAPI microservice that allows users to retrieve and add movie data from the IMDb Top 5000 dataset. It's containerized using Docker for easy setup and deployment.

---

## 📦 Requirements

- Docker
- Docker Compose
- (Optional) `make` for simplified commands
- IMDb dataset CSV (`imdb_top_5000.csv`) downloaded from [Kaggle](https://www.kaggle.com/datasets/tiagoadrianunes/imdb-top-5000-movies)

---

## 📁 Project Structure
```
imdb_microservice/ 
├── app/ # FastAPI app 
│ ├── main.py # Main API routes 
│ ├── models.py # Pydantic models 
│ └── database.py # In-memory dataset handling 
├── consumer/
│ └── client.py 
├── data/ # Place your imdb_top_5000.csv here 
├── Dockerfile 
├── docker-compose.yml 
├── Makefile 
├── requirements.txt 
└── README.md
```
---

## 🚀 Setup & Run

### 🔹 1. Place the dataset

Download `imdb_top_5000.csv` from [Kaggle](https://www.kaggle.com/datasets/tiagoadrianunes/imdb-top-5000-movies) and place it in the `data/` folder:
```imdb_microservice/data/imdb_top_5000.csv```

### 🔹 2. Build and Run

Using `make`:

```bash
make build   # Build Docker container
make run     # Start the server
```
Or manually:
```
docker-compose build
docker-compose up
```

## 🌐 API Access
Visit the following in your browser:

Swagger Docs: http://localhost:8000/docs

Redoc Docs: http://localhost:8000/redoc

## 🔧 Example Usage
GET all movies
```
curl http://localhost:8000/movies
```
GET movies with a title filter
```
curl "http://localhost:8000/movies?title=Dark"
```
GET movie by ID
```
curl http://localhost:8000/movies/1
```
POST a new movie
```
curl -X POST http://localhost:8000/movies \
  -H "Content-Type: application/json" \
  -d '{
    "tconst": "tt9999999",
    "primaryTitle": "My Cool Movie",
    "startYear": 2025,
    "averageRating": 8.7,
    "numVotes": 12345
  }'
```

<!-- ## 🧪 Consumer Script
Run the provided Python script to make GET and POST requests:
```
python consumer/client.py
``` -->

## 🛑 Stopping the Server
Using `make`:
```
make stop
```
Or:
```
docker-compose down
```
