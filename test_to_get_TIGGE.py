#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
from ecmwfapi.api import APIException
import calendar
import os
from fire import Fire
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

var_dict = {
    '2m_temperature': '167',
    'total_column_water': '136',
    '10m_u_component':'165',
    '10m_v_component':'165'
}

PATH_OUT = '/storage/homefs/no21h426/tmp/'

def retrieve_data(var, years=[2020, 2021], month_start=1, month_end=12, path=PATH_OUT, ens=False):

    server = ECMWFDataServer()
    months = range(month_start, month_end+1)
    for year in years:
        for month in months:

            try:
                days = calendar.monthrange(year, month)[1]
                month = str(month).zfill(2)
                if var == 'z':
                    print('download geopotential')
                    params = {
                        "class": "ti",
                        "dataset": "tigge",
                        "date": f"{year}-{month}-01/to/{year}-{month}-{days}",
                        "expver": "prod",
                        "grid": "0.5/0.5",
                        "levelist": "200/300/500/850/1000",
                        "levtype": "pl",
                        "origin": "ecmf",
                        "param": "156",
                        "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360",
                        "time": "00:00:00/12:00:00",
                        "type": "cf",
                        "target": f"{path}/geopotential/geopotential{'_ens' if ens else ''}_{year}_{month}_raw.grib",
                    }
                elif var == 't':
                    params = {
                        "class": "ti",
                        "dataset": "tigge",
                        "date": f"{year}-{month}-01/to/{year}-{month}-{days}",
                        "expver": "prod",
                        "grid": "0.5/0.5",
                        "levelist": "200/300/500/850/1000",
                        "levtype": "pl",
                        "origin": "ecmf",
                        "param": "130",
                        "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360",
                        "time": "00:00:00/12:00:00",
                        "type": "cf",
                        "target": f"{path}/temperature_850/temperature_850{'_ens' if ens else ''}_{year}_{month}_raw.grib",
                    }
                elif var in var_dict.keys():
                    params = {
                        "class": "ti",
                        "dataset": "tigge",
                        "date": f"{year}-{month}-01/to/{year}-{month}-{days}",
                        "expver": "prod",
                        "grid": "0.703125/0.703125",
                        # "levelist": "850",
                        "levtype": "sfc",
                        "origin": "ecmf",
                        "param": var_dict[var],
                        # "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360",
                        "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120",
                        "time": "00:00:00/12:00:00",
                        "type": "cf",
                        "target": f"{path}/{var}/{var}{'_ens' if ens else ''}_{year}_{month}_raw.grib",
                    }
                if ens:
                    params['number'] = "1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50"
                    params['step'] = "0/24/48/72/96/120/144/168"
                    params['type'] = "pf"
            
                os.makedirs('/'.join(params['target'].split('/')[:-1]), exist_ok=True)
                server.retrieve(params)

            except APIException:
                print(f'Damaged files {year}-{month}-01/to/{year}-{month}-{days}')



# call function

retrieve_data('z')
