###################################################################
# File:        ./continuity_calibration.py                        #
# Author:      Haowen Zhang, Jianxi Zhang                         #
# Date:        2024-03-16                                         #
# Description: This script is used to perform continuity          #
#              calibration on the DMSP data.                      #
# Contact:     zhang-hw22@mails.tsinghua.edu.cn                   #
###################################################################

import os
import numpy as np, pandas as pd, xarray as xr, rioxarray as rxr

# Define DMSP data directory
DMSP_dir = 'E:/DMSP-VIIRS/DMSP'
# The DMSP data directory should be changed to your own directory, in our case it is 'E:/DMSP-VIIRS/DMSP'
df = pd.read_csv(f'{DMSP_dir}/radiometric_calibration.csv')

# Load the DMSP data

DMSP_files = [f for f in os.listdir(DMSP_dir) if f.endswith('.tif')]

'''
filelist = os.listdir(r'E:\DMSP-VIIRS\DMSP')
pd_file = pd.DataFrame(filelist[:-4])

pd_ap = []
for i in pd_file.iloc[:,0]:
    pd_ap.append(int(i[3:7]))

pd_ap = np.array(pd_ap).reshape(-1,1)
pd_file= np.array(pd_file).reshape(-1,1)

pd3 = np.append(pd_ap,pd_file,axis=1)
pd3 = pd.DataFrame(pd3,columns=['时间','数据'])
pd3
'''
