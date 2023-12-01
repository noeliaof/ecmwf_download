#!/bin/bash

module load Python
## maybe you need to specify the Workspace name first OR use `Workspace/home`
module load Workspace/home
pip install --prefix $PYTHONPACKAGEPATH cdsapi 

echo "starting download and processing"

python down_era5_cc.py
