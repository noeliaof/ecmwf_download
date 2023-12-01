#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
import os,sys
import pandas as pd
from datetime import datetime
import utils.date_to_model  as d2m
# to avoid problems with the certificated
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


server = ECMWFDataServer()

#product = 'forecast' # forecast, hincast
product = 'hindcast' # forecast, hincast
dirbase = '/srv/data/data_oterofelipe_springenberg/'
dir = '%s/%s/%s/'%(dirbase,product,'/ECMWF/sfc')

if product == 'hindcast':
    STREAM =  'enfh'
elif product == 'forecast':
    STREAM = 'enfo'

basedict = {
    'class': 's2',
    'dataset': 's2s',
    'expver': 'prod',
    'model': 'glob',
    'origin': 'ecmf',
    'stream': STREAM ,
    'time': '00:00:00'
}

l = range(0,1128,24)
paired = ['-'.join([str(v) for v in l[i:i + 2]]) for i in range(len(l))]
final = '/'.join(paired[0:-1])

meta = {
    'tp': {
        'param': '228228',
        'levtype': 'sfc',
        #'step': '/'.join(['%i'%i for i in range(0,1128,24)])
        'step': '0/to/1104/by/24'
    },

     't2m': {
        'param': '167',
        'levtype': 'sfc',
        'step': '/'.join([final])
    },

     'sst': {
        'param': '34',
        'levtype': 'sfc',
        'step': '/'.join([final])
    },

     'u10': {
        'param': '165',
        'levtype': 'sfc',
       # 'step': '0/to/1104/by/24'
        'step': '0/to/1104/by/6'
    },

    'v10': {
        'param': '166',
        'levtype': 'sfc',
       # 'step': '0/to/1104/by/24'
        'step': '0/to/1104/by/6'
    },

    'mslp': {
        'param': '151',
        'levtype': 'sfc',
        'step': '0/to/1104/by/24'
    },

    'z': {
        'param': '156',
        'levelist': '500',
        'levtype': 'pl',
        'step': '0/to/1104/by/24'
    },
    'u': {
        'param': '131',
        'levelist': '300/925',
        'levtype': 'pl',
        'step': '0/to/1104/by/24'
    },
    'v': {
        'param': '132',
        'levelist': '300/925',
        'levtype': 'pl',
        'step': '0/to/1104/by/24'
    }
}

#dates_monday = pd.date_range("20190701", periods=52, freq="7D") # forecasts start Monday
# to complete 2021 just get half of the rest year
dates_monday = pd.date_range("20210104", periods=52, freq="7D") # forecasts start Monday
#dates_monday = pd.date_range("20210705", periods=52, freq="7D") # forecasts start Monday
#dates_thursday = pd.date_range("20190704", periods=52, freq="7D") # forecasts start Thursday
dates_thursday = pd.date_range("20210107", periods=52, freq="7D") # forecasts start Thursday
#dates_thursday = pd.date_range("20210708", periods=52, freq="7D") # forecasts start Thursday
dates_fcycle = dates_monday.union(dates_thursday)

for filename in (
   # 'tp',
   # 't2m',
   # 'sst',
   # 'mslp',
   # 'z',
   # 'u10',
   # 'v10',
   # 'u',
    'v',
):
    for prefix in (
        'pf',
        'cf',
    ):
        for dates in dates_fcycle:
            d = dates.strftime('%Y-%m-%d')
            refyear = int(d[:4])
            datadir = '%s/%s'%(dir,filename)
            if not os.path.exists(datadir)  :
                os.makedirs(datadir)
            hdate = '/'.join([d.replace('%i'%refyear,'%i'%i) for i in range(refyear-20,refyear)])
            forcastcycle = d2m.which_mv_for_init(d,model='ECMWF',fmt='%Y-%m-%d')
            target = '%s/%s_%s_%s_%s_%s.grb'%(datadir,filename,forcastcycle,d,prefix,product)
            if not os.path.isfile(target):
               dic = basedict.copy()
               for k,v in meta[filename].items():
                   dic[k] = v
               dic['date'] = d
               dic['type'] = prefix
               if ( product == 'hindcast' ):
                   dic['hdate'] = hdate
                   if prefix == 'pf':
                       dic['number'] =  '1/to/10'
               if ( product == 'forecast' ):
                   if prefix == 'pf':
                       dic['number'] =  '1/to/50'
               dic['target'] = target
               print(dic)
               if server is not None:
                   server.retrieve(dic)

print('DONE')
