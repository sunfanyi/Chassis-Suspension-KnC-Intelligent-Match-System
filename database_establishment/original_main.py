# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:06:28 2021

@author: Fanyi Sun
"""

import pandas as pd

from get_files import get_VehFilePath_and_PdfPath, get_test_data_paths
from data_extraction import get_all_data
from original_data_handling import arrange_data
from generate_test_data_df import generate_total_df_test
from generate_general_data_df import generate_total_df_general
from vehicle_identity import write_vehicle_identity
from excel_formating import generate_spreadsheet


database_paths = [r"D:\Desktop\database"]

# the folder containing the data for each vehicle is found based on the report location
vehicle_file_paths, general_data_paths = \
                        get_VehFilePath_and_PdfPath(database_paths)


# dataframe for general data
total_df_general, vehicle_identities, vehicle_names = \
                    generate_total_df_general(general_data_paths)
print(len(vehicle_identities))
write_vehicle_identity(vehicle_file_paths, vehicle_identities, vehicle_names)


# get all the test data
database = get_all_data(get_test_data_paths, vehicle_file_paths, 
                        vehicle_names)
useful_data = arrange_data(database)


# dataframe for test data
total_df_test = generate_total_df_test(useful_data)

# =============================================================================
# # set the columns as vehicle names according to total_df_vehicle and concat
# # vehicle_names = list(total_df_general.columns)
# # total_df_test.columns = vehicle_names
# =============================================================================

total_df = pd.concat([total_df_general, total_df_test])

total_df = total_df.set_index(['VEHICLES',''])

# store as xlsx for reviewing
store_path = '..\Summary Data_original.xlsx'
generate_spreadsheet(total_df, store_path)

# =============================================================================
# # store as csv for data processing
# store_path = '..\summary_data.csv'
# total_df.to_csv(store_path)
# =============================================================================


# to see the process, print on  generate_total_df_general()