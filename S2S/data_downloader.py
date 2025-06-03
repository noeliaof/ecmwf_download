import os
import ssl
import logging
import argparse
from ecmwfapi import ECMWFDataServer
import pandas as pd
from datetime import datetime
import utils.date_to_model as d2m
from utils.DataRetriever import ECMWFDataRetriever
import json

# Open the metadata
with open('metadata.json', 'r') as file:
    metadata = json.load(file)


def parse_args():
    
    parser = argparse.ArgumentParser(description="Retrieve S2S data from ECMWF.")
    parser.add_argument("--base_directory", dest="base_directory", required=True, help="Base directory for storing data.")
    parser.add_argument("--product", dest="product", required=True, help="Type of product, either 'hindcast' or 'forecast'.")
    parser.add_argument("--level_type", dest="level_type", required=True, help="sfc or pl.")
    parser.add_argument("--var", dest="var", required=True, help="Variable to retrieve, e.g., 't2m'.")
    parser.add_argument("--prefix", dest="prefix", required=True, help="Prefix for the data file.")
    
    return parser.parse_args()


if __name__ == "__main__":
    
    args = parse_args()
    dirbase = args.base_directory
    product = args.product
    level_type = args.level_type
    var = args.var
    prefix = args.prefix
    
    # Define the dates to download
    dates_monday = pd.date_range("20220103", periods=52, freq="7D")  # Forecasts start Monday 
    dates_thursday = pd.date_range("20220106", periods=52, freq="7D")  # Forecasts start Thursday
    #dates_monday = pd.date_range("20210104", periods=52, freq="7D")  # Forecasts start Monday 
    #dates_thursday = pd.date_range("20210107", periods=52, freq="7D")  # Forecasts start Thursday
    dates_fcycle = dates_monday.union(dates_thursday)


    retriever = ECMWFDataRetriever(product, level_type=level_type, meta_json=metadata, dates_fcycle=dates_fcycle, dirbase=dirbase)
    retriever.retrieve_data(var, prefix)
