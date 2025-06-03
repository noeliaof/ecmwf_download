#!/bin/bash

# add directory
dir1='/srv/data/noelia/Droughts/'

# basedir="$(cd "$(dirname "$0")" && pwd)"
cd $dir1 || exit 1

for year in {2022..2024}; do
    echo "Processing year $year..."

    # Unzip the corresponding file
    unzip -o "${dir1}/UTCI_${year}.zip" -d "${dir1}/UTCI_${year}_unzipped"

    # Change to the unzipped directory
    cd "${dir1}/UTCI_${year}_unzipped" || { echo "Failed to enter directory UTCI_${year}_unzipped"; exit 1; }

    # Merge all ECMWF_utci* files into one
    cdo mergetime ECMWF_utci* "${dir1}/UTCI_${year}_utci.nc"
    echo "Created UTCI_${year}_utci.nc"

    # Merge all ECMWF_mrt* files into one
    cdo mergetime ECMWF_mrt* "${dir1}/UTCI_${year}_mrt.nc"
    echo "Created UTCI_${year}_mrt.nc"

    # Go back to the base directory
    cd "$dir1"
done
