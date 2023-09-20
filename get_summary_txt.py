# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:38:19 2021

@author: Fanyi Sun
"""

# from Database Establishment import get_files
import sys

from create_dir import create_dir

sys.path.append(r'Database Establishment')
from get_files import get_VehFilePath_and_PdfPath, get_test_data_paths



database_paths = [r"D:\Desktop\database"]
vehicle_file_paths, general_data_paths = \
                        get_VehFilePath_and_PdfPath(database_paths)
                        
with open('Vehicle Summary.txt','r') as f:
    vehicle_identities = f.readlines()

total = []
for vehicle in vehicle_file_paths:
    file_paths = {}
    file_paths = get_test_data_paths(vehicle,'summary.txt')
    total.append(file_paths)

total_dict = {}
for key in total[0].keys():
    total_dict[key] = []
    for dict in total:
        if not dict[key]:
            total_dict[key].append(None)
        else:
            if type(dict[key]) == list:
                total_dict[key].append(dict[key][0])
            else:
                total_dict[key].append(dict[key])
    

                        
for test_number in total_dict.keys():
    i = 1
    print(test_number,':',len(total_dict[test_number]))
    directory = r'D:\Desktop\summary of summary\\' + test_number + '\\'
    create_dir(directory,True)
    
    # print(directory)
    
    for vehicle in total_dict[test_number]:
        vehicle_identity = vehicle_identities[i].strip('\n')
        i += 2
        try:
            with open(vehicle,'r') as f:
                info = f.read()
            file_path = directory + vehicle_identity + '.txt'
            # print(file_path)
            with open(file_path,'w') as f:
                f.write(info)
        except:
            pass
            
            
            
            
# =============================================================================
# # method 1 (slower)
# # vehicle_file_paths, general_data_paths = \
# #                         get_VehFilePath_and_PdfPath(database_paths)
# 
# # total_df_general, vehicle_identities, vehicle_names = \
# #                     generate_total_df_general(general_data_paths)
#                   
#                     
#                   
# # method 2 (faster but need variables 'vehicle_identities' to be stored in advanced)          
# vehicle_file_paths, general_data_paths = \
#                         get_VehFilePath_and_PdfPath(database_paths)
# =============================================================================
            
            
            
            
            
            
            
            
            
# =============================================================================
# from get_files import get_test_file_paths
# 
# path = r"D:\Desktop\txt2excel\database"
# 
# file_paths = {}
# file_paths = get_test_file_paths(path,'summary.txt')
# 
# # print(file_paths)
# 
# for test_number in file_paths.keys():
#     print(test_number,':',len(file_paths[test_number]))
#     directory = "D:\Desktop\summary of summary\\" + test_number + '\\'
#     # print(directory)
#     for vehicle in file_paths[test_number]:
#         with open(vehicle,'r') as f:
#             info = f.read()
#         vehicle_name = vehicle.strip('D:\\Desktop\\txt2excel\\database\\')
#         vehicle_name = vehicle_name.split('\\')[0]
#         file_path = directory + vehicle_name + '.txt'
#         # print(file_path)
#         with open(file_path,'w') as f:
#             f.write(info)
# =============================================================================
