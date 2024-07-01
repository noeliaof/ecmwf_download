import cdsapi
c = cdsapi.Client()
    # Doesnt work, even if directly copied from CDS API
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'grib',
        'variable': '10m_u_component_of_wind',
        'year': '2023',
        'month': '01',
        'day': '18',
        'time': '11:00',
    },
    'download.grib')
