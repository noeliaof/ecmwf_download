import cdsapi

dataset = "derived-utci-historical"
request = {
    "variable": [
        "universal_thermal_climate_index",
        "mean_radiant_temperature"
    ],
    "version": "1_1",
    "product_type": "consolidated_dataset",
    "year": ["2020"],
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ],
    "area": [90, -10, 30, 30]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()
