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
DMSP_dir: str = './DMSP'
# The DMSP data directory should be changed to your own directory, in our case it is './DMSP'
df: pd.DataFrame = pd.read_csv(f'{DMSP_dir}/radiometric_calibration.csv')

# Load the DMSP data
DMSP_files: list = [f for f in os.listdir(DMSP_dir) if f.endswith('.tif')]
DMSP_files: np.ndarray = np.array(DMSP_files)
years: np.ndarray = df['Year'].values
df_year_file_mapping = pd.DataFrame(np.vstack((years, DMSP_files)).T, columns=['Year', 'File'])

# Identify the years with multiple DMSP files
years_with_multiple_files: np.ndarray = df_year_file_mapping['Year'].value_counts()[df_year_file_mapping['Year'].value_counts() > 1].index.values
years_with_multiple_files = years_with_multiple_files.astype(int)
years_with_multiple_files.sort()

RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

'''
Equation (2) in the paper.
'''

for year in years_with_multiple_files:
    # Get the DMSP files for the current year
    files: np.ndarray = df_year_file_mapping[df_year_file_mapping['Year'] == year]['File'].values
    # Get the corresponding a and b values for the current year
    slope_values: np.ndarray = df[df['Year'] == year]['Slope'].values
    intercept_values: np.ndarray = df[df['Year'] == year]['Intercept'].values

    # Load the DMSP files
    DMSP_files


    
    
raise AssertionError(f"{RED}{BOLD}The following code is not implemented yet.{RESET}")

# equation(2)
dp = pd.read_excel('E:\\DMSP-VIIRS\\DMSP\\dingbiao\\1饱和校正.xlsx')

values_1 = {}

for i in ls[:]:
    ds = rioxarray.open_rasterio('E:\\DMSP-VIIRS\\DMSP\\'+pd3[pd3['时间']==i]['数据'].iloc[0])
    a = dp[(dp.卫星序号==pd3[pd3['时间']==i]['数据'].iloc[0][:3]) & (dp.年份==i)]['a'].iloc[0]
    b = dp[(dp.卫星序号==pd3[pd3['时间']==i]['数据'].iloc[0][:3]) & (dp.年份==i)]['b'].iloc[0]
    ds = a*(ds.values.reshape(1,-1)[0].astype('float32')**b)

    ds1 = rioxarray.open_rasterio('E:\\DMSP-VIIRS\\DMSP\\'+pd3[pd3['时间']==i]['数据'].iloc[1])
    a1 = dp[(dp.卫星序号==pd3[pd3['时间']==i]['数据'].iloc[1][:3]) & (dp.年份==i)]['a'].iloc[0]
    b1 = dp[(dp.卫星序号==pd3[pd3['时间']==i]['数据'].iloc[1][:3]) & (dp.年份==i)]['b'].iloc[0]
    ds1 = a1*(ds1.values.reshape(1,-1)[0].astype('float32')**b1)

    print(ds)
    print(ds1)
    index3 = ds.nonzero()
    index4= ds1.nonzero()

    inter=np.intersect1d(index3,index4)

    zeros=np.zeros_like(ds)
    zeros[inter]=(ds[inter]+ds1[inter])/2
    
    print(len(ds))
    print(len(ds1))
    print(len(zeros))
    print(zeros)
    

    values_1['{}'.format(i)]=zeros
    print(values_1)
    print('*****')
