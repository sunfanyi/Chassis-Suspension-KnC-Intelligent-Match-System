# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:10:33 2021

@author: Fanyi Sun
"""

import pandas as pd

from veh_target_data import VehTargetData
from detailed_reliability import VehReliability
from overall_reliability import OverallReliability


def main_target(veh_identities, store_path, weightF, weightR, 
                    targetF, targetR):
    df_vehicles = pd.read_csv(store_path + '\\summary_data.csv')
    df_vehicles = df_vehicles.set_index('VEHICLES')
    
    detailed_reliability = {}
    for veh_identity in veh_identities:
        veh_name = veh_identity.rpartition('#')[0]
        print(veh_name)
        df_vehicle = df_vehicles[['Unnamed: 1', veh_name]]
             
        veh_data = VehTargetData(df_vehicle, store_path, veh_identity)
        
        reli = VehReliability(veh_data, targetF, targetR)
        
        detailed_reliability[veh_identity] = reli
    
    result = OverallReliability(detailed_reliability, weightF, weightR)
    df_ranking = pd.DataFrame({'VEHICLES' : result.overall_rb.keys(),
                               'OVERALL' : result.overall_rb.values()})
    df_ranking = df_ranking.sort_values(by=['OVERALL'], ascending=False)
    df_ranking = df_ranking.reset_index(drop=True)
    df_ranking.index = df_ranking.index + 1
    pd.set_option('display.max_row', 500)
    
    allRb_F = {}
    allRb_R = {}
    allRb_F['paraRb'] = result.para_rb_F
    allRb_R['paraRb'] = result.para_rb_R
    allRb_F['testRb'] = result.test_rb_F
    allRb_R['testRb'] = result.test_rb_R
    allRb_F['vehRb'] = result.veh_rb_F
    allRb_R['vehRb'] = result.veh_rb_R
    
    return df_ranking, allRb_F, allRb_R

        
if __name__ == '__main__':
    import time
    from pyinstrument import Profiler
    
    from target_setting import FrontTarget, RearTarget
    from weight_setting2 import FrontWeight, RearWeight
    
    profiler = Profiler()
    profiler.start()
    start = time.time()
    
    store_path = r'D:\Desktop\KnC Store Path'
    with open(store_path + '\\Vehicle Summary.txt','r') as f:
        lines = f.readlines()
        veh_identities = [a.split('\t')[0] for a in lines][:10]

    targetF = FrontTarget()
    targetR = RearTarget()
    weightF = FrontWeight()
    weightR = RearWeight()
    
    df_ranking, allRb_F, allRb_R = main_target(veh_identities, store_path, 
                                           weightF, weightR, targetF, targetR)
    
    print(df_ranking)
    # allRb_F['testRb']
    # allRb_R['testRb']
    # allRb_F['vehRb']
    # allRb_R['vehRb']
    
    end = time.time()
    print('time:%f' % (end - start))
    profiler.stop()
    # profiler.print()