import cdsapi
import os

# Initialize CDS API client
c = cdsapi.Client()

# Directory to save downloaded files
output_dir = "/srv/data/noelia/Droughts/"

# Dataset name for UTCI
dataset = "derived-utci-historical"

# Function to request data for the entire year (in a single ZIP file)
def request_utci_year(year, target):
    request = {
        "variable": [
            "universal_thermal_climate_index",
            "mean_radiant_temperature"
        ],
        "version": "1_1",
        "product_type": "consolidated_dataset",
        "year": f"{year}",
        "month": [f"{month:02d}" for month in range(1, 13)],  # 
        "day": [f"{day:02d}" for day in range(1, 32)],  # Max days, CDS will ignore invalid ones
        "area": [90, -10, 30, 30],  # Adjust area if needed
        "format": "zip"  # Ensure the format is ZIP
    }
    print(f"Requesting data for year: {year} → {target}")
    c.retrieve(dataset, request, target)

# Function to retrieve data for a range of years
def retrieve_multiple_years(start_year, end_year, dir_path):
    for year in range(start_year, end_year + 1):
        target_path = os.path.join(dir_path, f"UTCI_{year}.zip")
        request_utci_year(year, target_path)


retrieve_multiple_years(2022, 2024, output_dir)
