# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:26:18 2021

@author: Fanyi Sun
"""

import pandas as pd
import numpy as np

import sys
sys.path.append('..')
from match_test_name import get_full_test_name


def get_total_df_test(useful_data):
    total_df_test = []
    for test_number in useful_data.keys(): # for each test
        parameters, sub_index = get_test_para(useful_data[test_number],
                                              test_number)
        # for i in range(len(parameters)):
        #     print(parameters[i])
        #     print(sub_index[i])
        df_vehicle = []
        for veh_info in useful_data[test_number]:
            df_vehicle.append(generate_df_vehicle(veh_info, parameters))
        # add the information of a new vehicle by column
        df_test_data = pd.concat(df_vehicle, axis=1)
        
        parameters = remove_bracket(parameters)
        df_test_para = pd.DataFrame({'VEHICLES' : parameters,
                                             '' : sub_index})
        # set the first column as parameters and second column as wheels
        df_test_data = pd.concat([df_test_para,df_test_data], axis=1)
        total_df_test.append(df_test_data)

    # group the information for each test by rows
    total_df_test = pd.concat(total_df_test)
    return total_df_test


def get_test_para(test_info, test_number):
    test_name = get_full_test_name(test_number)
    
    # this is just for diaplay
    if test_number == 'test 7':
        test_name = 'Test 7_Steering Geometry Mid-Mid                               '
        
    parameters = [test_name]
    sub_index = [''] # ''is assigned to match 'test_name' in parameters
    for vehicle in test_info:
        for para in vehicle.keys():
            if para != 'vehicle name' and para not in parameters:
                # count how many wheels info in this parameter
                length = len(vehicle[para])
                # verify whether the y-intercept is recorded
                if type(vehicle[para][0]) == float:
                    parameters.extend([para] * length)
                    get_sub_index(sub_index, para, length)
                else: # type == list
                    parameters.extend([para] * length)
                    parameters.extend([para + '\ny-intercept']*length)
                    get_sub_index(sub_index, para, length)
                    get_sub_index(sub_index, para, length) # do it twice
    return parameters, sub_index


def get_sub_index(sub_index, para, length):
    """
    Find from the parameter name according to the parenthese location.
    
    Reverse and find the first '(' because some parameters contain
    more than one parentheses while index() only find the first.
    """
    x1 = len(para) - para[::-1].index('(')
    x2 = len(para) - para[::-1].index(')')
    x = para[x1:x2-1]
    if x == 'FL/FR/RL/RR':
        sub_index.extend(['FL','FR','F_avg','RL','RR','R_avg'])
    elif x == 'S':
        sub_index.append('Steer')
    elif x == 'V':
        sub_index.append('Total')
    elif x == 'F/R':
        sub_index.extend(['Front','Rear'])
    elif x == 'F/R/V':
        sub_index.extend(['Front','Rear','Total'])
    elif x == 'L/R':
        sub_index.extend(['Left','Right'])
    else: # for undefined names
        try:
            x = x.split('/')
            sub_index.extend(x)
        except: # if only one sub_index
            sub_index.append(x)


def generate_df_vehicle(veh_info, parameters):
    data = [np.nan] * len(parameters)
    veh_name = veh_info['vehicle name']
    for para in veh_info.keys():
        if para != 'vehicle name':
            pos = parameters.index(para)
            data_len = len(veh_info[para])
            # verify whether the y-intercept is recorded
            if type(veh_info[para][0]) == float:
                # assign the values in the corresponding position
                data[pos : pos+data_len] = veh_info[para]
            else:
                # add the gradient
                data[pos : pos+data_len] = [x[0] \
                    if type(x) == list else x for x in veh_info[para]]
                # add the y-intercept
                data[pos+data_len : pos+ 2*data_len] = [x[1] \
                    if type(x) == list else x for x in veh_info[para]]
                # in the else statement: x = np.nan
    df_vehicle = pd.DataFrame({veh_name : data})
    return df_vehicle


def remove_bracket(parameters):
    for i, para in enumerate(parameters):
        if 'Test' not in para:
            x1 = len(para) - para[::-1].index('(')
            x2 = len(para) - para[::-1].index(')')
            x = para[x1-1:x2+1] # +1 because one blank space to be removed
            # remove the wheels info inside the bracket
            parameters[i] = para.replace(x,'')
    return parameters

