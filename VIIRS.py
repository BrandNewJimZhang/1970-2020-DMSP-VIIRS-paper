###################################################################
# File:        ./VIIRS.py                                         #
# Author:      Haowen Zhang, Jianxi Zhang                         #
# Date:        2024-03-24                                         #
# Description: ******                                             #
# Contact:     zhang-hw22@mails.tsinghua.edu.cn                   #
###################################################################

import os, re
import numpy as np, xarray as xr, rioxarray as rxr
from osgeo import gdal, gdalconst

# Part 1: Load the VIIRS data

