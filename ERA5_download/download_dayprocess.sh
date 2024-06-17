#!/bin/bash


#module load Workspace
#module load Anaconda3
#module load Python
#module load CDO
## maybe you need to specify the Workspace name first OR use `Workspace/home`
#module load Workspace/home
#pip install --prefix $PYTHONPACKAGEPATH cdsapi 

echo "starting download and processing"

dir1='/srv/data/ERA5-LAND/'
dir2='/srv/data/ERA5-LAND/day/'
dir3='/srv/data/ERA5-LAND/day_S2Sgrid/'
topo='/home/fe/oterofelipe/ecmwf_download/ERA5_download/template.nc'

echo 'process data and aggreate to daily time scale'
y_names=$(seq 2000 1 2023)
for i in ${y_names[@]};do
  
  echo $i 
  python download_era5land_args.py $i
  f1=$(basename $dir1/*nc)
  echo $f1
  cdo daymean  $dir1/$f1 $dir2/'Daily_'$f1
  echo 'removing large hourly file'
  rm $dir1/$f1

done
