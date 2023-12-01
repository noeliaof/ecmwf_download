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
                print(year)
                print(lastDate)
                print(var)
                target = dir+"ERA5_" + var +"_%04d.nc" % (year)
                print(target)
               # interim_request(year, target, var)

def interim_request(requestDates, target, var):
    c.retrieve(
                'efas-historical',
        {
            'format':'netcdf',
            'system_version': 'version_3_5',
            'variable':var,
	    #'pressure_level':'1000',  # this is only for RH
             'model_levels': 'surface_level',
            'hyear':requestDates,
            'hmonth':[
		    'april','august','december',
		    'february','january','july',
		    'june','march','may',
		    'november','october','september'
            ],
            'hday':[
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
        },
        target)

dir="/storage/homefs/no21h426/efas/"
var="river_discharge_in_the_last_6_hours"
retrieve_interim(1991,1991,1,12,dir,var)
