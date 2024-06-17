import cdsapi
import calendar
import sys

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
		'reanalysis-era5-land',
        {
            'format':'netcdf',
            'variable':var,
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
                '00:00',
                '06:00',
                '12:00',
                '18:00'
            ],
            # 'grid': ['1.0/1.0'],
            'area': [80, -30, 20, 40], # North, West, South, East. Default: global
        },
        target)


dir="/srv/data/ERA5-LAND/"
var="volumetric_soil_water_layer_2"
#var="temperature"
#var="2m_temperature"
#var="geopotential"
#var="mean_sea_level_pressure"
#var="10m_v_component_of_wind"
#var="v_component_of_wind"

yy = sys.argv[1]
yy= int(yy)
print(yy)
print(type(yy))
retrieve_interim(yy,yy,1,12,dir,var)

