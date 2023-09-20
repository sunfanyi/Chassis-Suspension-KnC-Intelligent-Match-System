# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 09:45:13 2021

@author: Fanyi Sun
"""

import os


def get_VehFilePath_and_PdfPath(database_paths):
    # each path contains all data for the corresponding vehicle
    veh_file_paths = []
    # pdf files for general data
    general_data_paths = []

    for database_path in database_paths:
        found = False
        for dir in os.listdir(database_path):
            if '.pdf' in dir:
                pdf = os.path.join(database_path, dir)
                general_data_paths.append(pdf)
                veh_file_paths.append(database_path)
                found = True
                break
        if found:
            continue
        for dir in os.listdir(database_path):
            found = False
            paths = [os.path.join(database_path, dir)]
            isdir = [os.path.isdir(i) for i in paths]
            if not any(isdir):
                continue
            '''
            Searching layer by layer for all sub_directory, instead of
            using a simple while loop and os.walk, which would go directly to 
            the deepest layer of the first sub_directory and get the wrong pdf.
            '''
            while not found:
                next_paths = []
                for path in paths:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            if '.pdf' in file:
                                pdf = os.path.join(root, file)
                                general_data_paths.append(pdf)
                                veh_file_paths.append(root)
                                found = True
                        break  # stop walking deeper
                    if not found:
                        # if not in this directory, then go deeper
                        for dir in os.listdir(path):
                            if os.path.isdir(os.path.join(path, dir)):
                                next_paths.append(os.path.join(path, dir))
                try:
                    paths = next_paths
                except:
                    pass
    return veh_file_paths, general_data_paths


def get_test_data_paths(path, file_type):
    # test_type = .txt or .mat files for test data
    # get the file paths corresponding to the test number with orders
    all_files = get_all_files(path, file_type)
    if file_type == 'summary.txt':
        test_data_paths = {'test 1': [], 'test 2': [], 'test 3': [],
                           'test 4': [],
                           'test 5': [], 'test 6': [], 'test 7': [],
                           'test 8': [],
                           'test 10': [], 'strapped': []
                           }
    elif file_type == 'processed.mat':
        # don't need the curves for test 3, 5 and 6
        test_data_paths = {'test 1': [], 'test 2': [], 'test 4': [],
                           'test 7': [], 'test 8': [],
                           'test 10': [], 'strapped': []
                           }
    for test_number in test_data_paths.keys():
        match_test_number(test_number, all_files, test_data_paths)
    return test_data_paths


def get_all_files(path, file_type):
    # get all the files containing useful information without any order
    all_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            # print(file_path)
            if file_type in file_path and 'test 9' not in file_path:
                all_files.append(file_path)
    return all_files


def match_test_number(test_number, all_files, test_data_paths):
    # store the file paths correspondingly into test_file_paths
    if test_number == 'test 1':
        for file in all_files:
            if test_number in file and 'test 10' not in file \
                    and 'test 11' not in file:
                if 'ENGINE ON' in file.upper() or 'ENGIN ON' in file.upper():
                    # test for strapped wheels is not needed here
                    test_data_paths[test_number].append(file)
    elif test_number == 'strapped':
        for file in all_files:
            if 'STRAPPED'.upper() in file.upper() or 'STRAPT' in file.upper():
                test_data_paths[test_number].append(file)
    else:  # for test 2 to 10
        for file in all_files:
            if test_number in file:
                if 'ENGINE ON' in file.upper() or 'ENGIN ON' in file.upper():
                    test_data_paths[test_number].append(file)


if __name__ == '__main__':
    path = r"D:\Desktop\txt2excel\database"
    file_paths = get_test_data_paths(path, 'summary.txt')
    # for key in file_paths.keys():
    #     print(key)
    #     for a in file_paths[key]:
    #         print(a)

