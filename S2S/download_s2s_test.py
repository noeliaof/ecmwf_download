#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
from pprint import pprint
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

server = ECMWFDataServer()
server.retrieve({
    "class": "s2",
    "dataset": "s2s",
    "date": "2021-12-30",
    "expver": "prod",
    "hdate": ["2001-12-30"],
    "levtype": "sfc",
    "model": "glob",
    "origin": "ecmf",
    "param": "165",
    "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168/174/180/186/192/198/204/210/216/222/228/234/240/246/252/258/264/270/276/282/288/294/300/306/312/318/324/330/336/342/348/354/360/366/372/378/384/390/396/402/408/414/420/426/432/438/444/450/456/462/468/474/480/486/492/498/504/510/516/522/528/534/540/546/552/558/564/570/576/582/588/594/600/606/612/618/624/630/636/642/648/654/660/666/672/678/684/690/696/702/708/714/720/726/732/738/744/750/756/762/768/774/780/786/792/798/804/810/816/822/828/834/840/846/852/858/864/870/876/882/888/894/900/906/912/918/924/930/936/942/948/954/960/966/972/978/984/990/996/1002/1008/1014/1020/1026/1032/1038/1044/1050/1056/1062/1068/1074/1080/1086/1092/1098/1104",
    "stream": "enfh",
    "time": "00:00:00",
    "type": "cf",
    "target": "output",
})
