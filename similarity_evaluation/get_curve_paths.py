# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:47:34 2021

@author: Fanyi Sun
"""

import os


def get_curve_paths(veh_identity, store_path):
    test_numbers = ['test 1', 'test 2', 'test 4', 
                    'test 7', 'test 8', 'test 10', 'strapped']
    curve_data_paths = {}
    for test_number in test_numbers:
        dir = store_path + '\\Curves Data\\' + veh_identity
        for file in os.listdir(dir):
            if ('%s_processed.csv' % test_number) in file:
                curve_path = os.path.join(dir,file)
                curve_data_paths[test_number] = curve_path
    return curve_data_paths