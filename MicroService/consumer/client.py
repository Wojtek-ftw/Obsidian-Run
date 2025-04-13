import requests

BASE_URL = "http://localhost:8000"

# Example GET request
def get_movies(title=None):
    params = {"title": title} if title else {}
    response = requests.get(f"{BASE_URL}/movies", params=params)
    print(response.json())

# Example POST request
def add_movie():
    new_movie = {
        "title": "My Cool Movie",
        "genre": "Sci-Fi",
        "director": "John Doe",
        "year": 2025,
        "rating": 8.5
    }
    response = requests.post(f"{BASE_URL}/movies", json=new_movie)
    print(response.status_code, response.json())

if __name__ == "__main__":
    get_movies("Dark")
    add_movie()
