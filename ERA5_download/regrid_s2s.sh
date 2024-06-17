#!/bin/bash

dir1='/srv/data/ERA5-LAND/day/'
dir2='/srv/data/ERA5-LAND/day_S2Sgrid/'
topo='/home/fe/oterofelipe/ecmwf_download/ERA5_download/template.nc'

cd $dir1
for i in *nc;do
  
  f1=$(basename $i)
  echo 'regridding to a S2S grid'
  cdo -f nc -remapbil,$topo $f1 $dir2/'Daily_1.5_'$f1

done
