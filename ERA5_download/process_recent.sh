#!/bin/bash

echo "Starting download and processing"

# Usage check
if [ $# -ne 1 ]; then
  echo "Usage: $0 {dir1}"
  exit 1
fi

# Input arguments
dir1=$1
dir2="${dir1}/day/"

# Ensure dir2 exists
if [ ! -d "$dir2" ]; then
  mkdir -p "$dir2"
  echo "Creating directory for daily data..."
fi

# Call the Python script to download the data
python download_data.py $dir1

# Check if the file list exists
if [ ! -f "${dir1}downloaded_files.txt" ]; then
  echo "Error: downloaded_files.txt not found!"
  exit 1
fi

# Process each file listed in downloaded_files.txt
while IFS= read -r file; do
  echo "Processing file: $file"
  
  # Determine the variable from the filename
  var=$(basename "$file" | cut -d'_' -f2)

  # Process data based on the variable
  case $var in
    "2m_temperature")
      cdo chname,$var,t2m_mean -daymean "$file" "${dir2}/Daymean_$(basename $file)"
      cdo chname,$var,t2m_max -daymax "$file" "${dir2}/Daymax_$(basename $file)"
      cdo chname,$var,t2m_min -daymin "$file" "${dir2}/Daymin_$(basename $file)"
      ;;
    "potential_evaporation")
      cdo chname,$var,pev -daysum "$file" "${dir2}/Daysum_$(basename $file)"
      ;;
    "total_precipitation")
      cdo -b F64 chname,tp,tp_sum -delete,timestep=1 -daysum -shifttime,-1hour "$file" "${dir2}/Daysum_$(basename $file)"
      cdo -b F64 chname,tp,tp_var -delete,timestep=1 -dayvar -shifttime,-1hour "$file" "${dir2}/Dayvar_$(basename $file)"
      ;;
    *)
      echo "Variable $var not recognized for processing"
      exit 1
      ;;
  esac
  
  echo "Removing large hourly file"
  # Uncomment the next line to actually remove the file
  # rm "$file"
done < "${dir1}downloaded_files.txt"

echo "Download and processing complete"

