# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:47:51 2021

@author: Fanyi Sun
"""

import numpy as np

from get_files import get_test_data_paths


def get_all_data(veh_file_paths, veh_identities):
    database = {
        'test 1': [], 'test 2': [], 'test 3': [], 'test 4': [],
        'test 5': [], 'test 6': [], 'test 7': [], 'test 8': [],
        'test 10': [], 'strapped': []
    }

    for i in range(len(veh_identities)):
        veh_identity = veh_identities[i]
        veh_name = veh_identity.rpartition('#')[0]
        file_paths = get_test_data_paths(veh_file_paths[i], 'summary.txt')
        # =============================================================================
        #     # to see if the file path is correct:
        #         for key in file_paths.keys():
        #             print(key)
        #             for a in file_paths[key]:
        #                 print(a)
        #         print('\n')
        # =============================================================================

        for test_number in database.keys():
            if file_paths[test_number]:  # if it contains the specific test data
                # save as a dict with parameters as keys and numbers as values
                info_dict = get_info(file_paths[test_number][0], veh_name)
                database[test_number].append(info_dict)
            else:
                database[test_number].append({'vehicle name': veh_name})

    return database


def get_info(file_path, veh_name):
    with open(file_path, 'r') as file:
        info = file.readlines()
    for i in range(len(info)):
        if 'Calculated Parameters' in info[i]:
            # remove all the data for Calculated Parameters
            info = info[0:i - 1]
            break

    # seperate the data on the LHS and RHS of the txt files
    info = separate_left_right(info)[2:]  # remove first two lines
    info_dict = store_as_dict(info, veh_name)
    return info_dict


def separate_left_right(info):
    # point of separation (see the ORIGINAL format of the files):
    separation = len(info[0])
    left = []
    right = []
    for line in info:
        line = line.strip('\n')
        left.append(line[:separation])
        right.append(line[separation:])

    return (left + right)


def store_as_dict(info, veh_name):
    """
    convert the info as the desired format:
        a dict with parameters as keys and numbers as values
    """
    info_dict = {'vehicle name': veh_name}
    for line in info:
        if line.strip() != '':  # if the line is not empty
            if line.strip() != 'None':
                try:
                    # split the data, then convert strings into float
                    number = [float(x) for x in line.split()]
                except ValueError:
                    '''
                    If it can't be converted into float, this line is a 
                    parameter. Remove ':' and blank spaces and store it.
                    '''
                    para = line.replace(':', '').strip()
                    info_dict[para] = []
                else:
                    info_dict[para].append(number)
            else:
                info_dict[para].append(np.nan)
    return info_dict
