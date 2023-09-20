# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:14:27 2021

@author: Fanyi Sun
"""

import numpy as np
from fractions import Fraction

from veh_raw_data import VehRawData


class VehKeyData(VehRawData):
    def __init__(self, df_vehicle, curve_data_paths):
        super().__init__(df_vehicle, curve_data_paths)
        
        tests = ['test1', 'test2', 'test4', 'test7', 
                  'test8', 'test10', 'strapped']
        for test in tests:
            self.__test = test
            if eval('self.data_%s' % test) is not None:
                eval('self.process_%s' % test)()
            
    
    # Longitudinal Compliance (braking)(brake on, eng. on, ARB on)
    def process_test1(self):
        # find the position where the curve trend starts to change
        para = 'Longitudinal Wheel Centre Compliance [mm/N]'
        self.__trend_change(self.__test, para)
        
    
    # Lateral Compliance at 0mm X offset (in phase)
    def process_test2(self):
        # find the slope at +-2000
        para = 'Lateral Toe Compliance [deg/N]'
        x = 2000
        slope_x = self.__find_slope_x(self.__test, para, x)
        self.data_test2[para]['slope%d' % x] = slope_x
        
        # find the difference of the slopes between +-2000 & 0
        self.__find_slope_x_diff(self.__test, para, x, slope_x)
        
        # find the max and min RCH
        para = 'Force Roll Centre Height [mm/N]'
        max_y, min_y = self.__find_max_y(self.__test, para)
        self.data_test2[para]['max_RCH'] = max_y
        self.data_test2[para]['min_RCH'] = min_y
        
        
    # Lateral Compliance at -30mm X offset (in phase)
    def process_test4(self):
        # find the slope at +-2000
        para = 'Lateral Toe Compliance [deg/N]'
        x = 2000
        slope_x = self.__find_slope_x(self.__test, para, x)
        self.data_test4[para]['slope%d' % x] = slope_x
        # find the difference of the slopes between +-2000 & 0
        self.__find_slope_x_diff(self.__test, para, x, slope_x)
        
        # find the max and min RCH
        para = 'Force Roll Centre Height [mm/N]'
        max_y, min_y = self.__find_max_y(self.__test, para)
        self.data_test4[para]['max_RCH'] = max_y
        self.data_test4[para]['min_RCH'] = min_y
        
        
    # Steering Geometry Mid-Mid
    def process_test7(self):
        para = 'Percentage Ackermann'
        # concat with left half from left turn and right half from right turn
        curve = self.data_test7[para]['curve']
        if curve is not None:
            x_left = np.array(curve[1][0])
            y_left = np.array(curve[1][1])
            x_right = np.array(curve[0][0])
            y_right = np.array(curve[0][1])
            x = list(x_left[x_left<0]) + list(x_right[x_right>0])
            y = list(y_left[x_left<0]) + list(y_right[x_right>0])
            self.data_test7[para]['curve'] = [[x,y]]
        # find the value at x = +- 20
        for x in [20,-20]:
            value = self.__find_value(self.__test, para, x)
            self.data_test7[para]['value%d' % x] = value
        # Ackermann value in left and right limitation
        if curve is not None:
            y_value = self.data_test7[para]['curve'][0][1]
            self.data_test7[para]['limit'] = [y_value[0],y_value[-1]]
        else:
            self.data_test7[para]['limit'] = None
            
        
        # non consistence calculation
        para = 'Instantaneous Steering Ratio [/deg]'
        if self.data_test7[para]['curve'] is None:
            self.data_test7[para]['non-consistence'] = None
        else:
            ydata = self.data_test7[para]['curve'][0][1]
            non_cst = (np.nanmax(ydata) - np.nanmin(ydata)) / np.nanmean(ydata)
            self.data_test7[para]['non-consistence'] = [non_cst]

        # find the difference of y-values at different +- x positions
        parameters = ['Scrub Radius v Handwheel Steer [mm/deg]',
                      'Mechanical Trail v Handwheel Steer [mm/deg]']
        x_positions = ['3/4', '1/2', '1/4']
        for para in parameters:
            data = self.data_test7[para]['curve']
            # find the difference of y-values at max and min x first
            if data is None:
                self.data_test7[para]['ychange_max'] = None
                for pos in x_positions:
                    self.data_test7[para]['ychange_%s' % pos] = None
                continue
            self.data_test7[para]['ychange_max'] = []
            x_max, x_min = [], []
            for wheel in data:
                if wheel is None:
                    self.data_test7[para]['ychange_max'].append(np.nan)
                    continue
                x_min.append(wheel[0][0])
                x_max.append(wheel[0][-1])
                y_left = wheel[1][0]
                y_right = wheel[1][-1]
                diff = y_right - y_left
                self.data_test7[para]['ychange_max'].append(diff)
            # find the difference of y-values at different x from [x_positions]
            for pos in x_positions:
                self.data_test7[para]['ychange_%s' % pos] = []
                for wheel in range(len(data)):
                    if data[wheel] is None:
                        self.data_test7[para]['ychange_%s'%pos].append(np.nan)
                        continue
                    x_left = x_min[wheel] * Fraction(pos)
                    x_right = x_max[wheel] * Fraction(pos)
                    y_left = self.__find_value(self.__test, para, x_left,
                                               curve=data[wheel])
                    y_right = self.__find_value(self.__test, para, x_right, 
                                                curve=data[wheel])
                    diff = y_right - y_left
                    self.data_test7[para]['ychange_%s'%pos].append(diff)
                    
        para = 'Camber Angle v Handwheel Steer [deg/deg]'
        # find the second derivative at x=0
        x = 0
        data = self.data_test7[para]['curve']
        if data is None:
            self.data_test7[para]['slope_grad0'] = None
        else:
            self.data_test7[para]['slope_grad0'] = []
            for wheel in data:
                if wheel is None:
                    self.data_test7[para]['slope_grad0'].append(np.nan)
                    continue
                pre, nex = self.__find_surrounding_nodes(wheel, x)
                # find the 2nd derivative at pre and next nodes respectively
                xdata = wheel[0]
                ydata = wheel[1]
                # using Central Finite Difference Approximation
                dx = nex[0] - pre[0]
                pos = xdata.index(pre[0])
                d2y_pre = (ydata[pos+1] - 2* ydata[pos] + ydata[pos-1]) /\
                                                                    dx ** 2
                pos = xdata.index(nex[0])
                d2y_nex = (ydata[pos+1] - 2* ydata[pos] + ydata[pos-1]) /\
                                                                    dx ** 2
                # linear interpolation to find d2y at x
                d2y = d2y_pre + (x - pre[0]) / (nex[0] - pre[0]) * \
                                                    (d2y_nex - d2y_pre)
                self.data_test7[para]['slope_grad0'].append(d2y)
        # toe value in left and right limitation
        if data is None:
            self.data_test7[para]['limit'] = None
        else:
            self.data_test7[para]['limit'] = []
            for wheel in data:
                if wheel is None:
                    self.data_test7[para]['limit'].append(None)
                    continue
                y_value = wheel[1]
                self.data_test7[para]['limit'].append([y_value[0],y_value[-1]])
            
            
    # Roll test at Constant Axle Load (brake on, eng. on, ARB on)
    def process_test8(self):
        # find the difference of slopes between -1&1, -2&2, -4&4
        para = 'Roll Steer v Roll Angle [deg/deg]'
        for x in [1,2,4]:
            key = "self.data_test8[para]['slope_diff%d']" % x
            slope_x = self.__find_slope_x(self.__test, para, x)
            if slope_x is None:
                exec(f"{key} = None")
                continue
            slope_diff = [(i[0] - i[1]) if i is not None else np.nan
                          for i in slope_x]
            exec(f"{key} = slope_diff")
        
        # find the slope at +- 50
        para = 'Roll Steer v Wheel to Body [deg/mm]'
        x = 50
        slope_x = self.__find_slope_x(self.__test, para, x)
        self.data_test8[para]['slope%d' % x] = slope_x
        # find the difference of the slopes between +-50 & 0
        self.__find_slope_x_diff(self.__test, para, x, slope_x)
    
        # split the curves into intervals 
        # do it last because the curve data is needed for early stage
        para = 'Roll Steer v Roll Angle [deg/deg]'
        interval = [0,2,4]
        self.__curve_interval(self.__test, para, interval)
        para = 'Roll Steer v Wheel to Body [deg/mm]'
        interval = [0,20]
        self.__curve_interval(self.__test, para, interval)
    
    
    # Vertical Bounce test (brake on, eng. on, ARB on)
    def process_test10(self):
        # find the position where the curve trend starts to change
        para = 'Wheel Rates [N/mm]'
        self.__trend_change(self.__test, para)
        
        para = 'Bump Steer [deg/mm]'
        # find the slope at +- 50
        x = 50
        slope_x = self.__find_slope_x(self.__test, para, x)
        self.data_test10[para]['slope%d' % x] = slope_x
        # record the slope at 0 for later stage before they are cutted
        slope0 = self.data_test10[para]['slope']
        slope0 = slope0[:2] + slope0[3:5] # four wheels
        # find the difference of the slopes between +-50 & 0
        self.__find_slope_x_diff(self.__test, para, x, slope_x)
        # find the value at x = 20
        x = 20
        value_20 = self.__find_value(self.__test, para, x)
        self.data_test10[para]['value%d' % x] = value_20
        # find the deviation at -70mm, using the data found before
        x = -70
        value_n70 = self.__find_value(self.__test, para, x)
        if value_n70 is None:
            self.data_test10[para]['deviation-70'] = None
        else:
            deviation = []
            for i in range(len(slope0)): # for each wheel
                dev = value_20[i] - slope0[i] * (20 + 70) - value_n70[i]
                deviation.append(dev)
            self.data_test10[para]['deviation-70'] = deviation
        
        
        # find the maximum change in y
        parameters = ['Lateral Wheel Centre Displacement [mm/mm]',
                      'Longitudinal Wheel Centre Displacement [mm/mm]',
                      'Track Change [mm/mm]']
        for para in parameters:
            max_y, min_y = self.__find_max_y(self.__test, para)
            if max_y is None or min_y is None:
                self.data_test10[para]['max_ychange'] = None
                continue
            ychange = np.array(max_y) - np.array(min_y)
            self.data_test10[para]['max_ychange'] = list(ychange)
        
        # split the curves into intervals 
        parameters = ['Bump Steer [deg/mm]', 
                      'Lateral Wheel Centre Displacement [mm/mm]',
                      'Longitudinal Wheel Centre Displacement [mm/mm]',
                      'Track Change [mm/mm]']
        all_intervals = [[0,20,50,70], [0,50], [0,50], [0,20,50,100]]
        for i in range(len(parameters)):
            self.__curve_interval(self.__test, parameters[i], all_intervals[i])
        del self.data_test10['Track Change [mm/mm]']['curve_above100']
        

    # Longitudinal (acceleration)(brake off, eng. on, ARB on)
    def process_strapped(self):
        # find the position where the curve trend starts to change
        para = 'Longitudinal Wheel Centre Compliance [mm/N]'
        self.__trend_change(self.__test, para)
        
        
    def __find_value(self, test, para, x, curve=None):
        """
        find the y value at a particular point
        Normally this function find the values for 4 wheels and outputs
        a list. But if there is a curve input, it means the function only
        look at one wheel, and the curve input is for this specific wheel.
        But before inputting curve, make sure it is not None, ie. the curve
        data exists.
        """
        if curve is not None:
            pre, nex = self.__find_surrounding_nodes(curve, x)
            if pre is None or nex is None:
                return np.nan
            # linear interpolation
            y = pre[1] + (nex[1] - pre[1])/(nex[0] - pre[0]) * (x - pre[0])
            return y
        
        data = eval("self.data_%s[para]['curve']" % test)
        if data is None:
            return None
        
        value = []
        for wheel in data:
            if wheel is None:
                value.append(np.nan)
                continue
            pre, nex = self.__find_surrounding_nodes(wheel, x)
            if pre is None or nex is None:
                value.append(np.nan)
                continue
            # linear interpolation
            y = pre[1] + (nex[1] - pre[1])/(nex[0] - pre[0]) * (x - pre[0])
            value.append(y)
        return value
        
        
    def __find_max_y(self, test, para):
        """
        find the maximum and minimum y values of curves
        """
        data = eval("self.data_%s[para]['curve']" % test)
        if data is None:
            return None, None
        
        max_y, min_y = [], []
        for wheel in data:
            if wheel is None:
                max_y.append(np.nan)
                min_y.append(np.nan)
                continue
            max_y.append(np.nanmax(wheel[1]))
            min_y.append(np.nanmin(wheel[1]))
        return max_y, min_y
    
    
    def __find_slope_x(self, test, para, x):
        """
        find the slope at particular positions (+- x)
        """
        data = eval("self.data_%s[para]['curve']" % test)
        if data is None: # if parameter data absent
            return None

        slope_x = []
        for wheel in data:
            if wheel is None:
                slope_x.append(None)
                continue
            
            slopes = [] # each wheel has slopes at positive and negative x
            for x_target in [x,-x]:
                pre, nex = self.__find_surrounding_nodes(wheel, x_target)
                if pre is None or nex is None:
                    # x_target is outside of the curve
                    slopes.append(np.nan)
                    continue
                slope = (nex[1] - pre[1]) / (nex[0] - pre[0])
                slopes.append(slope)
            slope_x.append(slopes)
        return slope_x
    
    
    def __find_surrounding_nodes(self, curve, x_target):
        """
        search the closest point to x from the curve and output its y value
        """
        x = curve[0]
        y = curve[1]
        min_diff = 1e5
        # search the closest point
        for i in range(1,len(x)-1): # ignore the first and last index
            if abs(x_target - x[i]) < min_diff:
                min_diff = abs(x_target - x[i])
                pos = i
                
        # record the surrounding points
        if x_target >= x[pos]:
            pre = [x[pos],y[pos]]
            nex = [x[pos+1],y[pos+1]]
        else:
            pre = [x[pos-1],y[pos-1]]
            nex = [x[pos],y[pos]]
            
        if x_target > nex[0] or x_target < pre[0]:
            # x_target is outside of the curve
            return [None,None]
        return [pre,nex]
    
    
    def __find_slope_x_diff(self, test, para, x, slope_x):
        """
        find the difference of the slopes between +- x and 0
        """
        # find the slope at 0 from summary_data.csv
        key = "self.data_%s[para]['slope']" % test
        slope_FL = eval(key)[0]
        slope_FR = eval(key)[1]
        slope_Favg = eval(key)[2]
        slope_RL = eval(key)[3]
        slope_RR = eval(key)[4]
        slope_Ravg = eval(key)[5]
        slope0 = [slope_FL, slope_FR, slope_RL, slope_RR]
        # reassign slope data, only these two are kept
        exec(f"{key} = [slope_Favg, slope_Ravg]")
        
        key_diff = "self.data_%s[para]['slope%d_diff']" % (test, x)
        if slope_x is None:
            exec(f"{key_diff} = None")
            return 
        
        exec(f"{key_diff} = []")
        for wheel in range(len(slope0)):
            if slope_x[wheel] is None:
                eval(key_diff).append(None)
                continue
            slope_diff = [(x - slope0[wheel]) for x in slope_x[wheel]]
            eval(key_diff).append(slope_diff)
            
            
    def __trend_change(self, test, para):
        """
        find the position where the curve trend starts to change
        """
        data = eval("self.data_%s[para]['curve']" % test)
        key = "self.data_%s[para]['slope']" % test
        slope_FL = eval(key)[0]
        slope_FR = eval(key)[1]
        slope_Favg = eval(key)[2]
        slope_RL = eval(key)[3]
        slope_RR = eval(key)[4]
        slope_Ravg = eval(key)[5]
        slope = [slope_FL, slope_FR, slope_RL, slope_RR]
        # reassign slope data, only these two are kept
        exec(f"{key} = [slope_Favg, slope_Ravg]")
        
        key_left = "self.data_%s[para]['trend_change_left']" % test
        key_right = "self.data_%s[para]['trend_change_right']" % test
        if data is None: # if parameter data absent
            exec(f"{key_left} = None")
            exec(f"{key_right} = None")
            return
        
        exec(f"{key_left} = []")
        exec(f"{key_right} = []")
        for wheel in range(len(data)):
            curve = data[wheel] # curve contains one x and one y
            if curve is None: # if wheel data absent
                eval(key_left).append(np.nan)
                eval(key_left).append(np.nan)
                continue
            
            # split into left and right
            x_left = curve[0][:int(len(curve[0]) / 2)][::-1]
            y_left = curve[1][:int(len(curve[0]) / 2)][::-1]
            x_right = curve[0][int(len(curve[0]) / 2):]
            y_right = curve[1][int(len(curve[0]) / 2):]
            
            pos_left, pos_right = None, None # in case the point is not found
            for i in range(len(x_left) - 1):
                slope_local = (y_left[i+1] - y_left[i]) / \
                                            (x_left[i+1] - x_left[i])
                if np.abs((slope_local - slope[wheel]) / slope[wheel]) > 0.2:
                    pos_left = i
                    break
            
            for i in range(len(x_right) - 1):
                slope_local = (y_right[i+1] - y_right[i]) / \
                                            (x_right[i+1] - x_right[i])
                if np.abs((slope_local - slope[wheel]) / slope[wheel]) > 0.2:
                    pos_right = i
                    break
            if pos_left is not None:
                eval(key_left).append(x_left[pos_left])
            else: # if not found
                eval(key_left).append(np.nan)
            if pos_right is not None:
                eval(key_right).append(x_right[pos_right])
            else:
                eval(key_right).append(np.nan)
                
    
    def __curve_interval(self, test, para, interval):
        """
        split the curves into several sub-intervals
        """
        data = eval("self.data_%s[para]" % (test)).pop('curve')
                                                 
        for i in range(len(interval)):
            # create a empty list for each interval
            if i == len(interval) - 1: # for the outermost interval
                key = "self.data_%s[para]['curve_above%d']" \
                            % (test, interval[-1])
            else:
                key = "self.data_%s[para]['curve_%dto%d']" \
                            % (test, interval[i], interval[i+1])
            if data is None: # if para info absent
                exec(f"{key} = None")
                continue
            
            exec(f"{key} = []")
            for wheel in data:
                if wheel is None: # if wheel info absent
                    eval(key).append(None)
                    continue
                
                x = wheel[0]
                y = wheel[1]
                x_interval, y_interval = [], []
                for node in range(len(x)):
                    if i == len(interval) - 1:
                        if (x[node] >= interval[i] or x[node] <= -interval[i]):
                            x_interval.append(x[node])
                            y_interval.append(y[node])
                    else:
                        if ((x[node] >= interval[i] and 
                             x[node] < interval[i+1]) or
                            (x[node] <= -interval[i] and 
                             x[node] > -interval[i+1])):
                            x_interval.append(x[node])
                            y_interval.append(y[node])
                if not x_interval or not y_interval: # empty list
                    eval(key).append(None)
                else:
                    eval(key).append([x_interval, y_interval])
        

if __name__ == '__main__':
    import pandas as pd
    import time
    
    from get_curve_paths import get_curve_paths
    
    store_path = r'D:\Desktop\KnC Store Path'
    start = time.time()
    df_vehicles = pd.read_csv(store_path + '\\summary_data.csv')
    df_vehicles = df_vehicles.set_index('VEHICLES')
    
    with open(store_path + '\\Vehicle Summary.txt','r') as f:
        lines = f.readlines()
        veh_identities = [a.split('\t')[0] for a in lines]
        
    for veh_identity in veh_identities:
        # veh_name for searching columns in summary_data.csv without VehID,
        # veh_identity for searching csv with VehID 
        veh_name = veh_identity.rpartition('#')[0]
        print(veh_name)
        df_vehicle = df_vehicles[['Unnamed: 1', veh_name]]
        
        curve_data_paths = get_curve_paths(veh_identity, store_path)
        sample_vehicle = VehKeyData(df_vehicle, curve_data_paths)
        
        # print(sample_vehicle.data_test8)
        # a = sample_vehicle.data_test7['Camber Angle v Handwheel Steer [deg/deg]']['curve'][0]
        # if sample_vehicle.data_test4 is not None:
        #     for key,value in sample_vehicle.data_test8.items():
        #         print(key)
        #         for feature, data in value.items():
        #             # if 'curve' not in feature:
        #             print(feature)
        #             print(data)
        #         print('\n')
    end = time.time()
    print('time:%f' % (end - start))
