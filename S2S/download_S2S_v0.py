#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
origin = "ecmf"
 
# Step 1: Select a Model Version Date
modelVersionDate = "2021-12-30"
 
# Step 2: Set the hindcast Dates you wish to request
# For the model version "2015-12-03" the available hindcast dates are listed below:
hindcastDates = ["2001-12-30", "2002-12-30", "2003-12-30", "2004-12-30", "2005-12-30", "2006-12-30",
                 "2007-12-30", "2008-12-30", "2009-12-30", "2010-12-30", "2011-12-30", "2012-12-30", "2013-12-30",
                 "2014-12-30", "2015-12-30", "2016-12-30", "2017-12-30", "2018-12-30", "2019-12-30", "2020-12-30"]
 
def retrieve_ECMWF_reforecast():
    """
       A function to demonstrate how to retrieve efficiently all hindcastDates
       for a particular ECMWF reforecast model version.
       Change the variables below to adapt the request to your needs
    """
    mdir = '/storage/homefs/no21h426/S2S_data_test/' 
    
    # Please note that the "sfc" and "pl" requests below could run in parallel
    # Step 1: Get pressure level data
    pfplTarget = "%s%s_%s_%s.grb"%( mdir, origin, "pfpl", modelVersionDate)
    ECMWF_reforecast_pf_pl_request("/".join(hindcastDates), pfplTarget)
    
    # Step 2: Get surface data
    pfsfcTarget = "%s%s_%s_%s.grb"%(mdir, origin, "pfsfc", modelVersionDate)
    #pfsfcTarget = "%s_%s_%s.grb" % (origin, "pfsfc", modelVersionDate)
    ECMWF_reforecast_pf_sfc_request("/".join(hindcastDates), pfsfcTarget)
 
def ECMWF_reforecast_pf_pl_request(hindcastDate, target):
    """
       An ECMWF reforecast, perturbed forecast, pressure level, request.
       Change the keywords below to adapt it to your needs. (eg to add or remove some steps or parameters etc)
    """
    server.retrieve({
        "class": "s2",
        "dataset": "s2s",
        "date": modelVersionDate,
        "expver": "prod",
        "hdate": hindcastDates,
        "levtype": "pl",
        "levelist": "300/500/850/1000",
        "origin": origin,
        "param": "156",
        "step": "24/to/768/by/24",
        "stream": "enfh",
        "target": target,
        "time": "00",
        "number": "1/2/3/4",
        "type": "pf",
    })
def ECMWF_reforecast_pf_sfc_request(hindcastDate, target):
    """
    An ECMWFreforecast, perturbed forecast, sfc request.
       Change the keywords below to adapt it to your needs. (eg to add or remove some steps or parameters etc)
    """
    server.retrieve({
        "class": "s2",
        "dataset": "s2s",
        "date": modelVersionDate,
        "expver": "prod",
        "hdate": hindcastDate,
        "levtype": "sfc",
        "origin": origin,
        "param": "151/165/166",
        "step": "24/to/744/by/24",
        "stream": "enfh",
        "target": target,
        "time": "00",
        "number": "1/2/3/4",
        "type": "pf",
    })
if __name__ == '__main__':
    retrieve_ECMWF_reforecast()
