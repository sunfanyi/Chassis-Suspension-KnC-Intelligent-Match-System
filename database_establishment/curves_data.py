# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:16:20 2021

@author: Fanyi Sun
"""

import os
import sys
import pandas as pd
import numpy as np
from scipy.io import loadmat

from get_files import get_test_data_paths

sys.path.append('..')
from create_dir import create_dir


def get_curves_data(df_raw, df_processed, veh_identity, test_number, file_path):
    """
    for each sublist: the first parameter is in x-axis, and the others are y.
    eg. if length == 3, the last two parameters share the same x.
    """
    if test_number == 'test 1':
        parameters = [['FrontLHwheelForceXN', 'FrontLHwheelcentreXdispmm',
                       'FrontLHwheeltoeindeg'],
                      ['FrontRHwheelForceXN', 'FrontRHwheelcentreXdispmm',
                       'FrontRHwheeltoeindeg'],
                      ['RearLHwheelForceXN', 'RearLHwheelcentreXdispmm',
                       'RearLHwheeltoeindeg'],
                      ['RearRHwheelForceXN', 'RearRHwheelcentreXdispmm',
                       'RearRHwheeltoeindeg']]

    elif test_number == 'test 2' or test_number == 'test 4':
        parameters = [['FrontLHwheelForceYN', 'FrontLHwheeltoeindeg',
                       'FLHForceRollCentreHeightmm'],
                      ['FrontRHwheelForceYN', 'FrontRHwheeltoeindeg',
                       'FRHForceRollCentreHeightmm'],
                      ['RearLHwheelForceYN', 'RearLHwheeltoeindeg',
                       'RLHForceRollCentreHeightmm'],
                      ['RearRHwheelForceYN', 'RearRHwheeltoeindeg',
                       'RRHForceRollCentreHeightmm']]

    elif test_number == 'test 7':
        parameters = [['FRSteerAngledeg', 'LeftTurnLHPercentageAckermann'],
                      ['FLSteerAngledeg', 'RightTurnRHPercentageAckermann'],
                      ['steeringwheelpositiondeg',
                       'FrontInstantaneousSteeringRatio',
                       'FrontLHwheelcamberdeg', 'FrontRHwheelcamberdeg',
                       'FLHScrubRadiusmm', 'FRHScrubRadiusmm',
                       'FLHMechanicalTrailmm', 'FRHMechanicalTrailmm']]

    elif test_number == 'test 8':
        parameters = [['BodyRollAngledeg',
                       'FrontLHwheeltoeindeg', 'FrontRHwheeltoeindeg',
                       'RearLHwheeltoeindeg', 'RearRHwheeltoeindeg'],
                      ['FLHwheeltobodyZdisplacementmm', 'FrontLHwheeltoeindeg'],
                      ['FRHwheeltobodyZdisplacementmm', 'FrontRHwheeltoeindeg'],
                      ['RLHwheeltobodyZdisplacementmm', 'RearLHwheeltoeindeg'],
                      ['RRHwheeltobodyZdisplacementmm', 'RearRHwheeltoeindeg']]

    elif test_number == 'test 10':
        parameters = [['FLHwheeltobodyZdisplacementmm',
                       'FrontLHwheelForceZN', 'FrontLHwheeltoeindeg',
                       'FrontLHwheelcentreYdispmm',
                       'FrontLHwheelcentreXdispmm'],
                      ['FRHwheeltobodyZdisplacementmm',
                       'FrontRHwheelForceZN', 'FrontRHwheeltoeindeg',
                       'FrontRHwheelcentreYdispmm',
                       'FrontRHwheelcentreXdispmm'],
                      ['RLHwheeltobodyZdisplacementmm',
                       'RearLHwheelForceZN', 'RearLHwheeltoeindeg',
                       'RearLHwheelcentreYdispmm', 'RearLHwheelcentreXdispmm'],
                      ['RRHwheeltobodyZdisplacementmm',
                       'RearRHwheelForceZN', 'RearRHwheeltoeindeg',
                       'RearRHwheelcentreYdispmm', 'RearRHwheelcentreXdispmm'],
                      ['CentreTableZDisplacementmm',
                       'FrontTrackchangemm', 'RearTrackchangemm']]

    elif test_number == 'strapped':
        parameters = [['FrontLHwheelForceXN', 'FrontLHwheelcentreXdispmm',
                       'FrontLHwheeltoeindeg'],
                      ['FrontRHwheelForceXN', 'FrontRHwheelcentreXdispmm',
                       'FrontRHwheeltoeindeg'],
                      ['RearLHwheelForceXN', 'RearLHwheelcentreXdispmm',
                       'RearLHwheeltoeindeg'],
                      ['RearRHwheelForceXN', 'RearRHwheelcentreXdispmm',
                       'RearRHwheeltoeindeg']]
    try:
        info_dict = loadmat(file_path)
    except TypeError:
        print('Unable to read MAT-file: %s. File might be corrupt.' % file_path)
        return df_raw, df_processed
    except Exception as e:
        print('Unable to read MAT-file: %s. Errortype: %s' % (file_path, e))
        return df_raw, df_processed

    del info_dict['__globals__']
    del info_dict['__header__']
    del info_dict['__version__']

    for group in parameters:
        # each group is a list with the first item containing x-axis info
        group_data = []
        # record the x-axis first
        for para in info_dict.keys():
            if para == group[0]:
                df_raw, group_data = store_raw_data(para, info_dict[para],
                                                    df_raw, group_data)
        # for the y-axis, save with order
        for y_para in group[1:]:
            for para in info_dict.keys():
                if para == y_para:
                    df_raw, group_data = store_raw_data(para, info_dict[para],
                                                        df_raw, group_data)
        # for each group
        df_processed, data_correct = hysteresis_approximation(df_processed,
                                      group_data, veh_identity, test_number)
        # add an empty column
        df_raw = pd.concat([df_raw, pd.DataFrame({'': [np.nan]})], axis=1)
        if data_correct:
            df_processed = pd.concat([df_processed,
                                      pd.DataFrame({'': [np.nan]})], axis=1)
    return df_raw, df_processed


def store_raw_data(para, info, df_raw, group_data):
    # for some parameters the offset are not considered
    para_wo_offset = ['FrontLHwheelForceXN', 'FrontRHwheelForceXN',
                      'RearLHwheelForceXN', 'RearRHwheelForceXN',
                      'FrontLHwheelForceYN', 'FrontRHwheelForceYN',
                      'RearLHwheelForceYN', 'RearRHwheelForceYN',
                      'FrontLHwheelForceZN', 'FrontRHwheelForceZN',
                      'RearLHwheelForceZN', 'RearRHwheelForceZN',
                      'FLHForceRollCentreHeightmm',
                      'FRHForceRollCentreHeightmm',
                      'RLHForceRollCentreHeightmm',
                      'RRHForceRollCentreHeightmm',
                      'FRSteerAngledeg', 'FLSteerAngledeg',
                      'LeftTurnLHPercentageAckermann',
                      'RightTurnRHPercentageAckermann',
                      'FrontLHwheelcamberdeg',
                      'FrontRHwheelcamberdeg',
                      'steeringwheelpositiondeg',
                      'FrontInstantaneousSteeringRatio',
                      'FLHScrubRadiusmm', 'FRHScrubRadiusmm',
                      'FLHMechanicalTrailmm', 'FLHMechanicalTrailmm']
    data = info[0][0][0]
    if para in para_wo_offset:
        data = [float(x[0]) for x in data]
    else:
        setup_offset = info[0][0][1][0][0]
        data = [float(x[0]) - setup_offset for x in data]
    try:
        df_raw = pd.concat([df_raw, pd.DataFrame({para: data})], axis=1)
    except ValueError:
        print('Different data size can\'t be used for plotting')

    # for each para, store the para_name first:
    value = [para]
    value.extend(data)
    # group_data is used for df_processed
    group_data.append(value)
    return df_raw, group_data


def hysteresis_approximation(df_processed, group_data, veh_identity,
                             test_number):
    for para in range(len(group_data)):
        '''
        Most tests already take 1024 values so nothing is changed.
        For some tests, 2048 values are taken, only the first 1024 values 
        are interested because they are enough to form a loop.
        '''
        group_data[para][1:] = group_data[para][1:][:1024]

    # print('\n','x-para:',group_data[0][0]) # print x-para name
    x1 = group_data[0][1:][768:] + group_data[0][1:][:256]
    x2 = group_data[0][1:][256:768][::-1]
    reverse = False
    if x1[-1] < x1[0]:
        reverse = True

    if x1[-1] < x1[0] and x2[-1] > x2[0]:  # ideally impossible
        print('wtfffffffff')

    fit = 0
    for x in [x1, x2]:
        if reverse:
            x.reverse()
        # test if two curves are split correctly
        for i in range(511):
            if x[i + 1] > x[i]:
                fit += 1

    data_correct = True
    if fit < 0.6 * 1024:
        data_correct = False
        print('incorrect x-values in', veh_identity, test_number,
              group_data[0][0])

    # set default interval for plotting:
    # choose the smaller value at x1&x2 to avoid list out of range issue 
    x_leftmost = x1[0] if abs(x1[0]) < abs(x2[0]) else x2[0]
    x_rightmost = x1[-1] if abs(x1[-1]) < abs(x2[-1]) else x2[-1]
    xn = np.linspace(x_leftmost, x_rightmost, 50)  # reduce from 1024 to 50

    if not data_correct:
        df_processed = pd.DataFrame({})
        return df_processed, data_correct

    # x-value is same for each group
    df_processed[group_data[0][0]] = xn
    for y_value in group_data[1:]:  # for each y in this group
        # print(y_value[0]) # print y-para name
        y1 = y_value[1:][768:] + y_value[1:][:256]
        y2 = y_value[1:][256:768][::-1]

        if reverse:
            y1.reverse()
            y2.reverse()

        yn1 = curve_redistribution(xn, x1, y1)
        yn2 = curve_redistribution(xn, x2, y2)
        # take average
        yn = [(yn1[i] + yn2[i]) / 2 for i in range(len(xn))]

        df_processed = pd.concat([df_processed, pd.DataFrame({y_value[0]: yn})],
                                 axis=1)
    return df_processed, data_correct


def curve_redistribution(xn, x_original, y_original):
    yn = []
    for x in xn:
        min_diff = 1e5
        # search the closest point
        for i in range(len(x_original)):
            if abs(x - x_original[i]) < min_diff:
                min_diff = abs(x - x_original[i])
                pos = i
        if x_original[pos] == x:  # they coincide
            yn.append(y_original[pos])

        else:
            if abs(x_original[pos]) < abs(x):
                # =============================================================================
                #                 # skip np.nan
                #                 nex = [x_original[pos+1],y_original[pos+1]]
                #                 i = 2
                #                 while np.isnan(nex).any() and (pos+i) < len(x_original):
                #                     nex = [x_original[pos+i],y_original[pos+i]]
                #                     i += 1
                # =============================================================================
                lower = [x_original[pos], y_original[pos]]
                upper = [x_original[pos + 1], y_original[pos + 1]]
            else:
                # =============================================================================
                #                 # skip np.nan
                #                 pre = [x_original[pos-1],y_original[pos-1]]
                #                 i = 2
                #                 while np.isnan(pre).any() and (pos-i) >= 0:
                #                     pre = [x_original[pos-i],y_original[pos-i]]
                #                     i += 1
                # =============================================================================
                lower = [x_original[pos - 1], y_original[pos - 1]]
                upper = [x_original[pos], y_original[pos]]

            # using linear interpolation:
            try:
                yvalue = lower[1] + (x - lower[0]) / (upper[0] - lower[0]) * \
                         (upper[1] - lower[1])
            except ZeroDivisionError:  # upper[0] != lower[0]
                yvalue = (lower[1] + upper[1]) / 2
            yn.append(yvalue)
    return yn


def store_curves(veh_file_paths, veh_paths_stored, store_path, veh_identities):
    store_path = store_path + '\\Curves data\\'
    create_dir(store_path)

    i = 0
    for veh_path in veh_file_paths:  # for each vehicle
        veh_identity = veh_identities[i]
        i += 1
        print('\n', veh_identity)

        if veh_path in veh_paths_stored:
            continue
        file_paths = get_test_data_paths(veh_path, 'processed.mat')

        csv_dir = os.path.join(store_path, veh_identity)
        create_dir(csv_dir)

        for test_number, file_path in file_paths.items():
            csv_path_raw = ('%s\\%s_%s_raw.csv'
                            % (csv_dir, veh_identity, test_number))
            csv_path_processed = ('%s\\%s_%s_processed.csv'
                                  % (csv_dir, veh_identity, test_number))

            df_raw = pd.DataFrame({})
            df_processed = pd.DataFrame({})
            if file_path:
                file_path = file_path[0]  # first item from the list
                df_raw, df_processed = get_curves_data(df_raw, df_processed,
                                       veh_identity, test_number, file_path)
            df_raw.to_csv(csv_path_raw)
            df_processed.to_csv(csv_path_processed)


if __name__ == '__main__':
    import time
    from get_files import get_VehFilePath_and_PdfPath

    database_paths = [r'D:\Desktop\database']

    veh_file_paths, general_data_paths = \
        get_VehFilePath_and_PdfPath(database_paths)
    start = time.time()

    store_path = r"D:\Desktop\KnC Store Path"

    store_curves(veh_file_paths, store_path)

    end = time.time()
    print('time: %f' % (end - start))
