import cdsapi
import calendar
c = cdsapi.Client()
"""
var: 2m_temperature
"""

def retrieve_interim(yS,yE,mS,mE,dir,var):
        """
        A function to demonstrate how to iterate efficiently over several years and months etc
        #rfor a particular interim_request.
        Change the variables below to adapt the iteration to your needs.
        You can use the variable 'target' to organise the requested data in files as you wish.
        In the example below the data are organised in files per month. (eg "interim_daily_201510.grb")
        """
        yearStart = yS
        yearEnd = yE
        monthStart = mS
        monthEnd = mE
        for year in list(range(yearStart, yearEnd + 1)):
                startDate = '%04d%02d%02d' % (year, mS, 1)
                numberOfDays = calendar.monthrange(year, mS)[1]
                lastDate = '%04d%02d%02d' % (year, mE, numberOfDays)
                print(lastDate)
                print(var)
                target = dir+"ERA5_" + var +"_%04d.nc" % (year)
                print(target)
                interim_request(year, target, var)

def interim_request(requestDates, target, var):
    c.retrieve(
#        'reanalysis-era5-single-levels',
	'reanalysis-era5-pressure-levels',
        {
            'product_type':'reanalysis',
            'format':'netcdf',
            'variable':var,
	    'pressure_level':  
                           ['1000', '925','850',
                          '700','500',
            300  ],  
            'year':requestDates,
            'month':[
		    '01','02','03',
		    '04','05','06',
		    '07','08','09',
		    '10','11','12'
            ],
            'day':[
                '01','02','03',
                '04','05','06',
                '07','08','09',
                '10','11','12',
                '13','14','15',
                '16','17','18',
                '19','20','21',
                '22','23','24',
                '25','26','27',
                '28','29','30',
                '31'
            ],
            'time':[
                '00:00','01:00','02:00',
                '03:00','04:00','05:00',
                '06:00','07:00','08:00',
                '09:00','10:00','11:00',
                '12:00','13:00','14:00',
                '15:00','16:00','17:00',
                '18:00','19:00','20:00',
                '21:00','22:00','23:00'
            ],
            'grid': ['1.0/1.0'],
            'area': [80, -40, 30, 40], # North, West, South, East. Default: global
        },
        target)


dir="/storage/homefs/no21h426/"
#var = "total_precipitation"
#var = "relative_humidity"
var="geopotential"
#var="2m_temperature"
#var="surface_solar_radiation_downwards"
#var="mean_sea_level_pressure"
#var="snow_depth"
#var="snow_depth"
#var="u_component_of_wind"
#var="total_column_water_vapour"
#var = 'temperature'
retrieve_interim(2021,2021,1,12,dir,var)
