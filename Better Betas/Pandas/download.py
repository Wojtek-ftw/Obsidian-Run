import os
import requests
import zipfile

# Set up paths and URLs
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
ZIP_FILE_NAME = 'massive-yahoo-finance-dataset.zip'
CSV_FILE_NAME = 'stock_details_5_years.csv'
ZIP_FILE_PATH = os.path.join(DATA_DIR, ZIP_FILE_NAME)
CSV_FILE_PATH = os.path.join(DATA_DIR, CSV_FILE_NAME)

# URL for the Kaggle dataset
DOWNLOAD_URL = 'https://www.kaggle.com/api/v1/datasets/download/iveeaten3223times/massive-yahoo-finance-dataset'

def ensure_data_file():
    # Create data directory if it doesn't exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Check if the zip file exists
    if not os.path.isfile(ZIP_FILE_PATH):
        print(f"{ZIP_FILE_NAME} not found. Downloading...")
        
        # Make the request to download the file (Kaggle API requires authentication)
        headers = {
            'Authorization': 'Bearer YOUR_KAGGLE_API_KEY'
        }

        response = requests.get(DOWNLOAD_URL, headers=headers, stream=True)
        response.raise_for_status()  # Raises error for bad status codes

        # Write the zip file to disk
        with open(ZIP_FILE_PATH, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded and saved to {ZIP_FILE_PATH}")

    else:
        print(f"{ZIP_FILE_NAME} already exists at {ZIP_FILE_PATH}")

    # Check if the CSV file exists
    if not os.path.isfile(CSV_FILE_PATH):
        print(f"{CSV_FILE_NAME} not found. Unzipping {ZIP_FILE_NAME}...")

        # Unzipping the file if the CSV file doesn't exist
        with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zip_ref:
            zip_ref.extractall(DATA_DIR)

        print(f"Unzipped to {DATA_DIR}")
    else:
        print(f"{CSV_FILE_NAME} already exists at {CSV_FILE_PATH}")

if __name__ == '__main__':
    ensure_data_file()
