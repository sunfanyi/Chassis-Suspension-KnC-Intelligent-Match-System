# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:35:42 2021

@author: Fanyi Sun
"""

import numpy as np


class OverallSimilarity():
    def __init__(self, detailed_similarity, weight):
        self.detailed_similarity = detailed_similarity
        self.weight = weight
        self.find_parameter_similarity()
        self.find_test_similarity()
        self.find_vehicle_similarity()
        
    
    def find_parameter_similarity(self):
        self.para_simi = {}
        for vehicle, data_vehicle in self.detailed_similarity.items():
            if data_vehicle is None:
                self.para_simi[vehicle] = None
                continue
            
            self.para_simi[vehicle] = {}
            for test, data_test in data_vehicle.items():
                if data_test is None:
                    self.para_simi[vehicle][test] = None
                    continue
                    
                self.para_simi[vehicle][test] = {}
                for para, data_para in data_test.items():
                    simi = []
                    data_missing = False
                    for feature, value in data_para.items():
                        wt_feature = eval('self.weight.wt_%s[para][feature]' 
                                              % test)
                        if value is None:
                            # to be used in __process_missing_data
                            simi.append([np.nan,wt_feature])
                            data_missing = True
                        else:
                            simi.append(value * wt_feature)
                    if data_missing:
                        simi = self.__process_missing_data(simi)
                    simi = np.sum(simi)
                    self.para_simi[vehicle][test][para] = simi
    
    
    def find_test_similarity(self):
        self.test_simi = {}
        for vehicle, data_vehicle in self.para_simi.items():
            # print(vehicle)
            if data_vehicle is None:
                self.test_simi[vehicle] = None
                continue
            
            self.test_simi[vehicle] = {}
            for test, data_test in data_vehicle.items():
                if data_test is None:
                    self.test_simi[vehicle][test] = None
                    continue
                
                simi = []
                data_missing = False
                for para, data_para in data_test.items():
                    wt_para = eval("self.weight.wt_%s[para]['weight']" % test)
                    if data_para is None:
                        simi.append([np.nan,wt_para])
                        data_missing = True
                    else:
                        simi.append(data_para * wt_para)
                if data_missing:
                    # print(para)
                    # print(simi)
                    simi = self.__process_missing_data(simi)
                simi = np.sum(simi)
                self.test_simi[vehicle][test] = simi
                    
    
    def find_vehicle_similarity(self):
        self.veh_simi = {}
        for vehicle, data_vehicle in self.test_simi.items():
            if data_vehicle is None:
                self.veh_simi[vehicle] = None
                continue
            
            simi = []
            data_missing = False
            for test, data_test in data_vehicle.items():
                wt_test = eval("self.weight.wt_overall[test]")
                if data_test is None:
                    simi.append([np.nan,wt_test])
                    data_missing = True
                else:
                    simi.append(data_test * wt_test)
            if data_missing:
                simi = self.__process_missing_data(simi)
            simi = np.sum(simi)
            self.veh_simi[vehicle] = simi * 100

                
    def __process_missing_data(self, data):
        # find the proportion of data missing
        count_missing = [np.isnan(x).any() for x in data].count(True)
        missing_proportion = count_missing / len(data)
        # print(missing_proportion)
        if missing_proportion == 1:
            return None
        
        # find the average similarity of exsisting data        
        obtained = np.sum([x for x in data if not np.isnan(x).any()])
        # maximum possible similarity (excluding missing data)
        total = 1 - np.sum([x[1] for x in data if np.isnan(x).any()])
        avg_simi = obtained / total
        
        '''the similarity of missing data is assigned to be the average 
        similarity of those exsisting data, but with a weight deduction
        according to the proportion of data missing.'''
        # weight_adjust = (1 - missing_proportion **2) ** 0.5
        weight_adjust = (5 - (missing_proportion + 1) **2) ** 0.5 - 1
        data = [avg_simi * x[1] * weight_adjust if np.isnan(x).any() 
                                                else x for x in data]
        return data
        
            
if __name__ == '__main__':
    import time
    import pandas as pd
    
    from weight_setting import Weight
    from get_curve_paths import get_curve_paths
    from veh_key_data import VehKeyData
    from detailed_similarity import VehSimilarity
    
    store_path = r'D:\Desktop\KnC Store Path'
    start = time.time()
    df_vehicles = pd.read_csv(store_path + '\\summary_data.csv')
    df_vehicles = df_vehicles.set_index('VEHICLES')
    
    with open(store_path + '\\Vehicle Summary.txt','r') as f:
        lines = f.readlines()[:20]
        veh_identities = [a.split('\t')[0] for a in lines]

    target_veh_identity = veh_identities[0]
    target_veh_name = target_veh_identity.rpartition('#')[0]
    df_target = df_vehicles[['Unnamed: 1', target_veh_name]]
    target_curve_paths = get_curve_paths(target_veh_identity, store_path)
    target_vehicle = VehKeyData(df_target, target_curve_paths)
    target_missing = False
    if target_vehicle.all_data_missing:
        vehicle_diff = None
        print('Warning! Target vehicle: %s is missing data for all tests.' 
                                                  % target_veh_identity)
        target_missing = True

    
    all_vehicles = {}
    for veh_identity in veh_identities:
        print(veh_identity)
        veh_name = veh_identity.rpartition('#')[0]
        df = df_vehicles[['Unnamed: 1',veh_name]]
        curve_paths = get_curve_paths(veh_identity, store_path)
        vehicle_data = VehKeyData(df, curve_paths)
        all_vehicles[veh_identity] = vehicle_data


    detailed_similarity = {}
    for sample_veh_identity, sample_vehicle in all_vehicles.items():
        if target_missing:
            break
        if sample_veh_identity == target_veh_identity:
            continue
        if sample_vehicle.all_data_missing:
            detail = None
            print('Warning! Sample vehicle: %s is missing data for all tests.' 
                                              % sample_veh_identity)
        else:
            simi = VehSimilarity(target_vehicle, sample_vehicle)
            detail = simi.detailed_similarity
        detailed_similarity[sample_veh_identity] = detail
        
    weight = Weight()
    result = OverallSimilarity(detailed_similarity, weight)

    # print(result.para_simi)
    # print(result.test_simi)
    
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
            
            
    print('\nTarget vehicle:', target_veh_identity)
    df_ranking = pd.DataFrame({'VEHICLES' : result.veh_simi.keys(),
                               'OVERALL' : result.veh_simi.values()})
    # df_ranking = pd.DataFrame([overall_simi])
    df_ranking = df_ranking.sort_values(by=['OVERALL'], ascending=False)
    df_ranking = df_ranking.reset_index(drop=True)
    df_ranking.index = df_ranking.index + 1
    pd.set_option('display.max_row', 500)
    print(df_ranking[:])
    # for vehicle, similarity in overall_simi.items():
    #     print(vehicle)
    #     print(similarity)            
    end = time.time()
    print('time:%f' % (end - start))
    