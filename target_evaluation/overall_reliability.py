# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:15:09 2021

@author: Fanyi Sun
"""

import numpy as np

class OverallReliability():
    def __init__(self, detailed_reliability, weightF, weightR):
        self.detailed_rb = detailed_reliability
        self.weightF = weightF
        self.weightR = weightR
        self.para_rb_F = {}
        self.para_rb_R = {}
        
        # find the sub-overall reliability for each test condition
        self.find_test_reliability_F()
        self.find_test_reliability_R()
        self.find_front_reliability()
        self.find_rear_reliability()
        self.find_overall_reliability()
        
        
    def find_test_reliability_F(self):
        # a dict containing all vehicles and their test reliability info
        self.test_rb_F = {}
        for vehicle, veh_data in self.detailed_rb.items():
            self.test_rb_F[vehicle] = {}
            self.para_rb_F[vehicle] = {}
            rb_detailed_data = veh_data.reliabilityF
            for test, data_test in rb_detailed_data.items():
                rb = []
                data_missing = False
                for para, data_para in data_test.items():
                    self.para_rb_F[vehicle][para] = data_para
                    wt_para = eval("self.weightF.%s" % para)
                    if np.isnan(data_para):
                        # to be used in __process_missing_data
                        rb.append([np.nan,wt_para])
                        data_missing = True
                    else:
                        rb.append(data_para * wt_para)
                        
                if data_missing:
                    rb = self.__process_missing_data(rb)   
                reliability = np.sum(rb)
                self.test_rb_F[vehicle][test] = reliability
                
                
    def find_test_reliability_R(self):
        self.test_rb_R = {}
        for vehicle, veh_data in self.detailed_rb.items():
            self.test_rb_R[vehicle] = {}
            self.para_rb_R[vehicle] = {}
            rb_detailed_data = veh_data.reliabilityR
            for test, data_test in rb_detailed_data.items():
                rb = []
                data_missing = False
                for para, data_para in data_test.items():
                    self.para_rb_R[vehicle][para] = data_para
                    wt_para = eval("self.weightR.%s" % para)
                    if np.isnan(data_para):
                        rb.append([np.nan,wt_para])
                        data_missing = True
                    else:
                        rb.append(data_para * wt_para)
                        
                if data_missing:
                    rb = self.__process_missing_data(rb)   
                reliability = np.sum(rb)
                self.test_rb_R[vehicle][test] = reliability
                
                
    def find_front_reliability(self):
        self.veh_rb_F = {}
        for vehicle, veh_data in self.test_rb_F.items():
            rb = []
            data_missing = False
            for test, data_test in veh_data.items():
                wt_test = eval("self.weightF.%s" % test)
                
                if np.isnan(data_test):
                    rb.append([np.nan,wt_test])
                    data_missing = True
                else:
                    rb.append(data_test * wt_test)
            if data_missing:
                rb = self.__process_missing_data(rb)
            rb = np.sum(rb)
            self.veh_rb_F[vehicle] = rb * 100
                
                
    def find_rear_reliability(self):
        self.veh_rb_R = {}
        for vehicle, veh_data in self.test_rb_R.items():
            rb = []
            data_missing = False
            for test, data_test in veh_data.items():
                wt_test = eval("self.weightR.%s" % test)
                
                if np.isnan(data_test):
                    rb.append([np.nan,wt_test])
                    data_missing = True
                else:
                    rb.append(data_test * wt_test)
            if data_missing:
                rb = self.__process_missing_data(rb)
            rb = np.sum(rb)
            self.veh_rb_R[vehicle] = rb * 100
        
            
    def find_overall_reliability(self):
        self.overall_rb = {}
        for vehicle in self.veh_rb_F.keys():
            avg = self.veh_rb_F[vehicle] * self.weightF.front + \
                    self.veh_rb_R[vehicle] * self.weightR.rear
            self.overall_rb[vehicle] = avg
            
                
        
        
    def __process_missing_data(self, data):
        # find the proportion of data missing
        count_missing = [np.isnan(x).any() for x in data].count(True)
        missing_proportion = count_missing / len(data)
        # print(missing_proportion)
        if missing_proportion == 1:
            return np.nan
        
        # find the average similarity of exsisting data        
        obtained = np.sum([x for x in data if not np.isnan(x).any()])
        # maximum possible similarity (excluding missing data)
        total = 1 - np.sum([x[1] for x in data if np.isnan(x).any()])
        avg_rb = obtained / total
        
        '''the reliability of missing data is assigned to be the average 
        reliability of those exsisting data, but with a weight deduction
        according to the proportion of data missing.'''
        # weight_adjust = (1 - missing_proportion **2) ** 0.5
        weight_adjust = (5 - (missing_proportion + 1) **2) ** 0.5 - 1
        data = [avg_rb * x[1] * weight_adjust if np.isnan(x).any() 
                                                else x for x in data]
        return data
    
    
        
        
if __name__ == '__main__':
    import time
    import pandas as pd
    from pyinstrument import Profiler
    
    from veh_target_data import VehTargetData
    from target_setting import *
    from detailed_reliability import VehReliability
    from weight_setting2 import *
    
    store_path = r'D:\Desktop\KnC Store Path'
    profiler = Profiler()
    profiler.start()
    
    df_vehicles = pd.read_csv(store_path + '\\summary_data.csv')
    df_vehicles = df_vehicles.set_index('VEHICLES')
    
    with open(store_path + '\\Vehicle Summary.txt','r') as f:
        lines = f.readlines()
        veh_identities = [a.split('\t')[0] for a in lines][:1]
        
    start = time.time()
    
    targetF = FrontTarget()
    targetR = RearTarget()
    weightF = FrontWeight()
    weightR = RearWeight()
    
    detailed_reliability = {}
    for veh_identity in veh_identities:
        veh_name = veh_identity.rpartition('#')[0]
        print(veh_name)
        df_vehicle = df_vehicles[['Unnamed: 1', veh_name]]
        
             
        veh_data = VehTargetData(df_vehicle, store_path, veh_identity)
        
        reli = VehReliability(veh_data, targetF, targetR)
        a = reli.reliabilityR
        # for condition, info in a.items():
        #     print(condition)
        #     print(info)
        # print()
        
        detailed_reliability[veh_identity] = reli
    
    result = OverallReliability(detailed_reliability, weightF, weightR)
    
    for veh in result.overall_rb.keys():
        print('\n',veh)
        for test, rb in result.test_rb_F[veh].items():
            print('%s: %s' % (test, rb))
            
        print()
        print('front: %s' % (result.veh_rb_F[veh]))
        print('rear: %s' % (result.veh_rb_R[veh]))
        print('overall:',result.overall_rb[veh])
            
    
            
    end = time.time()
    total = end - start
    print("\ntime:%f"  % total)
    profiler.stop()
    # profiler.print()