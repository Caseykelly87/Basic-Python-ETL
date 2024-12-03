# nasa_etl/extract.py

import requests
from config import BASE_URL

def fetch_data(query, media_type="image", page=1):
    """Fetch data from NASA API based on search query."""
    url = f"{BASE_URL}/search"
    params = {
        "q": query,
        "media_type": media_type,
        "page": page
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()       # Return JSON response as a Python dictionary
