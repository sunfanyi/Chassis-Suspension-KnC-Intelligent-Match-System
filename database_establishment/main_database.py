# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:06:28 2021

@author: Fanyi Sun
"""

import pandas as pd

from get_files import get_VehFilePath_and_PdfPath
from data_extraction import get_all_data
from data_handling import arrange_data
from get_test_data_df import get_total_df_test
from get_pdf_data_df import get_total_df_pdf
from vehicle_identity import write_veh_identity
from excel_formating import generate_spreadsheet

from curves_data import store_curves


def main_database(database_paths, store_path):
    # find vehicles that are already stored
    summary_path = '%s\\Vehicle Summary.txt' % store_path
    try: 
        with open(summary_path,'r',encoding='utf-8') as f:
            lines = f.readlines()
            veh_paths_stored = [a.split('\t')[1] for a in lines]
            pdf_paths_stored = [a.split('\t')[-1].strip('\n') for a in lines]
            # veh_paths_stored = []
            # pdf_paths_stored = []
    except FileNotFoundError:
        veh_paths_stored = []
        pdf_paths_stored = []
        
    # for summary data:
    # the folder containing the data for each vehicle is found based on the report location
    veh_file_paths, pdf_data_paths = \
                            get_VehFilePath_and_PdfPath(database_paths)
                    
    total_veh_paths = veh_paths_stored + [path for path in veh_file_paths 
                        if path not in veh_paths_stored]
    total_pdf_paths = pdf_paths_stored + [path for path in pdf_data_paths 
                        if path not in pdf_paths_stored]
    # dataframe for pdf data
    total_df_pdf, veh_identities = get_total_df_pdf(total_pdf_paths)
    write_veh_identity(total_veh_paths, total_pdf_paths,
                        veh_identities, store_path)
    # get all the test data
    database = get_all_data(total_veh_paths, veh_identities)
    useful_data = arrange_data(database)
    
    # dataframe for test data
    total_df_test = get_total_df_test(useful_data)
    total_df = pd.concat([total_df_pdf, total_df_test])
    total_df = total_df.set_index(['VEHICLES',''])
    
    # store as xlsx for reviewing
    xlsx_store_path = store_path + '\\Summary Data.xlsx'
    generate_spreadsheet(total_df, xlsx_store_path)
    
    # store as csv for data processing
    csv_store_path = store_path + '\\summary_data.csv'
    total_df.to_csv(csv_store_path)
    
    # to see the process, print on  generate_total_df_general()
    # for curves data:
    store_curves(total_veh_paths, veh_paths_stored, store_path, veh_identities)
    return veh_identities, total_veh_paths
    

if __name__ == '__main__':
    from pyinstrument import Profiler
    
    profiler = Profiler()
    profiler.start()
    
    database_paths = [r"D:\Desktop\database"]
    store_path = r"D:\Desktop\KnC Store Path"
    veh_identities, total_veh_paths = main_database(database_paths, store_path)
    
    profiler.stop()
    # profiler.print()