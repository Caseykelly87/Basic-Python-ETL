# nasa_etl/transform.py

import pandas as pd

def transform_data(data):
    """Transform raw NASA API data into a structured format."""
    items = data.get("collection", {}).get("items", [])
    
    # Extract relevant fields and organize into a DataFrame
    records = []
    for item in items:
        record = {
            "title": item["data"][0].get("title"),
            "nasa_id": item["data"][0].get("nasa_id"),
            "date_created": item["data"][0].get("date_created"),
            "media_type": item["data"][0].get("media_type"),
            "description": item["data"][0].get("description"),
            "keywords": item["data"][0].get("keywords"),
            "center": item["data"][0].get("center"),
            "secondary_creator": item["data"][0].get("secondary_creator"),
            "location": item["data"][0].get("location"),
            "original_url": next((link.get("href") for link in item.get("links", []) if link.get("render") == "image"), None),
        }
        records.append(record)
    
    return pd.DataFrame(records)
