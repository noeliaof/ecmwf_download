### S2S ECMWF Data Retriever

#### Overview

This script allows you to retrieve ECMWF S2S database. It utilizes the ECMWF API to download hindcast or forecast data based on user specifications.
For now, it retrieves data for the ECMWF model.

#### Requirements

- Install the file of the main folder

#### Usage

python ecmwf_data_retriever.py --base_directory /path/to/store/data --product [hindcast/forecast] --var [variable] --prefix [custom_prefix]
