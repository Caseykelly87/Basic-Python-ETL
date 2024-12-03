# nasa_etl/load.py

def save_data(dataframe, filename="nasa_moon_landing_image_data.csv"):
    """Save the transformed data to a CSV file."""
    dataframe.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
