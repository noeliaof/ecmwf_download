import cdsapi

c = cdsapi.Client()

c.retrieve(
    'insitu-gridded-observations-europe',
    {
        'format': 'zip',
        'grid_resolution': '0.1deg',
        'variable': 'precipitation_amount',
        'product_type': 'ensemble_mean',
        'period': 'full_period',
        'version': '23.1e',
    },
    'total_precipitation_1950-2021.zip')
