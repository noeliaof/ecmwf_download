#!/bin/bash

# ========== PATHS ==========
dir='/srv/data/noelia/Droughts/data/ERA5/'
python_script='/home/fe/oterofelipe/ecmwf_download/ERA5_download/get_era5_variables.py'

# Make sure the output directory exists
mkdir -p "$dir"

echo "Starting ERA5 download..."

# ========== VARIABLES TO DOWNLOAD ==========
declare -a surface_vars=(
    'surface_pressure'
    'mean_sea_level_pressure'
    '10m_u_component_of_wind'
    '10m_v_component_of_wind'
    '2m_temperature'
    '2m_dewpoint_temperature'
    'total_precipitation'
    'evaporation'
    'potential_evaporation'
    'surface_net_solar_radiation'
    'surface_net_thermal_radiation'
    'volumetric_soil_water_layer_1'
    'volumetric_soil_water_layer_2'
    'volumetric_soil_water_layer_3'
    'volumetric_soil_water_layer_4'
    'surface_latent_heat_flux'
    'surface_sensible_heat_flux'
    # 'geopotential_at_surface'
    # 'land_sea_mask'
)

declare -a pressure_vars=(
    'geopotential'
    'temperature'
    'specific_humidity'
    'u_component_of_wind'
    'v_component_of_wind'
)

# ========== PROCESS ONE YEAR AT A TIME ==========
year=2021  # Set the year to process here

for var in "${surface_vars[@]}"; do
    echo "Processing surface variable: $var"
    python "$python_script" "$year" "$var"
done

for var in "${pressure_vars[@]}"; do
    echo "Processing pressure variable: $var"
    python "$python_script" "$year" "$var"
done

echo " Download complete."
