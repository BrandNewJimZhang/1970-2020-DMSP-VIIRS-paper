###################################################################
# File:        ./DMSP_radiometric_calibration.py                  #
# Author:      Haowen Zhang, Jianxi Zhang                         #
# Date:        2024-03-12                                         #
# Description: This script is used to perform radiometric         #
#              calibration on the DMSP data.                      #
# Contact:     zhang-hw22@mails.tsinghua.edu.cn                   #
###################################################################

import os 

import numpy as np, pandas as pd, xarray as xr, rioxarray as rxr
import matplotlib.pyplot as plt, seaborn as sns
import rioxarray 
from scipy import stats

from tqdm import tqdm

# Define DMSP data directory
DMSP_dir: str = './DMSP' 
# The DMSP data directory `DMSP_dir` should be changed to your own directory, in our case it is './DMSP'

# Load the DMSP data
DMSP_files: list[str] = [f for f in os.listdir(DMSP_dir) if f.endswith('.tif')]

# Create empty lists to store the slope, intercept, and R2 values of the linear regression
slope_list: list[np.float64] = []
exp_list: list[np.float64] = []
r2_score_list: list[np.float64] = []

# Radiometric calibration using 2006 data
DMSP_base_data = rxr.open_rasterio(f'{DMSP_dir}/calibration/F16_20051128-20061224_rad_v4.avg_vis.tif')

# Estimated time for below loop (Tested on Mac Mini, 2020, M1, 16GB RAM): 5~6 minutes
for DMSP_file in tqdm(DMSP_files):
    DMSP_data = rxr.open_rasterio(f'{DMSP_dir}/{DMSP_file}')
    
    # Identify valid (non-zero) radiometric values in both the current and base DMSP data
    _, index = DMSP_data.values.reshape(1, -1).nonzero()
    _, index_base = DMSP_base_data.values.reshape(1, -1).nonzero()

    # Find the intersection of the non-zero value indices from both the current and base DMSP data
    inter = np.intersect1d(index, index_base)

    slope, intercept, r_value, p_value, std_err = stats.linregress(
        np.log(DMSP_data.values.reshape(1, -1)[0][inter]).astype('float16'),
        np.log(DMSP_base_data.values.reshape(1, -1)[0][inter]).astype('float16')
    )

    # Append the slope, intercept, and R2 values to the corresponding lists
    slope_list.append(slope)
    exp_list.append(np.exp(intercept))
    r2_score_list.append(r_value ** 2)

satellites = ['F10', 'F10', 'F10', 'F12', 'F12', 'F12', 'F12', 'F12', 'F12', 'F14', 'F14', 'F14', 'F14', 'F14', 'F14', 'F14', 'F15', 'F15', 'F15', 'F15', 'F15', 'F15', 'F15', 'F15', 'F16', 'F16', 'F16', 'F16', 'F16', 'F16', 'F18', 'F18', 'F18', 'F18']
years = [1992, 1993, 1994, 1994, 1995, 1996, 1997, 1998, 1999, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]

# Write the satellites, years, slope, intercept, and R2 values to a csv file
matrix = np.array([satellites, years, slope_list, exp_list, r2_score_list]).T
df = pd.DataFrame(matrix, columns=['Satellite', 'Year', 'Slope', 'Intercept', 'R2'])
df.to_csv(f'{DMSP_dir}/radiometric_calibration.csv', index=False)
