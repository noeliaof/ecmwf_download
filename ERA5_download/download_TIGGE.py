#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ti",
    "dataset": "tigge",
    "date": "2021-05-01/to/2021-05-31",
    "expver": "prod",
    "grid": "0.5/0.5",
    "levtype": "sfc",
    "origin": "ecmf",
    "param": "136/167",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240",
    "time": "00:00:00/12:00:00",
    "type": "fc",
    "target": "output",
})
