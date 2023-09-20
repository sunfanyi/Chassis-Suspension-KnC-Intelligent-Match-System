# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:22:45 2021

@author: Fanyi Sun
"""

import pandas as pd

from get_curve_paths import get_curve_paths
from veh_key_data import VehKeyData
from detailed_similarity import VehSimilarity
from overall_similarity import OverallSimilarity


def main_similarity(target_veh, veh_identities, store_path, weight):
    df_vehicles = pd.read_csv(store_path + '\\summary_data.csv')
    df_vehicles = df_vehicles.set_index('VEHICLES')
    
    result, detailed_simi = get_overall_simi(target_veh, veh_identities, 
                              store_path, df_vehicles, weight)
    if result is None:
        return None, None, None
    
    df_ranking = pd.DataFrame({'VEHICLES' : result.veh_simi.keys(),
                               'OVERALL' : result.veh_simi.values()})
    df_ranking = df_ranking.sort_values(by=['OVERALL'], ascending=False)
    df_ranking = df_ranking.reset_index(drop=True)
    df_ranking.index = df_ranking.index + 1
    pd.set_option('display.max_row', 500)
    
    allSimi = {}
    allSimi['testSimi'] = result.test_simi
    allSimi['paraSimi'] = result.para_simi
    allSimi['detailedSimi'] = detailed_simi
    
    return df_ranking, allSimi


def get_overall_simi(target_veh_identity, veh_identities,
                     store_path, df_vehicles, weight):
    
    target_VehData, target_missing = get_target_VehData(target_veh_identity,
                                                    store_path, df_vehicles)
    if target_missing:
        print('Warning! Target vehicle: %s is missing data for all tests.' 
                                                  % target_veh_identity)
        return None
    
    all_VehData = get_all_VehData(veh_identities, store_path, df_vehicles)
    
    detailed_simi = {}
    for sample_veh_identity, sample_VehData in all_VehData.items():
        if sample_veh_identity == target_veh_identity:
            continue
        if sample_VehData.all_data_missing:
            detail = None
            print('Warning! Sample vehicle: %s is missing data for all tests.' 
                                              % sample_veh_identity)
        else:
            simi = VehSimilarity(target_VehData, sample_VehData)
            detail = simi.detailed_similarity
        detailed_simi[sample_veh_identity] = detail
        
    result = OverallSimilarity(detailed_simi, weight)
    
    return result, detailed_simi


def get_target_VehData(target_veh_identity, store_path, df_vehicles):
    target_veh_name = target_veh_identity.rpartition('#')[0]
    df_target = df_vehicles[['Unnamed: 1', target_veh_name]]
    target_curve_paths = get_curve_paths(target_veh_identity, store_path)
    target_VehData = VehKeyData(df_target, target_curve_paths)
    target_missing = target_VehData.all_data_missing
    
    return target_VehData, target_missing


def get_all_VehData(veh_identities, store_path, df_vehicles):
    all_VehData = {}
    for veh_identity in veh_identities:
        print(veh_identity)
        veh_name = veh_identity.rpartition('#')[0]
        df = df_vehicles[['Unnamed: 1', veh_name]]
        curve_paths = get_curve_paths(veh_identity, store_path)
        vehicle_data = VehKeyData(df, curve_paths)
        all_VehData[veh_identity] = vehicle_data
        
    return all_VehData
        
        
'''
for vehicle, data_vehicle in result.para_simi.items():
    print('\n', vehicle)
    if data_vehicle is None:
        print(None)
        continue
    for test, data_test in data_vehicle.items():
        print(test)
        if data_test is None:
            print(data_test)
            continue
        for para, para_data in data_test.items():
            print(para)
            print(para_data)
            
for vehicle, data_vehicle in result.test_simi.items():
    print('\n', vehicle)
    if data_vehicle is None:
        print(None)
        continue
    for test, data_test in data_vehicle.items():
        print(test)
        print(data_test)'''
        
    
    
if __name__ == '__main__':
    import time
    from weight_setting import Weight
    
    start = time.time()
    store_path = r'D:\Desktop\KnC Store Path'
    target_veh = '3_Volvo 518H - V60 PHEV Sedan#JUV1055 _ ZEP864'
    with open(store_path + '\\Vehicle Summary.txt','r') as f:
        lines = f.readlines()
        veh_identities = [a.split('\t')[0] for a in lines][:6]
    
    weight = Weight()
    df_ranking, allSimi = main_similarity(target_veh, veh_identities, 
                                              store_path, weight)
    
    veh_identity = '1_Volvo Y283 - S60 Sedan#NJM397'
    testSimi = allSimi['testSimi'][veh_identity]
    paraSimi = allSimi['paraSimi'][veh_identity]
    detailedSimi = allSimi['detailedSimi'][veh_identity]
    
    end = time.time()
    print('time:%f' % (end - start))