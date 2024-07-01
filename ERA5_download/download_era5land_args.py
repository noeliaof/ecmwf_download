import cdsapi
import calendar
import sys
from datetime import datetime, timedelta

c = cdsapi.Client()

def retrieve_interim(yS, yE, mS, mE, var, dirout):
    """
    A function to demonstrate how to iterate efficiently over several years and months etc
    for a particular interim_request.
    Change the variables below to adapt the iteration to your needs.
    You can use the variable 'target' to organize the requested data in files as you wish.
    In the example below the data are organized in files per month. (eg "interim_daily_201510.grb")
    """
    yearStart = yS
    yearEnd = yE
    monthStart = mS
    monthEnd = mE
    
    for year in range(yearStart, yearEnd + 1):
        for month in range(monthStart, monthEnd + 1):
            startDate = '%04d%02d%02d' % (year, month, 1)
            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            print(lastDate)
            print(var)
            target = f"{dirout}/ERA5_{var}_{year}_{month:02d}.nc"
            print(target)
            interim_request(year, month, target, var)


def interim_request(year, month, target, var):
    c.retrieve(
		'reanalysis-era5-land',
        {
            'format':'netcdf',
            'variable':var,
            'year':str(year),
            'month': [f'{month:02d}'],
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
            # 'grid': ['1.0/1.0'],
            'area': [80, -30, 20, 40], # North, West, South, East. Default: global
        },
        target)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: download_era5land_args.py year start_month end_month var dirout")
        sys.exit(1)

    yy = int(sys.argv[1])
    ms = int(sys.argv[2])
    me = int(sys.argv[3])
    var = sys.argv[4]
    dirout = sys.argv[5]
    print("Retrieving the data")
    print("month", ms)
    retrieve_interim(yy, yy, ms, me, var, dirout)


