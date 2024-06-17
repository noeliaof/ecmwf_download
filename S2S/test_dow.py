#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

server.retrieve({
    "class": "s2",
    "dataset": "s2s",
    "date": "2024-01-01/to/2024-01-31",
    "expver": "prod",
    "levtype": "sfc",
    "model": "glob",
    "origin": "ecmf",
    "param": "168",
    "step": "0-24/24-48/48-72/72-96/96-120/120-144/144-168/168-192/192-216/216-240/240-264/264-288/288-312/312-336/336-360/360-384/384-408/408-432/432-456/456-480/480-504/504-528/528-552/552-576/576-600/600-624/624-648/648-672/672-696/696-720/720-744/744-768/768-792/792-816/816-840/840-864/864-888/888-912/912-936/936-960/960-984/984-1008/1008-1032/1032-1056/1056-1080/1080-1104",
    "stream": "enfo",
    "time": "00:00:00",
    "type": "cf",
    "target": "output"
})