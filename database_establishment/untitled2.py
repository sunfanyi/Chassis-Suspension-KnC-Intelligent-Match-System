# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 22:39:04 2021

@author: Fanyi Sun
"""

import os
import pandas as pd
import numpy as np

import PyPDF2
import pdfplumber
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Font,Alignment,Border

# df = pd.DataFrame(np.random.randint(80, 120, size=(8,2)), 
#                     columns= ['girl', 'boy'],
#                     index=pd.MultiIndex.from_product([['English','Chinese'],
#                                                     ['like','dislike'],
#                                                     ['strongly','slightly']]))
# print(df.index)
# df = df.T

# print(df,'\n')

# a = df.index.get_loc('boy')
# print(a)
# df['English','like','slightly'].iloc[a] = 10000
# print(df.T)


df = pd.read_csv(r'..\summary_data.csv')
print(type(df))
# print(df.info)
# df = df.stack()
# df = df.set_index(['VEHICLES','Unnamed: 1'])
# df = df.set_index('VEHICLES')
print(type(df))
# df = df.loc[(df['Unnamed: 1'] == 'F_avg'),:]
df = df[['VEHICLES', 'Unnamed: 1', '1_Volvo Y283 - S60 Sedan']]
df = df.set_index('VEHICLES')
# df = df.unstack()
print(type(df))
# df = pd.DataFrame(df)
# print(df.info)
# df = df[('Test 1_Longitudinal Compliance (braking)(brake on, eng. on, ARB on)',np.nan):('Test 2_Lateral Compliance at 0mm X offset (in phase)',np.nan)]
# df = df[('Anti-Lift Front/Anti-Squat Rear Curve Fits [N/N]', 'F_avg'):('Anti-Dive Front/Anti-Lift Rear Curve Fits [N/N]','RL')]
# df = df['Test 1_Longitudinal Compliance (braking)(brake on, eng. on, ARB on)':'Test 2_Lateral Compliance at 0mm X offset (in phase)'][:-1]
df = df['Test 1_Longitudinal (acceleration)(brake off, eng. on, ARB on)':]
# df = df.loc[df['Unnamed: 1'] == 'F_avg', :]
# df = df.set_index(['VEHICLES','Unnamed: 1'])
df = df.set_index('Unnamed: 1', append=True)
# df = pd.DataFrame(df)
print(df)
print(df.loc[('Anti-Dive/Squat Curve Fits [N/N]','F_avg')].iloc[0])
# df = df.loc[:, 'F_avg']
# df = df['F_avg']

# df = pd.DataFrame(df)
# print(df)
# print(df.loc['Longitudinal Wheel Centre Compliance [mm/N]','RL'])
# df = df.loc[:,'F_avg']
# df = df.set_index('Unnamed: 1')
# print(df.index)

# a = df.index.get_loc(('Test 1_Longitudinal Compliance (braking)(brake on, eng. on, ARB on)',np.nan))
# b = df.index.get_loc('Test 2_Lateral Compliance at 0mm X offset (in phase)')
# print(a)
# path = r'D:\Desktop\txt2excel\Curves Data Processed\1_Volvo Y283 - S60 Sedan_NJM397_processed.xlsx'
# df = pd.read_excel(path)
# print(list(df['FrontLHwheelForceXN']))
a = [1,2,3,4]
print(a[:3])