import cdsapi
import calendar
import xarray as xr
import numpy as np
import os

c = cdsapi.Client()
# I will need to change this function when using other variable (not z)
def compute_daily_mean(target, dir_out, year, var ):
     fout = dir_out+"ERA5_daily_" + str(year) +"_" + var +".nc" 
     ds_nc = xr.open_mfdataset(target)                        # read the file
     daily_gp = ds_nc.z.resample(time='24H').mean('time')   # calculate day mean (need to change this)
     daily_gp.to_netcdf(fout) 


def retrieve_interim(yS,yE,mS,mE,dir_out,var):
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
                target = dir_out+"ERA5_" + var +"_%04d.nc" % (year)
                print(target)
                interim_request(year, target, var)
                #compute_daily_mean(target,dir_out, year, var) 
                #print("remove hourly file")
                #os.remove(target) 

def interim_request(requestDates, target, var):
    c.retrieve(
		#'reanalysis-era5-single-levels',
		'reanalysis-era5-pressure-levels',
        {
            'product_type':'reanalysis',
            'format':'netcdf',
            'variable':var,
	    'pressure_level':[
                           '1000', '850',
                           '700','500', '300'
             ],  # this is only for RH
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
            'area': [80, -40, 30, 40], # North, West, South, East. Default: global
        },
        target)


dir_out="/storage/homefs/no21h426/ERA5/geopotential/"
var="geopotential"
#var="snow_depth"
retrieve_interim(1979,1979,1,12,dir_out,var)

