# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:09:26 2021

@author: Fanyi Sun
"""

import numpy as np

class VehReliability():
    def __init__(self, veh_data, targetF, targetR):
        self.veh_data = veh_data
        self.targetF = targetF
        self.targetR = targetR
        
        self.__get_reliability()
    
    
    def __get_reliability(self):        
        self.reliabilityF = {}
        for condition, info in self.veh_data.dataF.items():
            self.reliabilityF[condition] = {}
            for para, value in info.items():
                para_target = eval('self.targetF.%s' % para)
                if para_target['type'] == 'interval':
                    ans = self.__process_interval(para, value, para_target)
                    self.reliabilityF[condition][para] = ans
                elif para_target['type'] == 'max':
                    ans = self.__process_max(para, value, para_target)
                    self.reliabilityF[condition][para] = ans
                elif para_target['type'] == 'min':
                    ans = self.__process_min(para, value, para_target)
                    self.reliabilityF[condition][para] = ans
                
        self.reliabilityR = {}
        for condition, info in self.veh_data.dataR.items():
            self.reliabilityR[condition] = {}
            for para, value in info.items():
                para_target = eval('self.targetR.%s' % para)
                if para_target['type'] == 'interval':
                    ans = self.__process_interval(para, value, para_target)
                    self.reliabilityR[condition][para] = ans
                elif para_target['type'] == 'max':
                    ans = self.__process_max(para, value, para_target)
                    self.reliabilityR[condition][para] = ans
                elif para_target['type'] == 'min':
                    ans = self.__process_min(para, value, para_target)
                    self.reliabilityR[condition][para] = ans
                
                    
    def __process_interval(self, para, value, para_target):
        # abcd are four values at the axis from left to right
        if np.isnan(value):
            return np.nan
        
        a = para_target['limit'][0]
        b = para_target['value'][0]
        c = para_target['value'][1]
        d = para_target['limit'][1]
        if b <= value <= c:
            ans = 1
        elif value <= a or value >= d:
            ans = 0
        else:
            if 'other' not in para_target:
                if a < value < b:
                    ans = (value - a) / (b - a)
                elif c < value < d: 
                    ans = 1 - (value - c) / (d - c)
            else:
                '''
                record all the nodes in the form of coordinates and use linear
                interpolation to find the y value at a specific position
                '''
                x = [a,b,c,d]
                y = [0,1,1,0]
                ans = self.__customised_nodes(value, x, y, para_target)
        return ans
    
        
    def __process_max(self, para, value, para_target):
        if np.isnan(value):
            return np.nan
        
        a = para_target['limit'][0]
        b = para_target['value'][0]
        c = para_target['limit'][1]
        # reliability at the critical value
        loc_rb = para_target['value'][1]
        if value <= a:
            ans = 1
        elif value >= c:
            ans = 0
        else:
            if 'other' not in para_target:
                if value < b:
                    ans = 1 - (value - a) / (b - a) * (1 - loc_rb)
                else:
                    ans = (c - value) / (c - b) * loc_rb
            else:
                x = [a,b,c]
                y = [1,loc_rb,0]
                ans = self.__customised_nodes(value, x, y, para_target)
        return ans
        
    
    def __process_min(self, para, value, para_target):
        if np.isnan(value):
            return np.nan
        
        a = para_target['limit'][0]
        b = para_target['value'][0]
        c = para_target['limit'][1]
        # reliability at the critical value
        loc_rb = para_target['value'][1]
        if value <= a:
            ans = 0
        elif value >= c:
            ans = 1
        else:
            if 'other' not in para_target:
                if value < b:
                    ans = (value - a) / (b - a) * loc_rb
                else:
                    ans = loc_rb + (value - b) / (c - b) * (1 - loc_rb)
            else:
                x = [a,b,c]
                y = [1,loc_rb,0]
                ans = self.__customised_nodes(value, x, y, para_target)
        return ans

                
    def __customised_nodes(self, value, x, y, para_target):
        for i in range(0,len(para_target['other']),2):
            x.append(para_target['other'][i])
            y.append(para_target['other'][i+1])
        zipped = sorted(zip(x,y))
        x, y = zip(*zipped)
        for i in range(len(x)):
            if value < x[i]:
                # linear interpolation
                ans = y[i-1] + (value - x[i-1]) / (x[i] - x[i-1]) * \
                                                    (y[i] - y[i-1])
                break
        return ans




if __name__ == '__main__':
    import time
    import pandas as pd
    from pyinstrument import Profiler
    
    from veh_target_data import VehTargetData
    from target_setting import *
    
    store_path = r'D:\Desktop\KnC Store Path'
    profiler = Profiler()
    profiler.start()
    
    df_vehicles = pd.read_csv(store_path + '\\summary_data.csv')
    df_vehicles = df_vehicles.set_index('VEHICLES')
    
    with open(store_path + '\\Vehicle Summary.txt','r') as f:
        lines = f.readlines()
        veh_identities = [a.split('\t')[0] for a in lines][:1]
        
    start = time.time()
    for veh_identity in veh_identities:
        veh_name = veh_identity.rpartition('#')[0]
        print(veh_name)
        df_vehicle = df_vehicles[['Unnamed: 1', veh_name]]
        
        # curve_data_paths = get_curve_paths(veh_identity, store_path)
             
        veh_data = VehTargetData(df_vehicle, store_path, veh_identity)
        targetF = FrontTarget()
        targetR = RearTarget()
        
        veh_reliability = VehReliability(veh_data, targetF, targetR)
        a = veh_reliability.reliabilityR
        print(a)
    
    
        
    end = time.time()
    total = end - start
    print("time:%f"  % total)
    profiler.stop()
    profiler.print()
                