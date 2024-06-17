
import os
import ssl
import logging
from ecmwfapi import ECMWFDataServer
import pandas as pd
from datetime import datetime
import utils.date_to_model as d2m

ssl._create_default_https_context = ssl._create_unverified_context

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ECMWFDataRetriever:
    """
    A class for retrieving ECMWF data based on specified parameters.

    Args:
    - product (str): The type of product, either 'hindcast' or 'forecast'.
    - level_type (str): The type of level, e.g., 'sfc' for surface or 'pl' for pressure levels.
    - meta_json (dict): JSON metadata containing information about different parameters.
    - dates_fcycle (DatetimeIndex): Combined dates for forecast cycles.
    - dirbase (str): main directory to the data
    
    Attributes:
    - product (str): The type of product, either 'hindcast' or 'forecast'.
    - level_type (str): The type of level, e.g., 'sfc' for surface or 'pl' for pressure levels.
    - server (ECMWFDataServer): An instance of ECMWFDataServer for data retrieval.
    - dir (str): The directory for storing data specific to the product and level type.
    - stream (str): The data stream based on the product type.
    

    Methods:
    - retrieve_data(var, prefix): Retrieves data based on specified parameters.

    Example:
    ```python
    retriever = ECMWFDataRetriever('hindcast', 'sfc', meta_json)
    retriever.retrieve_data('t2m', 'pf')
    ```

    Note:
    Ensure you have the required libraries and logger instance before using this class.
    """

    def __init__(self, product, level_type, meta_json, dates_fcycle, dirbase):
        
        self.product = product
        self.level_type = level_type
        self.metadata = meta_json
        self.server = ECMWFDataServer()
        self.dates_fcycle = dates_fcycle
        self.dirbase = dirbase
        self.dir = f'{self.dirbase}/{self.product}/ECMWF/{self.level_type}/'

        if self.product == 'hindcast':
            self.stream = 'enfh'
        elif self.product == 'forecast':
            self.stream = 'enfo'

        self.basedict = {
            'class': 's2',
            'dataset': 's2s',
            'expver': 'prod',
            'model': 'glob',
            'origin': 'ecmf',
            'stream': self.stream,
            'time': '00:00:00'
        }


    def retrieve_data(self, var, prefix):
        for dates in self.dates_fcycle:
            d = dates.strftime('%Y-%m-%d')
            refyear = int(d[:4])
            datadir = f'{self.dir}/{var}'
            print(datadir)
            if not os.path.exists(datadir):
                os.makedirs(datadir)
            
            hdate = '/'.join([d.replace('%i' % refyear, '%i' % i) for i in range(refyear - 20, refyear)])
            forcastcycle = d2m.which_mv_for_init(d, model='ECMWF', fmt='%Y-%m-%d')
            target = f'{datadir}/{var}_{forcastcycle}_{d}_{prefix}_{self.product}.grb'
            if not os.path.isfile(target):
                dic = self.basedict.copy()
                for k, v in self.metadata[var].items():
                    dic[k] = v
                dic['date'] = d
                dic['type'] = prefix
                if self.product == 'hindcast':
                    dic['hdate'] = hdate
                    if prefix == 'pf':
                        dic['number'] = '1/to/10'
                if self.product == 'forecast':
                    if prefix == 'pf':
                        dic['number'] = '1/to/50'
                dic['target'] = target
                logger.info(dic)
                if self.server is not None:
                    self.server.retrieve(dic)
