# Numpy Analysis


## Project Structure
```
Numpy Analysis/ 
├── README.md
├── requirements.txt
├── Dockerfile
├── Makefile
├── setup.py
├── data/
├── numpy_analysis/
│ ├── __init__.py
│ ├── dot_prod.py
│ ├── row_sums.py
│ └── testbench.py
├── notebooks/
│ └── analysis.ipynb
```

## Setup & Run

### 🔹 1. Build and Run

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
To access the server, following the commandline output to get the URL and token. Typically at http://127.0.0.1:8888/lab
