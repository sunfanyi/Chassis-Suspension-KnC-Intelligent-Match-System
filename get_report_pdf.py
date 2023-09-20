# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 14:49:26 2021

@author: Fanyi Sun
"""

import sys
import shutil

from create_dir import create_dir

sys.path.append(r'Database Establishment')
from get_files import get_VehFilePath_and_PdfPath

database_paths = [r"D:\Desktop\database"]

         
vehicle_file_paths, general_data_paths = \
                        get_VehFilePath_and_PdfPath(database_paths)
                        
with open('Vehicle Summary.txt','r') as f:
    vehicle_identities = f.readlines()
    vehicle_identities = vehicle_identities[1::2]

# for i in general_data_paths:
#     print(i)
    
print(len(general_data_paths))
print(len(vehicle_identities))


# copy files：
for i in range(len(general_data_paths)): 
    dir = r'D:\Desktop\Vehicle Report\\'
    create_dir(dir,True)
    vehicle_identity = vehicle_identities[i].strip('\n')
    new_file = dir + vehicle_identity + '.pdf'
    shutil.copyfile(general_data_paths[i],new_file)
 
 
