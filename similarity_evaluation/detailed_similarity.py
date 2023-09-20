# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:36:16 2021

@author: Fanyi Sun
"""

import numpy as np

from veh_key_data import VehKeyData

class VehSimilarity():
    def __init__(self, target_vehicle, sample_vehicle):
        self.target = target_vehicle
        self.sample = sample_vehicle
        
        tests = ['test1', 'test2', 'test3', 'test4', 'test5',
                 'test6', 'test7', 'test8', 'test10', 'strapped']
        
        self.detailed_similarity = {}
        for test in tests:
            self.__test = test
            exec(f"{'self.%s_missing' % test} = False")
            if eval('self.target.data_%s' % test) is None:
                self.detailed_similarity[test] = None
                exec(f"{'self.%s_missing' % test} = True")
# =============================================================================
#                 # print('Warning! Target vehicle: %s is missing data for %s.' 
#                 #                   % (target_vehicle_identity, test))
# =============================================================================
            elif eval('self.sample.data_%s' % test) is None: 
                self.detailed_similarity[test] = None
            else:
                simi = eval('self.compare_test')()
                self.detailed_similarity[test] = simi
                
                
    def compare_test(self):
        simi = {}
        for para in eval("self.target.data_%s.keys()" % self.__test):
            simi[para] = {} # create an empty dict
            for feature in eval("self.target.data_%s[para]" % self.__test):
                if 'curve' not in feature:
                    simi = self.__compare_value(simi, self.__test,
                                                para, feature)
                else:
                    simi = self.__compare_curve(simi, self.__test,
                                                para, feature)
        return simi
    
    
    def __compare_curve(self, simi, test, para, feature):
        target = eval("self.target.data_%s[para][feature]" % test)
        sample = eval("self.sample.data_%s[para][feature]" % test)       
        if target is None or sample is None:
            exec(f"{'simi[para][feature]'} = None")
        else:
            similarity = []
            for wheel in range(len(target)):
                if target[wheel] is None or sample[wheel] is None:
                    similarity.append(np.nan)
                    continue
                x_sample = np.array(sample[wheel][0])
                y_sample = np.array(sample[wheel][1])
                x_target = np.array(target[wheel][0])
                y_target = np.array(target[wheel][1])
                # remove np.nan
                x1 = x_sample[(np.isnan(x_sample)==False) & 
                                  (np.isnan(y_sample)==False)]
                y1 = y_sample[(np.isnan(x_sample)==False) & 
                                  (np.isnan(y_sample)==False)]
                x2 = x_target[(np.isnan(x_target)==False) & 
                                  (np.isnan(y_target)==False)]
                y2 = y_target[(np.isnan(x_target)==False) & 
                                  (np.isnan(y_target)==False)]
                if feature == 'curve':
                    # compare the region where two curves intersect.
                    x_left = (x2[0] if (abs(x2[0]) < 
                                          abs(x1[0])) else x1[0])
                    x_right = (x2[-1] if (abs(x2[-1]) < 
                                        abs(x1[-1])) else x1[-1])
                    # cut the curves so they have similar x ranges
                    x1_temp = x1
                    y1_temp = y1
                    x2_temp = x2
                    y2_temp = y2
                    x1 = x1_temp[(x1_temp > x_left) & (x1_temp < x_right)]
                    y1 = y1_temp[(x1_temp > x_left) & (x1_temp < x_right)]
                    # x2 is always wider than x1 (because of >= & <=)
                    # It doesn't mean x2 has more nodes.
                    x2 = x2_temp[(x2_temp >= x_left) & (x2_temp <= x_right)]
                    y2 = y2_temp[(x2_temp >= x_left) & (x2_temp <= x_right)]
                simi_wheel = []
                for i in range(len(x1)):
                    # find the y value from target curve at a specific x
                    # add constrains when searching value to improve speed
                    ratio = len(x2) / len(x1)
                    toleft = round(i * ratio) - 5
                    toright = round(i * ratio) + 5
                    if round(i * ratio) < 5:
                        y = self.__find_value(x1[i],x2[:toright],y2[:toright])
                    elif round(i * ratio) >= len(x1) - 5:
                        y = self.__find_value(x1[i],x2[toleft:],y2[toleft:])
                    else:
                        y = self.__find_value(x1[i], x2[toleft:toright],
                                                     y2[toleft:toright])
                    diff = np.abs((y1[i] - y) / y)
                    simi_wheel.append(1 / (1 + diff))
                similarity.append(np.nanmean(simi_wheel))
            if np.isnan(similarity).all():
                avg_simi = None
            else:
                avg_simi = np.nanmean(similarity)
            exec(f"{'simi[para][feature]'} = avg_simi")
        return simi
                
    
    def __compare_value(self, simi, test, para, feature):
        """
        compare the difference of a specific feature of a curve
        """
        target = eval("self.target.data_%s[para][feature]" % test)
        sample = eval("self.sample.data_%s[para][feature]" % test)
        if target is None or sample is None:
            exec(f"{'simi[para][feature]'} = None")
        else: # it's a list
            target = [[np.nan,np.nan] if x is None else x for x in target]
            sample = [[np.nan,np.nan] if x is None else x for x in sample]
            if np.isnan(target).all() or np.isnan(sample).all():
                exec(f"{'simi[para][feature]'} = None")
            else:
                target = np.array(target)
                sample = np.array(sample)
                diff = np.abs((sample - target) / target)
                if np.isnan(diff).all():
                    similarity = None
                else:
                    similarity = np.nanmean(1 / (1 + diff))
                # exec(f"{'simi[para][feature]'} = diff")
                exec(f"{'simi[para][feature]'} = similarity")
        return simi
    
    
    def __find_value(self, x, xn, yn):
        min_diff = 1e5
        # search the closest point
        for i in range(1,len(xn)-1): # ignore the first and last index
            if abs(x - xn[i]) < min_diff:
                min_diff = abs(x - xn[i])
                pos = i
                
        if x >= xn[pos]:
            pre = [xn[pos],yn[pos]]
            nex = [xn[pos+1],yn[pos+1]]
        else:
            pre = [xn[pos-1],yn[pos-1]]
            nex = [xn[pos],yn[pos]]
        # using linear interpolation
        y = pre[1] + (nex[1] - pre[1])/(nex[0] - pre[0]) * (x - pre[0])
        return y
        
        
if __name__ == '__main__':
    import time
    import pandas as pd
    
    from get_curve_paths import get_curve_paths
    
    store_path = r'D:\Desktop\KnC Store Path'
    start = time.time()
    df_vehicles = pd.read_csv(store_path + '\\summary_data.csv')
    df_vehicles = df_vehicles.set_index('VEHICLES')
    
    with open(store_path + '\\Vehicle Summary.txt','r') as f:
        lines = f.readlines()
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
    
    detailed_similarity = {}
    for veh_identity in veh_identities:
    # for i in [10]:
        if target_missing:
            break
        sample_veh_identity = veh_identity
        sample_veh_name = veh_identity.rpartition('#')[0]
        if sample_veh_name == target_veh_name:
            continue
        print('\n',sample_veh_identity)
        df_sample = df_vehicles[['Unnamed: 1',sample_veh_name]]
        sample_curve_paths = get_curve_paths(sample_veh_identity, store_path)
        sample_vehicle = VehKeyData(df_sample, sample_curve_paths)
        
        if sample_vehicle.all_data_missing:
            detail = None
            print('Warning! Sample vehicle: %s is missing data for all tests.' 
                                              % sample_veh_identity)
        else:
            simi = VehSimilarity(target_vehicle, sample_vehicle)
            detail = simi.detailed_similarity

        detailed_similarity[sample_veh_identity] = detail

        # if detail is None:
        #     print(detail)
        #     continue
        # for test, data_tests in detail.items():
        #     print(test)
        #     if data_tests is None:
        #         print(data_tests)
        #         continue
        #     for para, para_data in data_tests.items():
        #         print(para)
        #         print(para_data)
                
        
    for vehicle, data_vehicle in detailed_similarity.items():
        print('\n', vehicle)
        # print(data_vehicle['test8']['Roll Steer v Wheel to Body [deg/mm]'])
        # for test, data_test in data_vehicle.items():
        #     print(test,'\n')
            # for para, data_para in data_tests.items():
            #     print(para)
            #     print(data_para)
                
    end = time.time()
    print('time:%f' % (end - start))
    
    
    
    
