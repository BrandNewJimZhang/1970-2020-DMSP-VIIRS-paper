###################################################################
# File:        ./radiometric_calibration.py                       #
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

# Define DMSP data directory
DMSP_dir = 'E:/DMSP-VIIRS/DMSP' 
# The DMSP data directory should be changed to your own directory, in our case it is 'E:/DMSP-VIIRS/DMSP'

# Load the DMSP data
DMSP_files = [f for f in os.listdir(DMSP_dir) if f.endswith('.tif')]

# Create empty lists to store the slope, intercept, and R2 values of the linear regression
slope_list, exp_list, r2_score_list = [], [], []

# Radiometric calibration using 2006 data
for DMSP_file in DMSP_files:
    DMSP_data = rxr.open_rasterio(f'{DMSP_dir}/{DMSP_file}')
    DMSP_base_data = rxr.open_rasterio(f'{DMSP_dir}/observation/F16_20051128-20061224_rad_v4.avg_vis.tif')

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

# Write the slope, intercept, and R2 values to a csv file
exp_array = np.array(exp_list).reshape(-1, 1)
slope_array = np.array(slope_list).reshape(-1, 1)
r2_score_array = np.array(r2_score_list).reshape(-1, 1)


#! TO DO: Some issues occur here.
pd2=np.append(new_exp,new_b,axis=1)
pd2=np.append(pd2,new_r2,axis=1)

pd2=pd.DataFrame(pd2,columns=['a','b','R2'])
pd2.to_excel(excel_writer='E:\\DMSP-VIIRS\\DMSP\\定标\\1饱和校正.xlsx')
pd2