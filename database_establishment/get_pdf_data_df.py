# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:56:27 2021

@author: Fanyi Sun
"""

import re
import pandas as pd
import numpy as np
import pdfplumber

from data_handling import insert_average


def get_total_df_pdf(pdf_data_paths):
    parameters, sub_index = get_vehicle_para()
    df_para = pd.DataFrame({'VEHICLES': parameters,
                            '': sub_index})
    df_pdf = []
    # store the vehicle name and VehID for each vehicle for later stage
    veh_identities = []  # contain name and ID
    i = 0
    for file_path in pdf_data_paths:
        i += 1
        with pdfplumber.open(file_path) as p:
            # get the vehicle name from the first line in the first table
            first_table = p.pages[0].extract_text()
            veh_name = '%d_%s' % (i, first_table.split('\n')[0])
            VehID = 'ID not found'
            data = [np.nan] * len(parameters)
            pages_info = ''
            pg = 0
            while True:
                pg += 1
                '''
                skip the first page because the vehicle name here
                sometimes contains parameter name, eg, Model and
                Tesla Model-3, which is misleading while searching
                '''
                try:
                    table = p.pages[pg].extract_text()
                except IndexError:  # no curve page found
                    setup = []
                    break
                if table:  # some page doesn't contain any information
                    pages_info += table + '\n'
                    if 'Vehicle Number' in table:
                        '''
                        find the setup number from the first page containing 
                        figure, so that the setup number can be used to find 
                        the corresponding setup information
                        '''
                        setup = re.findall('Setup \d+', table)
                        break
                    elif pg > 50:
                        break

            pages_info = pages_info.split('\n')
            # part 1 contains the info that is not setup info
            part1 = pages_info[:pages_info.index('SETUP 1 INFORMATION')]
            # part 2 contains setup info only
            if setup:
                setup = setup[0]
                next_setup = setup.split(' ')[0] + ' ' + \
                             str(int(setup.split(' ')[1]) + 1)
                setup = setup.upper() + ' INFORMATION'
                next_setup = next_setup.upper() + ' INFORMATION'

                try:
                    part2 = pages_info[pages_info.index(setup):
                                       pages_info.index(next_setup)]
                except ValueError:
                    pass
            else:
                part2 = []

            pages_info = part1 + part2
        data, VehID = get_pdf_data(data, pages_info, parameters, VehID)
        VehID = VehID.replace('#', '_')
        veh_identity = '%s#%s' % (veh_name, VehID)
        veh_identity = veh_identity.replace('/', '_')
        veh_identity = veh_identity.replace('\\', '_')
        veh_name = veh_name.replace('/', '_')
        veh_name = veh_name.replace('\\', '_')
        print(veh_identity)
        veh_identities.append(veh_identity)
        df_pdf.append(pd.DataFrame({veh_name: data}))

    # add information for a new vehicle by column
    df_pdf_data = pd.concat(df_pdf, axis=1)
    # set the first column as parameters and second column as wheels
    df_pdf_data = pd.concat([df_para, df_pdf_data], axis=1)

    return df_pdf_data, veh_identities


def get_vehicle_para():
    parameters = ['GENERAL', 'VehID', 'Year', 'Mileage', 'Manufacturer',
                  'Model', 'Class', 'WEIGHTS AND DIMENSIONS', 'GVWR [kg]',
                  'FGAWR [kg]', 'RGAWR [kg]', 'WheelBase [mm]'] \
                 + ['Track [mm]'] * 2 \
                 + ['Rolling radius [mm]'] * 2 \
                 + ['Kerb weight [kg]'] * 6 \
                 + ['Wing height [mm]'] * 6 \
                 + ['VEHICLE AND RIG CONFIGURATION', 'Drive'] \
                 + ['Susp layout'] * 2 \
                 + ['ALIGNMENT DATA'] \
                 + ['Kerb toe [deg]'] * 6 \
                 + ['Kerb camber [deg]'] * 6 \
                 + ['Kerb castor [deg]'] * 6 \
                 + ['Kingpin incl. [deg]'] * 6 \
                 + ['Offset [mm]'] * 6 \
                 + ['TYRES AND RIMS'] \
                 + ['Tyre size'] * 2 \
                 + ['Tyre type'] * 2 \
                 + ['Infl. pressure [kPa]'] * 2 \
                 + ['Wheel size'] * 2 \
                 + ['Wheel type'] * 2 \
                 + ['USER LABELS', 'Engine', 'SETUP INFORMATION'] \
                 + ['Toe [deg]'] * 6 \
                 + ['Camber [deg]'] * 6 \
                 + ['Static forces [N]'] * 6

    sub_index = [''] * len(parameters)
    for i in set(parameters):
        if parameters.count(i) == 2:
            pos = parameters.index(i)
            sub_index[pos:pos + 2] = ['Front', 'Rear']
        elif parameters.count(i) == 6:
            pos = parameters.index(i)
            sub_index[pos:pos + 6] = ['FL', 'FR', 'F_avg', 'RL', 'RR', 'R_avg']
    return parameters, sub_index


def get_pdf_data(data, pages_info, parameters, VehID):
    for line in pages_info:
        for i, para in enumerate(parameters):
            # remove the unit if exist during searching
            try:
                para = para.split(' [')[0]
            except:
                pass
            if para in line:
                pos = i
                data, VehID = fill_data(data, pos, line, para, VehID)
                break
    for i in range(len(data)):
        try:  # store as float if possible
            data[i] = float(data[i])
        except ValueError:
            pass
    return data, VehID


def fill_data(data, pos, line, para, VehID):
    """
    This function first find how many values each parameter needs, 
    and then store them into the corresponding position
    """
    line = line.replace(para, '', 1).strip()  # it could be empty if no data
    if line:
        # use different methods for different paras
        if para == 'VehID' or para == 'Drive' or para == 'Engine':
            if para == 'VehID':  # record the VehID for later stage
                VehID = line
            # record all the information
            data[pos] = line
        elif para == 'Susp layout' or para == 'Tyre size' or \
                para == 'Tyre type' or para == 'Wheel type' or \
                para == 'Wheel size':
            if len(line.split()) == 2:
                # if only one blank space so that it can be splitted easily:
                data[pos] = line.split()[0]
                data[pos + 1] = line.split()[0]
            else:
                # split the data in the middle and assign for front and rear
                middle = int((len(line) + 1) / 2)
                data[pos] = line[:middle]
                data[pos + 1] = line[middle:]
        else:
            if para == 'Offset':
                try:  # sometimes it's called Offset (ET) in the report
                    line = line.replace('(ET)', '').strip()
                except:
                    pass
            line = line.split()
            if len(line) == 2:  # one for value, one for unit
                # record the value only
                data[pos] = line[0]
            elif len(line) == 4:  # 2 pairs, for front and rear
                data[pos] = line[0]
                data[pos + 1] = line[2]
            elif len(line) == 8:  # 4 pairs, for 4 wheels
                if para == 'Offset':
                    try:  # sometimes it's called Offset (ET) in the report
                        line = line.replace('(ET)', '').strip()
                    except:
                        pass
                values = [line[0], line[2], line[4], line[6]]
                values = [float(x) for x in values]
                values = insert_average(values)
                data[pos:pos + 6] = values
            else:  # usual case, one single value
                data[pos] = line[0]
    return data, VehID


if __name__ == '__main__':
    store_path = r"D:\Desktop\KnC Store Path"
    summary_path = '%s\\Vehicle Summary.txt' % store_path
    with open(summary_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        pdf_paths_stored = [a.split('\t')[-1].strip('\n') for a in lines]
    total_df_pdf, veh_identities = get_total_df_pdf(pdf_paths_stored,
                                                    store_path)
    # get_total_df_pdf(pdf_paths_stored, store_path)
    print(total_df_pdf)
