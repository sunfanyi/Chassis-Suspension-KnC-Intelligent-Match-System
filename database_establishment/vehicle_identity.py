# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 10:51:51 2021

@author: Fanyi Sun
"""

import os

def write_veh_identity(veh_file_paths, pdf_data_paths, 
                       veh_identities, store_path):
    """
    if the database is changed, this function must be used after the 
    function: generate_total_df_vehicle() from  generate_vehicle_data_df
    """
        
    # create a txt file containing the vehicle_name and VehID for each vehicle
    i = 0
    for file_path in veh_file_paths:
        print(file_path)
        txt_path = file_path + '\\vehicle_identity.txt'
        with open(txt_path,'w') as f:
            # veh_identities[i] = veh_identities[i].replace('/','&')
            f.write(veh_identities[i])
        i += 1
    
    summary_path = '%s\\Vehicle Summary.txt' % store_path
    with open(summary_path,'w',encoding='utf-8') as f:
        for i in range(len(veh_identities)):
            
            f.write(veh_identities[i] + '\t')
            f.write(veh_file_paths[i] + '\t')
            f.write(pdf_data_paths[i] + '\n')
            
        # f.write(str(len(veh_identities)))
            
        
    
# no longer useful
def find_vehicle_identity(vehicle_path):
    # find the vehicle identity from the path by finding the txt
    for dir in os.listdir(vehicle_path):    
        if dir == 'vehicle_identity.txt':
            txt_path = os.path.join(vehicle_path, dir)
            with open(txt_path,'r') as f:
                return f.read()
        
        
if __name__ == '__main__':
    # normally don't call this function at the main module
    write_veh_identity(veh_file_paths, veh_identities)
    
