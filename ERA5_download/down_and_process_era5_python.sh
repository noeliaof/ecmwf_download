#!/bin/bash


module load Workspace
#module load Anaconda3
#module load Python
module load CDO
## maybe you need to specify the Workspace name first OR use `Workspace/home`
#module load Workspace/home
pip install --prefix $PYTHONPACKAGEPATH cdsapi 

echo "starting download and processing"

dir1='/storage/homefs/no21h426/tmp/'
dir2='/storage/homefs/no21h426/tmp/day/'

echo 'process data and aggreate to daily time scale'
y_names=$(seq 1959 1 2021)
for i in ${y_names[@]};do
  
  echo $i 
  python download_era5_args.py $i
  f1=$(basename $dir1/*nc)
  echo $f1
  cdo daymean  $dir1/$f1 $dir2/'Daily_'$f1
  echo 'removing large hourly file'
  rm $dir1/$f1


done
