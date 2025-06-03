import cdsapi
import calendar
import sys
import os
from pathlib import Path

c = cdsapi.Client()


# Function to download surface variable for an entire year (all months)
def download_surface_var(year, var, output_path):
    print(f"Surface var: {var} for {year} → {output_path}")
    months = [f"{month:02d}" for month in range(1, 13)]
    
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': var,
            'year': str(year),
            'month': months,
            'day': [f"{d:02d}" for d in range(1, 32)],
            'time': [f"{h:02d}:00" for h in range(24)],
            'area': [80, -90, 20, 30],
        },
        str(output_path)
    )

# Function to download pressure-level variable for an entire year (all months)
def download_pressure_var(year, var, levels, output_path):
    print(f"Pressure var: {var} ({'/'.join(levels)}) for {year} → {output_path}")
    months = [f"{month:02d}" for month in range(1, 13)]
    
    c.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': var,
            'pressure_level': levels,
            'year': str(year),
            'month': months,
            'day': [f"{d:02d}" for d in range(1, 32)],
            'time': [f"{h:02d}:00" for h in range(24)],
            'area': [80, -90, 20, 30],
        },
        str(output_path)
    )

# Main block to run the download for a single year
if __name__ == "__main__":
    year = int(sys.argv[1])  # Pass year as a command-line argument
    output_dir = Path("/srv/data/noelia/Droughts/data/ERA5/")
    output_dir.mkdir(parents=True, exist_ok=True)

    # List of surface variables to download
    surface_vars = [
        'surface_pressure',
        'mean_sea_level_pressure',
        '10m_u_component_of_wind',
        '10m_v_component_of_wind',
        '2m_temperature',
        '2m_dewpoint_temperature',
        'total_precipitation',
        'evaporation',
        'potential_evaporation',
        'surface_net_solar_radiation',
        'surface_net_thermal_radiation',
        'volumetric_soil_water_layer_1',
        'volumetric_soil_water_layer_2',
        'volumetric_soil_water_layer_3',
        'volumetric_soil_water_layer_4',
        'surface_latent_heat_flux',
        'surface_sensible_heat_flux',
        'geopotential_at_surface',
        'land_sea_mask',
    ]

    # List of pressure-level variables
    pressure_vars = [
        'geopotential',
        'temperature',
        'specific_humidity',
        'u_component_of_wind',
        'v_component_of_wind',
    ]

    pressure_levels = ['500', '850', '925']

    # Download each variable for the entire year (one file per year)
    for var in surface_vars:
        output_file = output_dir / f"ERA5_sfc_{var}_{year}.nc"
        if not output_file.exists():
            download_surface_var(year, var, output_file)
        else:
            print(f"File already exists: {output_file}")

    for var in pressure_vars:
        output_file = output_dir / f"ERA5_pl_{var}_{year}.nc"
        if not output_file.exists():
            download_pressure_var(year, var, pressure_levels, output_file)
        else:
            print(f"File already exists: {output_file}")
