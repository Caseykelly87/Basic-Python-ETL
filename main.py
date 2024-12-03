from nasa_etl.extract import fetch_data
from nasa_etl.transform import transform_data
from nasa_etl.load import save_data

def run_etl():
    # Extract
    print("Extracting data...")
    raw_data = fetch_data(query="moon landing")

    # Transform
    print("Transforming data...")
    transformed_data = transform_data(raw_data)

    # Load
    print("Loading data...")
    save_data(transformed_data)

if __name__ == "__main__":
    run_etl()