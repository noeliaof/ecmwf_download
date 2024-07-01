import sys
from datetime import datetime, timedelta
import cdsapi

# Initialize CDS API client
c = cdsapi.Client()

def retrieve_interim(year, dir, var):
    """
    Retrieve data for a specific year and variable, and save it in the specified directory.
    """
    target = f"{dir}ERA5_{var}_{year}.nc"
    
    print(f"Retrieving {var} data for {year}...")
    interim_request(year, target, var)
    print(f"Data saved to {target}")
    return target

def interim_request(year, target, var):
    # Calculate the date 5 days ago from today
    end_date = datetime.utcnow() - timedelta(days=5)
    
    # If the end date is in the previous year, adjust the year and month ranges accordingly
    if end_date.year > year:
        months = [f'{month:02d}' for month in range(1, 13)]
        days = [f'{day:02d}' for day in range(1, 32)]
    else:
        months = [f'{month:02d}' for month in range(1, end_date.month + 1)]
        if end_date.month == 1:
            days = [f'{day:02d}' for day in range(1, end_date.day + 1)]
        else:
            days = [f'{day:02d}' for day in range(1, 32)]
     

    print("month", months)
    print("days", days)

    c.retrieve(
        'reanalysis-era5-land',
        {
            'format': 'netcdf',
            'variable': var,
            'year': str(year),
            'month': months,
            'day': days,
            'time': [f'{hour:02d}:00' for hour in range(24)],
            'area': [80, -30, 20, 40],  # North, West, South, East. Default: global
        },
        target
    )

if __name__ == "__main__":
    # Get the current year and month
    now = datetime.utcnow()
    current_year = now.year
    current_month = now.month

    # Adjust the year if the current month is January
    most_recent_year = current_year - 1 if current_month == 1 else current_year

    # Directory where data will be saved
    dir = sys.argv[1] if len(sys.argv) > 1 else './data/'

    # Variables to retrieve
    variables = ["2m_temperature", "total_precipitation", "potential_evaporation"]

    # List to store downloaded file paths
    downloaded_files = []

    for var in variables:
        target = retrieve_interim(most_recent_year, dir, var)
        downloaded_files.append(target)

    # Save the list of downloaded files
    with open(f"{dir}downloaded_files.txt", "w") as file_list:
        for file in downloaded_files:
            file_list.write(f"{file}\n")

    print("All data retrieved and listed in downloaded_files.txt")

