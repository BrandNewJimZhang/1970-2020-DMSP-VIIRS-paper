###################################################################
# File:        ./DMSP_continuity_calibration.py                   #
# Author:      Haowen Zhang, Jianxi Zhang                         #
# Date:        2024-03-16                                         #
# Description: This script is used to perform continuity          #
#              calibration on the DMSP data.                      #
# Contact:     zhang-hw22@mails.tsinghua.edu.cn                   #
###################################################################

import os
import numpy as np, pandas as pd, xarray as xr, rioxarray as rxr

# Define DMSP data directory
# DMSP_dir: str = 'E:/DMSP-VIIRS/DMSP'
DMSP_dir: str = './DMSP'
# The DMSP data directory should be changed to your own directory, in our case it is 'E:/DMSP-VIIRS/DMSP'
df: pd.DataFrame = pd.read_csv(f'{DMSP_dir}/radiometric_calibration.csv')

# Load the DMSP data
DMSP_files: list = [f for f in os.listdir(DMSP_dir) if f.endswith('.tif')]
DMSP_files: np.ndarray = np.array(DMSP_files)
years: np.ndarray = df['Year'].values
df_year_file_mapping = pd.DataFrame(np.vstack((years, DMSP_files)).T, columns=['Year', 'File'])

# Identify the years with multiple DMSP files
years_with_multiple_files: np.ndarray = df_year_file_mapping['Year'].value_counts()[df_year_file_mapping['Year'].value_counts() > 1].index.values

RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

raise AssertionError(f"{RED}{BOLD}The following code is not implemented yet.{RESET}")

a = []

a_all = list(set(iss[:-1]))
a_all.sort(key=lambda x: int(x), reverse=False)

for i in iss:
  if iss.count(i)>1:
    a.append(int(i))
print (a)

ls = list(set(a[:-2]))
ls.sort(key=lambda x: x, reverse=False)
for i in ls:
   print(i)



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
