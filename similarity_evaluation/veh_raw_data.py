# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:04:59 2021

@author: Fanyi Sun
"""

import sys
import pandas as pd

sys.path.append('../')
# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from match_test_name import get_full_test_name

class VehRawData():
    """ 
    find unprocessed data of a vehicle which can be directly extracted from 
    the databse, including slope, y-intercept and curves data
    """
    tests = ['test1', 'test2', 'test3', 'test4', 'test5',
             'test6', 'test7', 'test8', 'test10', 'strapped']
    full_tests_names = []
    for test in tests:
        if test != 'test7':
            full_tests_names.append(get_full_test_name(test))
        else:
            full_tests_names.append('Test 7_Steering Geometry Mid-Mid                               ')
    
    
    def __init__(self, df_vehicle, curve_data_paths):
        self.df_vehicle = df_vehicle
        self.curve_data_paths = curve_data_paths
        found_data = False
        
        # tests = ['test1', 'test2', 'test3', 'test4', 'test5',
        #           'test6', 'test7', 'test8', 'test10', 'strapped']
        for i in range(len(self.tests)):
            if i == len(self.tests) - 1:
                self.__df = self.df_vehicle[self.full_tests_names[i]:]
            else:
                self.__df = self.df_vehicle[self.full_tests_names[i]:
                                              self.full_tests_names[i+1]]
            try: # some tests don't have curve data
                test = self.tests[i].replace('test','test ')
                self.__path = self.curve_data_paths[test]
                self.__curve = pd.read_csv(self.__path)
            except:
                pass
            self.__df = self.__df.set_index('Unnamed: 1', append=True)
            self.__df = self.__df.astype('float')
            self.__data = {}
            
            # some vehicles don't have any data
            test_data_missing = self.__df.isnull().values.all()
            if test_data_missing:
                exec(f"{'self.data_%s' % self.tests[i]} = None")
                continue
            
            found_data = True
            data = eval('self.get_data_%s' % self.tests[i])()
            exec(f"{'self.data_%s' % self.tests[i]} = data")
            
        self.all_data_missing = False if found_data else True
            
    
    # Longitudinal Compliance (braking)(brake on, eng. on, ARB on)
    def get_data_test1(self):
        # find slope
        parameters = ['Longitudinal Wheel Centre Compliance [mm/N]',
                      'Longitudinal Toe Compliance [deg/N]',
                      'Longitudinal Camber Compliance [deg/N]',
                      'Longitudinal Spin Compliance [deg/N]',
                      'Longitudinal Tyre Stiffness [N/mm]',
                      'Force Anti-Dive Angles [deg/N]',
                      'Anti-Dive Front/Anti-Lift Rear Curve Fits [N/N]']
        data = self.__get_slope(self.__data, parameters, self.__df)
        
        # find curves data
        parameters = ['Longitudinal Wheel Centre Compliance [mm/N]',
                      'Longitudinal Toe Compliance [deg/N]']
        x = ['FrontLHwheelForceXN', 'FrontRHwheelForceXN',
              'RearLHwheelForceXN', 'RearRHwheelForceXN']
        y = [['FrontLHwheelcentreXdispmm', 'FrontLHwheeltoeindeg'], 
              ['FrontRHwheelcentreXdispmm', 'FrontRHwheeltoeindeg'],
              ['RearLHwheelcentreXdispmm', 'RearLHwheeltoeindeg'],
              ['RearRHwheelcentreXdispmm', 'RearRHwheeltoeindeg']]
        data = self.__get_curve(data, parameters, x, y, self.__curve, 
                                self.__df)
        
        # find y-intercept
        parameters = ['Force Anti-Dive Angles [deg/N]']
        data = self.__get_y_intercept(data, parameters, self.__df)
        return data
            
    
    # Lateral Compliance at 0mm X offset (in phase)
    def get_data_test2(self):
        # find slope
        parameters = ['Lateral Toe Compliance [deg/N]',
                      'Force Roll Centre Height [mm/N]',
                      'Lateral Wheel Centre Compliance [mm/N]',
                      'Lateral Wheel Centre Stiffness projected on ground [N/mm]',
                      'Lateral Camber Compliance [deg/N]',
                      'Lateral Tyre Stiffness [N/mm]',
                      'Load Transfer (Roll Centre Curve Fits) [N/N]']
        data = self.__get_slope(self.__data, parameters, self.__df)
        
        # find curves data
        parameters = ['Lateral Toe Compliance [deg/N]',
                      'Force Roll Centre Height [mm/N]']
        x = ['FrontLHwheelForceYN', 'FrontRHwheelForceYN',
             'RearLHwheelForceYN', 'RearRHwheelForceYN']
        y = [['FrontLHwheeltoeindeg', 'FLHForceRollCentreHeightmm'],
             ['FrontRHwheeltoeindeg', 'FRHForceRollCentreHeightmm'],
             ['RearLHwheeltoeindeg', 'RLHForceRollCentreHeightmm'],
             ['RearRHwheeltoeindeg', 'RRHForceRollCentreHeightmm']]
        data = self.__get_curve(data, parameters, x, y, self.__curve, 
                                self.__df)      

        # find y-intercept
        parameters = ['Force Roll Centre Height [mm/N]']
        data = self.__get_y_intercept(data, parameters, self.__df)
        
        return data
    
    
    # Lateral Compliance at 0mm X offset (anti-phase)
    def get_data_test3(self):
        # find slope
        parameters = ['Lateral Wheel Centre Compliance [mm/N]',
                      'Lateral Wheel Centre Stiffness projected on ground [N/mm]',
                      'Lateral Toe Compliance [deg/N]',
                      'Lateral Camber Compliance [deg/N]',
                      'Lateral Tyre Stiffness [N/mm]',
                      'Force Roll Centre Height [mm/N]']
        data = self.__get_slope(self.__data, parameters, self.__df)
        
        # find y-intercept
        parameters = ['Force Roll Centre Height [mm/N]']
        data = self.__get_y_intercept(data, parameters, self.__df)
        
        return data

    
    # Lateral Compliance at -30mm X offset (in phase)
    def get_data_test4(self):
        # find slope
        parameters = ['Lateral Toe Compliance [deg/N]',
                      'Force Roll Centre Height [mm/N]',
                      'Lateral Wheel Centre Compliance [mm/N]',
                      'Lateral Wheel Centre Stiffness projected on ground [N/mm]',
                      'Lateral Camber Compliance [deg/N]',
                      'Lateral Tyre Stiffness [N/mm]',
                      'Load Transfer (Roll Centre Curve Fits) [N/N]']
        data = self.__get_slope(self.__data, parameters, self.__df)
        
        # find curves data
        parameters = ['Lateral Toe Compliance [deg/N]',
                      'Force Roll Centre Height [mm/N]']
        x = ['FrontLHwheelForceYN', 'FrontRHwheelForceYN',
             'RearLHwheelForceYN', 'RearRHwheelForceYN']
        y = [['FrontLHwheeltoeindeg', 'FLHForceRollCentreHeightmm'],
             ['FrontRHwheeltoeindeg', 'FRHForceRollCentreHeightmm'],
             ['RearLHwheeltoeindeg', 'RLHForceRollCentreHeightmm'],
             ['RearRHwheeltoeindeg', 'RRHForceRollCentreHeightmm']]
        data = self.__get_curve(data, parameters, x, y, self.__curve, 
                                self.__df)
        
        # find y-intercept
        parameters = ['Force Roll Centre Height [mm/N]']
        data = self.__get_y_intercept(data, parameters, self.__df)
        
        return data
    
    
    # Aligning Torque (in phase)(brake on, eng. on, ARB on)
    def get_data_test5(self):
        # find slope
        parameters = ['Toe Compliance [deg/Nm]', 'Camber Compliance [deg/Nm]',
                      'Tyre Aligning Stiffness [Nm/deg]',
                      'Steering Wheel Compliance [deg/Nm]']
        data = self.__get_slope(self.__data, parameters, self.__df)
        
        return data
    
    
    # Aligning Torque (anti-phase)(brake on, eng. on, ARB on)
    def get_data_test6(self):
        # find slope
        parameters = ['Toe Compliance [deg/Nm]', 'Camber Compliance [deg/Nm]',
                      'Tyre Aligning Stiffness [Nm/deg]',
                      'Steering Wheel Compliance [deg/Nm]']
        data = self.__get_slope(self.__data, parameters, self.__df)
        
        return data
    
    
    # Steering Geometry Mid-Mid
    def get_data_test7(self):
        # find slope 
        parameters = ['Percentage Ackermann', # no slope
                      'Instantaneous Steering Ratio [/deg]', # no slope
                      'Scrub Radius v Handwheel Steer [mm/deg]',
                      'Mechanical Trail v Handwheel Steer [mm/deg]',
                      'Camber Angle v Handwheel Steer [deg/deg]',
                      'Steering Ratio [deg/deg]',
                      'Handwheel Torque v Handwheel Steer [Nm/deg]', # Slope: Steer
                      'Kingpin Inclination Angle v Handwheel Steer [deg/deg]',
                      'Kingpin Castor Angle v Handwheel Steer [deg/deg]',
                      'Kingpin Offset v Handwheel Steer [mm/deg]']
        data = self.__get_slope(self.__data, parameters, self.__df)
        
        # find curves data
        parameters = ['Percentage Ackermann']
        x = ['FLSteerAngledeg', 'FRSteerAngledeg']
        y = [['RightTurnRHPercentageAckermann'],
             ['LeftTurnLHPercentageAckermann']]
        data = self.__get_curve(data, parameters, x, y, self.__curve, 
                                self.__df)
        
        parameters = ['Instantaneous Steering Ratio [/deg]',
                      'Scrub Radius v Handwheel Steer [mm/deg]',
                      'Mechanical Trail v Handwheel Steer [mm/deg]',
                      'Camber Angle v Handwheel Steer [deg/deg]']
        x = ['steeringwheelpositiondeg'] * 2
        y = [['FrontInstantaneousSteeringRatio', 'FLHScrubRadiusmm',
              'FLHMechanicalTrailmm', 'FrontLHwheelcamberdeg'],
             [None, 'FRHScrubRadiusmm',
              'FRHMechanicalTrailmm', 'FrontRHwheelcamberdeg']]
        data = self.__get_curve(data, parameters, x, y, self.__curve, 
                                self.__df)
    
        # find y-intercept
        parameters = ['Instantaneous Steering Ratio [/deg]',
                      'Kingpin Inclination Angle v Handwheel Steer [deg/deg]',
                      'Kingpin Castor Angle v Handwheel Steer [deg/deg]',
                      'Kingpin Offset v Handwheel Steer [mm/deg]']
        data = self.__get_y_intercept(data, parameters, self.__df)
        
        return data
    
    
    # Roll test at Constant Axle Load (brake on, eng. on, ARB on)
    def get_data_test8(self):
        # find slope
        parameters = ['Roll Steer v Roll Angle [deg/deg]',
                      'Roll Steer v Wheel to Body [deg/mm]',
                      'Roll Stiffnesses [Nm/deg]',
                      'Wheel Vertical Loads v Roll Angle [N/deg]',
                      'Wheel Vertical Rates [N/mm]',
                      'Roll Camber v Roll Angle [deg/deg]',
                      'Roll Camber v Wheel to Body [deg/mm]',
                      'Track Change [mm/deg]',
                      'Static Roll Weight Transfer Coefficient [/deg]',
                      'Kinematic Roll Centre Height [mm/deg]',
                      'Virtual Swing Arm Length [mm/deg]',
                      'Virtual Swing Arm Angle [deg/deg]',
                      'Track change variation [mm/mm]']
        data = self.__get_slope(self.__data, parameters, self.__df)
        
        # find curves data
        parameters = ['Roll Steer v Roll Angle [deg/deg]']
        x = ['BodyRollAngledeg'] * 4
        y = [['FrontLHwheeltoeindeg'], ['FrontRHwheeltoeindeg'],
             ['RearLHwheeltoeindeg'], ['RearRHwheeltoeindeg']]
        data = self.__get_curve(data, parameters, x, y, self.__curve, 
                                self.__df)
        
        parameters = ['Roll Steer v Wheel to Body [deg/mm]']
        x = ['FLHwheeltobodyZdisplacementmm', 'FRHwheeltobodyZdisplacementmm',
             'RLHwheeltobodyZdisplacementmm', 'RRHwheeltobodyZdisplacementmm']
        y = [['FrontLHwheeltoeindeg'], ['FrontRHwheeltoeindeg'],
             ['RearLHwheeltoeindeg'],['RearRHwheeltoeindeg']]
        data = self.__get_curve(data, parameters, x, y, self.__curve, 
                                self.__df)
        
        return data
    
    
    # Vertical Bounce test (brake on, eng. on, ARB on)
    def get_data_test10(self):
        # find slope
        parameters = ['Wheel Rates [N/mm]',
                      'Bump Steer [deg/mm]',
                      'Lateral Wheel Centre Displacement [mm/mm]',
                      'Longitudinal Wheel Centre Displacement [mm/mm]',
                      'Track Change [mm/mm]',
                      'Tyre Radial Rates [N/mm]',
                      'Ride Rates [N/mm]',
                      'Bump Camber [deg/mm]',
                      'Bump Spin [deg/mm]',
                      'Wheelbase Change [mm/mm]',
                      'Kinematic Roll Centre Height [mm/mm]',
                      'Virtual Swing Arm Length [mm/mm]',
                      'Virtual Swing Arm Angle [deg/mm]']
        data = self.__get_slope(self.__data, parameters, self.__df)
        
        # find curves data
        parameters = ['Wheel Rates [N/mm]', 'Bump Steer [deg/mm]',
                      'Lateral Wheel Centre Displacement [mm/mm]',
                      'Longitudinal Wheel Centre Displacement [mm/mm]']
        x = ['FLHwheeltobodyZdisplacementmm', 'FRHwheeltobodyZdisplacementmm',
             'RLHwheeltobodyZdisplacementmm', 'RRHwheeltobodyZdisplacementmm']
        y = [['FrontLHwheelForceZN', 'FrontLHwheeltoeindeg',
              'FrontLHwheelcentreYdispmm', 'FrontLHwheelcentreXdispmm'], 
             ['FrontRHwheelForceZN', 'FrontRHwheeltoeindeg',
              'FrontRHwheelcentreYdispmm', 'FrontRHwheelcentreXdispmm'],
             ['RearLHwheelForceZN', 'RearLHwheeltoeindeg',
              'RearLHwheelcentreYdispmm', 'RearLHwheelcentreXdispmm'],
             ['RearRHwheelForceZN', 'RearRHwheeltoeindeg',
              'RearRHwheelcentreYdispmm', 'RearRHwheelcentreXdispmm']]
        data = self.__get_curve(data, parameters, x, y, self.__curve, 
                                self.__df)
        
        parameters = ['Track Change [mm/mm]']
        x = ['CentreTableZDisplacementmm'] * 2
        y = [['FrontTrackchangemm'], ['RearTrackchangemm']]
        data = self.__get_curve(data, parameters, x, y, self.__curve, 
                                self.__df)
        
        # find y-intercept
        parameters = ['Kinematic Roll Centre Height [mm/mm]',
                      'Virtual Swing Arm Length [mm/mm]',
                      'Virtual Swing Arm Angle [deg/mm]']
        data = self.__get_y_intercept(data, parameters, self.__df)
        
        return data


    # Longitudinal (acceleration)(brake off, eng. on, ARB on)
    def get_data_strapped(self):
        # find slope
        parameters = ['Longitudinal Wheel Centre Compliance [mm/N]',
                      'Longitudinal Toe Compliance [deg/N]',
                      'Longitudinal Camber Compliance [deg/N]',
                      'Longitudinal Spin Compliance [deg/N]',
                      'Longitudinal Tyre Stiffness [N/mm]',
                      'Anti-Lift Front/Anti-Squat Rear Curve Fits [N/N]']
        data = self.__get_slope(self.__data, parameters, self.__df)
        
        # find curves data
        parameters = ['Longitudinal Wheel Centre Compliance [mm/N]',
                      'Longitudinal Toe Compliance [deg/N]']
        x = ['FrontLHwheelForceXN', 'FrontRHwheelForceXN',
             'RearLHwheelForceXN', 'RearRHwheelForceXN']
        y = [['FrontLHwheelcentreXdispmm', 'FrontLHwheeltoeindeg'], 
             ['FrontRHwheelcentreXdispmm', 'FrontRHwheeltoeindeg'],
             ['RearLHwheelcentreXdispmm', 'RearLHwheeltoeindeg'],
             ['RearRHwheelcentreXdispmm', 'RearRHwheeltoeindeg']]
        data = self.__get_curve(data, parameters, x, y, self.__curve, 
                                self.__df)
        return data

            
    
    def __get_slope(self, data, parameters, df):
        for para in parameters:
            data[para] = {}
            if para in ['Steering Wheel Compliance [deg/Nm]',
                        'Roll Stiffnesses [Nm/deg]',
                        'Track Change [mm/deg]',
                        'Track Change [mm/mm]']:
                slope_F = df.loc[para,'Front'].iloc[0]
                slope_R = df.loc[para,'Rear'].iloc[0]
                data[para]['slope'] = [slope_F,slope_R]
            
            elif para == 'Handwheel Torque v Handwheel Steer [Nm/deg]':
                slope_S = df.loc[para,'Steer'].iloc[0]
                data[para]['slope'] = [slope_S]
            
            elif para == 'Static Roll Weight Transfer Coefficient [/deg]':
                slope_V = df.loc[para,'Total'].iloc[0]
                data[para]['slope'] = [slope_V]
                
            elif para == 'Wheelbase Change [mm/mm]':
                slope_L = df.loc[para,'Left'].iloc[0]
                slope_R = df.loc[para,'Right'].iloc[0]
                data[para]['slope'] = [slope_L,slope_R]
                
            elif para in ['Longitudinal Wheel Centre Compliance [mm/N]',
                          'Lateral Toe Compliance [deg/N]',
                          'Roll Steer v Wheel to Body [deg/mm]',
                          'Wheel Rates [N/mm]',
                          'Bump Steer [deg/mm]']:
                '''
                All the wheels info are recorded for later stage when we 
                need to find the position where the curve trend starts to 
                change for each wheel, or compare the slope at a point with 
                the slope at 0.
                '''
                slope_FL = df.loc[para,'FL'].iloc[0]
                slope_FR = df.loc[para,'FR'].iloc[0]
                slope_Favg = df.loc[para,'F_avg'].iloc[0]
                slope_RL = df.loc[para,'RL'].iloc[0]
                slope_RR = df.loc[para,'RR'].iloc[0]
                slope_Ravg = df.loc[para,'R_avg'].iloc[0]
                data[para]['slope'] = [slope_FL, slope_FR, slope_Favg,
                                          slope_RL, slope_RR, slope_Ravg]
                
            elif para in ['Percentage Ackermann', 
                          'Instantaneous Steering Ratio [/deg]']:
                # don't need slope data, but we still need to create a dict
                continue
            
            else:
                slope_F = df.loc[para,'F_avg'].iloc[0]
                slope_R = df.loc[para,'R_avg'].iloc[0]
                data[para]['slope'] = [slope_F,slope_R]
        return data
    
    
    def __get_curve(self, data, parameters, x, y, df_curve, df):
        for para_index, para in enumerate(parameters):
            curve_missing = False
            '''
            find whether the curve data exists from summary_data.xlsx
            This step is necessary, because sometimes even there is no curve
            data for a particular curve, the program could still find
            the x and y values from the database, which are initially for 
            other parameters with the same axes names.
            '''
            if para != 'Percentage Ackermann': # no slope but curve is required
                curve_missing = df.loc[para].isnull().values.all()
            # print(para, curve_missing)
            if curve_missing:
                data[para]['curve'] = None
                continue
            
            data[para]['curve'] = []
            for i in range(len(x)): # FL/FR/RL/RR
                # sometimes there is slope data but curve data is missing...
                try:
                    x_data = list(df_curve[x[i]])
                except KeyError: # data for a specific wheel is missing
                    data[para]['curve'].append(None)
                    continue
                
                if y[i][para_index] is None:
                    continue
                else:
                    try:
                        y_data = list(df_curve[y[i][para_index]])
                    except KeyError:
                        # if para == 'Percentage Ackermann':
                        #     data[para]['curve'] = None
                        #     break
                        data[para]['curve'].append(None)
                        continue
                data[para]['curve'].append([x_data,y_data])
            if not any(data[para]['curve']):
                '''
                In this case, slope data is present in summary_data.csv, the 
                program would recognise the curve data to be present. However, 
                the curve data are stillng missing for all four wheels. For 
                example, there is no processed.mat in the database.
                '''
                data[para]['curve'] = None
            '''
            If data[para]['curve'] = None: that means the whole parameter is 
            missing. If data[para]['curve'] is a list with None, that means 
            the parameter is present but some wheel info might be absent.
            '''
        return data
    
    
    def __get_y_intercept(self, data, parameters, df):
        for para in parameters:
            search = para + '\ny-intercept'
            if para == 'Instantaneous Steering Ratio [/deg]':
                y_intercept_F = df.loc[search,'Front'].iloc[0]
                y_intercept_R = df.loc[search,'Rear'].iloc[0]
            else:
                y_intercept_F = df.loc[search,'F_avg'].iloc[0]
                y_intercept_R = df.loc[search,'R_avg'].iloc[0]
            data[para]['y-intercept'] = [y_intercept_F, y_intercept_R]
        return data


if __name__ == '__main__':
    import time
    from pyinstrument import Profiler
    from get_curve_paths import get_curve_paths
    
    store_path = r'D:\Desktop\KnC Store Path'
    profiler = Profiler()
    profiler.start()
    
    df_vehicles = pd.read_csv(store_path + '\\summary_data.csv')
    df_vehicles = df_vehicles.set_index('VEHICLES')
    
    with open(store_path + '\\Vehicle Summary.txt','r') as f:
        lines = f.readlines()
        veh_identities = [a.split('\t')[0] for a in lines]
    
    start = time.time()
    for veh_identity in veh_identities:
        # veh_name for searching columns in summary_data.csv without VehID,
        # veh_identity for searching csv with VehID 
        veh_name = veh_identity.rpartition('#')[0]
        print(veh_name)
        df_vehicle = df_vehicles[['Unnamed: 1', veh_name]]
        
        curve_data_paths = get_curve_paths(veh_identity, store_path)
             
        # start = time.time()
        sample_vehicle = VehRawData(df_vehicle, curve_data_paths)
        # end = time.time()
        # total += sample_vehicle.spent
        # print(sample_vehicle.all_data_missing)
        # print(sample_vehicle.data_test1)
        vehicle_wo_data = []
        if sample_vehicle.all_data_missing:
            vehicle_wo_data.append(veh_identity)
            # print(vehicle_identity)
            
    end = time.time()
    total = end - start
    print("time:%f"  % total)
    profiler.stop()
    profiler.print()
    # print("time:%f"  % spenta)
                
        
        
        