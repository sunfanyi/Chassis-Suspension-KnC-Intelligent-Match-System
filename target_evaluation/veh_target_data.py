# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 09:55:42 2021

@author: Fanyi Sun
"""

import sys
import os
import numpy as np
import pandas as pd

sys.path.append('..')
from match_test_name import get_full_test_name


class VehTargetData():
    """
    Get the full test name to split the dataframe and get the information from
    the specific test condition only. This can avoid confusion because some 
    test conditions have the same parameter names whilst only one is needed.
    """
    tests = ['test1', 'test2', 'test3', 'test4', 'test5',
             'test6', 'test7', 'test8', 'test10', 'strapped']
    full_tests_names = []
    for test in tests:
        if test != 'test7':
            full_tests_names.append(get_full_test_name(test))
        else:
            full_tests_names.append('Test 7_Steering Geometry Mid-Mid                               ')
    
    
    def __init__(self, df_vehicle, store_path, veh_identity):
        self.df_vehicle = df_vehicle
        self.store_path = store_path
        self.veh_identity = veh_identity

        self.dataF = {'general': {}, 'longitudinal': {}, 'lateral': {},
                      'vertical': {}, 'steer': {}, 'roll': {}}
        self.dataR = {'general': {}, 'longitudinal': {}, 'lateral': {},
                      'vertical': {}, 'roll': {}}
        
        # for general data
        self.__df = self.df_vehicle[:self.full_tests_names[0]]
        self.__df = self.__df.set_index('Unnamed: 1', append=True)
        self.get_data_general()
        
        # for test data
        for i in range(len(self.tests)):
            if self.tests[i] in ['test3', 'test5', 'test6']:
                # no information in these tests
                continue
            
            if i == len(self.tests) - 1:
                self.__df = self.df_vehicle[self.full_tests_names[i]:]
            else:
                self.__df = self.df_vehicle[self.full_tests_names[i]:
                                              self.full_tests_names[i+1]]
            # self.__df = self.__df.sort_index()
            self.__df = self.__df.set_index('Unnamed: 1', append=True)
            self.__df = self.__df.astype('float')
            eval('self.get_data_%s' % self.tests[i])()
        
    
    def get_data_general(self):
        parameters = ['static_camber', 'toe_in']
        indices = ['Camber [deg]', 'Toe [deg]']
        
        for para, index in zip(parameters, indices):
            slopeF = self.__df.loc[index,'F_avg'].iloc[0]
            self.dataF['general'][para] = float(slopeF)
            slopeR = self.__df.loc[index,'R_avg'].iloc[0]
            self.dataR['general'][para] = float(slopeR)
            

    def get_data_test1(self):
        para = 'brake_toe_in'
        index = 'Longitudinal Toe Compliance [deg/N]'
        slopeF = self.__df.loc[index,'F_avg'].iloc[0]
        self.dataF['longitudinal'][para] = -np.abs(slopeF * 1000)
        slopeR = self.__df.loc[index,'R_avg'].iloc[0]
        self.dataR['longitudinal'][para] = -np.abs(slopeR * 1000)
        
        para = 'caster_comp'
        index = 'Longitudinal Spin Compliance [deg/N]'
        slopeF = self.__df.loc[index,'F_avg'].iloc[0]
        self.dataF['longitudinal'][para] = slopeF * 1000
        slopeR = self.__df.loc[index,'R_avg'].iloc[0]
        self.dataR['longitudinal'][para] = slopeR * 1000
        
        para = 'anti_dive'
        index = 'Anti-Dive Front/Anti-Lift Rear Curve Fits [N/N]'
        slopeF = self.__df.loc[index,'F_avg'].iloc[0]
        self.dataF['longitudinal'][para] = np.abs(slopeF * 100)
        
        para = 'anti_lift'
        index = 'Anti-Dive Front/Anti-Lift Rear Curve Fits [N/N]'
        slopeR = self.__df.loc[index,'R_avg'].iloc[0]
        self.dataR['longitudinal'][para] = np.abs(slopeR * 100)


    def get_data_test2(self):
        para = 'camber_comp'
        index = 'Lateral Camber Compliance [deg/N]'
        slopeF = self.__df.loc[index,'F_avg'].iloc[0]
        self.dataF['lateral'][para] = np.abs(slopeF * 1000)
        slopeR = self.__df.loc[index,'R_avg'].iloc[0]
        self.dataR['lateral'][para] = np.abs(slopeR * 1000)
        
        para = 'lat_stif'
        index = 'Lateral Wheel Centre Compliance [mm/N]'
        slopeF = self.__df.loc[index,'F_avg'].iloc[0]
        self.dataF['lateral'][para] = 1 / slopeF
        slopeR = self.__df.loc[index,'R_avg'].iloc[0]
        self.dataR['lateral'][para] = 1 / slopeR
        
        index = 'Lateral Toe Compliance [deg/N]'
        # keep this info for calculating lat_F_delta at test4
        self.__lat_Force0_F = self.__df.loc[index,'F_avg'].iloc[0]
        self.__lat_Force0_F = np.abs(self.__lat_Force0_F * 1000)
        self.__lat_Force0_R = self.__df.loc[index,'R_avg'].iloc[0]
        self.__lat_Force0_R = np.abs(self.__lat_Force0_R * 1000)
        
        
    def get_data_test4(self):
        index = 'Lateral Toe Compliance [deg/N]'
        
        para = 'lat_F'
        slopeF = np.abs(self.__df.loc[index,'F_avg'].iloc[0] * 1000)
        self.dataF['lateral'][para] = slopeF
        slopeR = np.abs(self.__df.loc[index,'R_avg'].iloc[0] * 1000)
        self.dataR['lateral'][para] = slopeR
        
        para = 'lat_F_delta'
        deltaF = slopeF - self.__lat_Force0_F
        deltaR = slopeR - self.__lat_Force0_R
        self.dataF['lateral'][para] = deltaF
        self.dataR['lateral'][para] = deltaR
        
        
    def get_data_test7(self):
        parameters = ['caster', 'kpi', 'kpo','scrub_r']
        indices = ['Kingpin Castor Angle v Handwheel Steer [deg/deg]\ny-intercept', 
                   'Kingpin Inclination Angle v Handwheel Steer [deg/deg]\ny-intercept',
                   'Kingpin Offset v Handwheel Steer [mm/deg]\ny-intercept',
                   'Scrub Radius v Handwheel Steer [mm/deg]\ny-intercept']
        
        for para, index in zip(parameters, indices):
            slopeF = self.__df.loc[index,'F_avg'].iloc[0]
            self.dataF['steer'][para] = slopeF
            
        para = 'ackermann'
        # find the maiximum y from the curve
        dir = self.store_path + '\\Curves Data\\' + self.veh_identity
        for file in os.listdir(dir):
            if 'test 7_processed.csv' in file:
                path = os.path.join(dir,file)
        try:
            curve = pd.read_csv(path)
        except UnboundLocalError:
            # if file not founded
            self.dataF['steer'][para] = np.nan
        else:
            try:
                y_left = list(curve['LeftTurnLHPercentageAckermann'])
                y_right = list(curve['RightTurnRHPercentageAckermann'])
            except KeyError:
                # if curve data not founded
                self.dataF['steer'][para] = np.nan
            else:
                y_max = np.max([y_left[0], y_right[-1]])
                self.dataF['steer'][para] = y_max
        
        
    def get_data_test8(self):
        para = 'static_rch'
        index = 'Kinematic Roll Centre Height [mm/deg]\ny-intercept'
        slopeF = self.__df.loc[index,'F_avg'].iloc[0]
        self.dataF['roll'][para] = slopeF
        slopeR = self.__df.loc[index,'R_avg'].iloc[0]
        self.dataR['roll'][para] = slopeR
        
        para = 'static_rch_diff'
        diff = slopeR - slopeF
        self.dataR['roll'][para] = diff
        
        index = 'Roll Steer v Wheel to Body [deg/mm]'
        '''do we need absolute???'''
        # keep this info for calculating roll_bump at test10
        self.__roll_steerF = np.abs(self.__df.loc[index,'F_avg'].iloc[0] * 1000)
        self.__roll_steerR = np.abs(self.__df.loc[index,'R_avg'].iloc[0] * 1000)

        
    def get_data_test10(self):
        para = 'bump_camber'
        index = 'Bump Camber [deg/mm]'
        slopeF = self.__df.loc[index,'F_avg'].iloc[0] * 1000
        self.dataF['vertical'][para] = slopeF
        slopeR = self.__df.loc[index,'R_avg'].iloc[0] * 1000
        self.dataR['vertical'][para] = slopeR
        
        para = 'bump_understeer'    
        index = 'Bump Steer [deg/mm]'
        slopeF = np.abs(self.__df.loc[index,'F_avg'].iloc[0] * 1000)
        self.dataF['vertical'][para] = slopeF
        slopeR = np.abs(self.__df.loc[index,'R_avg'].iloc[0] * 1000)
        self.dataR['vertical'][para] = slopeR
        
        para = 'roll_bump'
        deltaF = slopeF - self.__roll_steerF
        deltaR = slopeR - self.__roll_steerR
        self.dataF['roll'][para] = deltaF
        self.dataR['roll'][para] = deltaR
        
        para = 'wheel_travel'
        # find the maiximum x from the curve (bump)
        dir = self.store_path + '\\Curves Data\\' + self.veh_identity
        for file in os.listdir(dir):
            if 'test 10_processed.csv' in file:
                path = os.path.join(dir,file)
        try:
            curve = pd.read_csv(path)
        except UnboundLocalError:
            # if file not founded
            self.dataF['vertical'][para] = np.nan
        else:
            try:
                FL = list(curve['FLHwheeltobodyZdisplacementmm'])
                FR = list(curve['FRHwheeltobodyZdisplacementmm'])
                # RL = list(curve['RLHwheeltobodyZdisplacementmm'])
                # RR = list(curve['RRHwheeltobodyZdisplacementmm'])
            except KeyError:
                # if curve data not founded
                self.dataF['steer'][para] = np.nan
            else:
                # find the righmost value
                x_maxF = np.mean([FL[-1], FR[-1]])
                # x_maxR = np.mean([RL[-1], RR[-1]])
                self.dataF['vertical'][para] = x_maxF
                # self.dataR['vertical'][para] = x_maxR
        
    
    def get_data_strapped(self):
        para = 'drive_toe_in'
        index = 'Longitudinal Toe Compliance [deg/N]'
        slopeF = self.__df.loc[index,'F_avg'].iloc[0]
        self.dataF['longitudinal'][para] = -np.abs(slopeF * 1000)
        slopeR = self.__df.loc[index,'R_avg'].iloc[0]
        self.dataR['longitudinal'][para] = -np.abs(slopeR * 1000)
        
        para = 'anti_lift'
        index = 'Anti-Lift Front/Anti-Squat Rear Curve Fits [N/N]'
        slopeF = self.__df.loc[index,'F_avg'].iloc[0]
        self.dataF['longitudinal'][para] = np.abs(slopeF * 100)
        
        para = 'anti_squat'
        index = 'Anti-Lift Front/Anti-Squat Rear Curve Fits [N/N]'
        slopeR = self.__df.loc[index,'R_avg'].iloc[0]
        self.dataR['longitudinal'][para] = np.abs(slopeR * 100)
        
        
if __name__ == '__main__':
    import time
    from pyinstrument import Profiler
    
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
        data = veh_data.dataR
        for condition, info in data.items():
            print(condition)
            print(info)
        print()
            
    end = time.time()
    total = end - start
    print("time:%f"  % total)
    profiler.stop()
    profiler.print()
                
            
        