# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 10:13:06 2021

@author: Fanyi Sun
"""

import numpy as np


def arrange_data(database):
    # The input is a list of dict
    database['test 1'] = process_test_1(database['test 1'])
    database['test 2'] = process_test_2to4(database['test 2'])
    database['test 3'] = process_test_2to4(database['test 3'])
    database['test 4'] = process_test_2to4(database['test 4'])
    database['test 5'] = process_test(database['test 5']) # usual case
    database['test 6'] = process_test(database['test 6']) # usual case
    database['test 7'] = process_test_7(database['test 7'])
    database['test 8'] = process_test(database['test 8']) # usual case
    database['test 10'] = process_test_10(database['test 10'])
    database['strapped'] = process_test_1(database['strapped']) # same as test1
    return database


def process_test(data): 
    '''
    This function handles with usual cases (no y-intercept recoreded, 
    no parameter name changed).
    '''
    # state for which parameters the y_intercepts are required
    y_intercept = []
    for i in range(len(data)):
        # data[i] is a dict with the info for each vehicle
        for para in data[i].keys():
            if para != 'vehicle name':
                # data[i][para] is a list contains 4 sublists of 4 wheels
                data = take_useful_data(data, i, para, y_intercept)
                # add the average of the left and right wheels
                insert_average(data[i][para])
    return data

        
def process_test_1(data):
    y_intercept = ['Force Anti-Dive Angles (FL/FR/RL/RR) [deg/N]']
    for i in range(len(data)):
# =============================================================================
#         # change the name of some parameters
#         old_name = 'Longitudinal Wheel Centre Stiffness (FL/FR/RL/RR) [N/mm]'
#         new_name = 'Longitudinal Wheel Centre Compliance (FL/FR/RL/RR) [mm/N]'
#         data[i] = rename_parameter(new_name, old_name, data[i])
# =============================================================================
        
        for para in data[i].keys():
            if para != 'vehicle name':
                data = take_useful_data(data, i, para, y_intercept)
                insert_average(data[i][para])
    return data
            

def process_test_2to4(data):
    y_intercept = ['Force Roll Centre Height (FL/FR/RL/RR) [mm/N]']
    for i in range(len(data)):
        old_name = 'Roll Centre Curve Fits (FL/FR/RL/RR) [N/N]'
        new_name = 'Load Transfer (Roll Centre Curve Fits) (FL/FR/RL/RR) [N/N]'
        data[i] = rename_parameter(new_name, old_name, data[i])
        
# =============================================================================
#         old_name = 'Lateral Wheel Centre Stiffness (FL/FR/RL/RR) [N/mm]'
#         new_name = 'Lateral Wheel Centre Compliance (FL/FR/RL/RR) [mm/N]'
#         data[i] = rename_parameter(new_name, old_name, data[i])
# =============================================================================
        for para in data[i].keys():
            if para != 'vehicle name':
                data = take_useful_data(data, i, para, y_intercept)
                insert_average(data[i][para])
    return data


def process_test_7(data):
    y_intercept = ['Instantaneous Steering Ratio (F/R) [/deg]',
                   'Camber Angle v Roadwheel Steer (FL/FR/RL/RR) [deg/deg]',
                   'Kingpin Inclination Angle v Handwheel Steer (FL/FR/RL/RR) [deg/deg]',
                   'Kingpin Castor Angle v Handwheel Steer (FL/FR/RL/RR) [deg/deg]',
                   'Scrub Radius v Handwheel Steer (FL/FR/RL/RR) [mm/deg]',
                   'Mechanical Trail v Handwheel Steer (FL/FR/RL/RR) [mm/deg]',
                   'Kingpin Offset v Handwheel Steer (FL/FR/RL/RR) [mm/deg]',]
    for i in range(len(data)):
        for para in data[i].keys():
            if para != 'vehicle name':
                data = take_useful_data(data, i, para, y_intercept)
                insert_average(data[i][para])
# =============================================================================
#                 if para == 'Steering Ratio (FL/FR/RL/RR) [deg/deg]':
#                     # find the reciprocal
#                     data[i][para] = [1 / x for x in data[i][para]]
# =============================================================================
    return data


def process_test_10(data):
    y_intercept = ['Track Change (F/R) [mm/mm]',
                   'Kinematic Roll Centre Height (FL/FR/RL/RR) [mm/mm]',
                   'Virtual Swing Arm Length (FL/FR/RL/RR) [mm/mm]',
                   'Virtual Swing Arm Angle (FL/FR/RL/RR) [deg/mm]']
    for i in range(len(data)):
        old_name = 'Wheel Recession (FL/FR/RL/RR) [mm/mm]'
        new_name = 'Longitudinal Wheel Centre Displacement (FL/FR/RL/RR) [mm/mm]'
        data[i] = rename_parameter(new_name, old_name, data[i])
        
        for para in data[i].keys():
            if para != 'vehicle name':
                data = take_useful_data(data, i, para, y_intercept)
                insert_average(data[i][para])
    return data
# =============================================================================
#         '''
# if para == 'Longitudinal Wheel Centre Stiffness (FL/FR/RL/RR) [N/mm]':
#                         new = 'Longitudinal Wheel Centre Compliance (FL/FR/RL/RR) [mm/N]'
#                         info_dict[new] = []
#                     elif para == 'Lateral Wheel Centre Stiffness (FL/FR/RL/RR) [N/mm]':
#                         new = 'Lateral Wheel Centre Compliance (FL/FR/RL/RR) [mm/N]'
#                         info_dict[new] = []
#                     else:
#                         info_dict[para] = []
#                 else:
#                     if para == ('Longitudinal Wheel Centre Stiffness (FL/FR/RL/RR) [N/mm]'
#                                 or 'Lateral Wheel Centre Stiffness (FL/FR/RL/RR) [N/mm]'):
#                         number = [1 / x for x in number] # find the reciprocal
#                     info_dict[para].append(number)'''
# =============================================================================

def rename_parameter(new_name, old_name, Dict):
    # change the parameter name without changing the order of the dict
# =============================================================================
#     new_dict = {}
#     for k, v in Dict.items():
#         if k == old_name:
#             if (k == 'Longitudinal Wheel Centre Stiffness (FL/FR/RL/RR) [N/mm]'
#                 or k == 'Lateral Wheel Centre Stiffness (FL/FR/RL/RR) [N/mm]'):
#                 v = [[1 / x[0], x[1]] for x in v] # find reciprocal for slope
#             new_dict[new_name] = v
#         else:
#             new_dict[k] = v
# =============================================================================
    Dict = dict([(new_name,v) if k == old_name 
                  else (k,v) for k,v in Dict.items()])
    return Dict

    
def take_useful_data(data, i, para, y_intercept):
    if para in y_intercept:
        # record both the gradient and y-intercept:
        # if x is not a list, it's None and record np.nan
        data[i][para] = [x[-2:] if type(x) == list 
                             else x for x in data[i][para]]
    else:
        # record the gradient only:
        data[i][para] = [x[-2] if type(x) == list 
                             else x for x in data[i][para]]
    return data


def insert_average(data):
    if len(data) == 4: # 4 wheels
        if type(data[0]) == float: # (contain gradient only)
            '''
            If the left and right data have opposite signs, the average
            is chosen to be their absolute average with the same sign as 
            the left data.
            '''
            if np.sign(data[0]) == np.sign(data[1]):
                avg_left = (data[0] + data[1]) / 2
            else:
                avg_left = (data[0] - data[1]) / 2
            if np.sign(data[2]) == np.sign(data[3]):
                avg_right = (data[2] + data[3]) / 2
            else:
                avg_right = (data[2] - data[3]) / 2
            data.insert(2,avg_left)
            data.insert(5,avg_right)
        else: # if it's a list (contain gradient and y-intercept)
            avg_left = [(data[0][i] + data[1][i]) / 2 
                            if np.sign(data[0][i]) == np.sign(data[1][i])
                            else (data[0][i] - data[1][i]) / 2 for i in [0,1]]
            try:
                avg_right = [(data[2][i] + data[3][i]) / 2 
                            if np.sign(data[2][i]) == np.sign(data[3][i])
                            else (data[2][i] - data[3][i]) / 2 for i in [0,1]]
            except TypeError: # np.nan is not subscriptable
                # if lack of data of rear wheels (ie.None)
                avg_right = np.nan
            data.insert(2,avg_left)
            data.insert(5,avg_right)
    return data