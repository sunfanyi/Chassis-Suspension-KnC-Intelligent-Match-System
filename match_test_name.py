# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 12:02:42 2021

@author: Fanyi Sun
"""


def get_full_test_name(test_number):
    if test_number == 'test 1' or test_number == 'test1':
        test_name = 'Test 1_Longitudinal Compliance (braking)(brake on, eng. on, ARB on)'
    elif test_number == 'test 2' or test_number == 'test2':
        test_name = 'Test 2_Lateral Compliance at 0mm X offset (in phase)'
    elif test_number == 'test 3' or test_number == 'test3':
        test_name = 'Test 3_Lateral Compliance at 0mm X offset (anti-phase)'
    elif test_number == 'test 4' or test_number == 'test4':
        test_name = 'Test 4_Lateral Compliance at -30mm X offset (in phase)'
    elif test_number == 'test 5' or test_number == 'test5':
        test_name = 'Test 5_Aligning Torque (in phase)(brake on, eng. on, ARB on)'
    elif test_number == 'test 6' or test_number == 'test6':
        test_name = 'Test 6_Aligning Torque (anti-phase)(brake on, eng. on, ARB on)'
    elif test_number == 'test 7' or test_number == 'test7':
        test_name = 'Test 7_Steering Geometry Mid-Mid'
    elif test_number == 'test 8' or test_number == 'test8':
        test_name = 'Test 8_Roll test at Constant Axle Load (brake on, eng. on, ARB on)'
    elif test_number == 'test 10' or test_number == 'test10':
        test_name = 'Test 10_Vertical Bounce test (brake on, eng. on, ARB on)'
    elif test_number.upper() == 'Strapped'.upper():
        test_name = 'Test 1_Longitudinal (acceleration)(brake off, eng. on, ARB on)'
    return test_name

        
def get_simp_test_name(test_number):
    if test_number == 'test 1' or test_number == 'test1':
        test_name = 'Long. braking'
    elif test_number == 'test 2' or test_number == 'test2':
        test_name = 'Lat. 0_in'
    elif test_number == 'test 3' or test_number == 'test3':
        test_name = 'Lat. 0_anti'
    elif test_number == 'test 4' or test_number == 'test4':
        test_name = 'Lat. -30_in'
    elif test_number == 'test 5' or test_number == 'test5':
        test_name = 'Alig. T_in'
    elif test_number == 'test 6' or test_number == 'test6':
        test_name = 'Alig. T_anti'
    elif test_number == 'test 7' or test_number == 'test7':
        test_name = 'Steering'
    elif test_number == 'test 8' or test_number == 'test8':
        test_name = 'Roll'
    elif test_number == 'test 10' or test_number == 'test10':
        test_name = 'Vertical'
    elif test_number.upper() == 'Strapped'.upper():
        test_name = 'Long.acc'
    return test_name


# test1 = 'Test 1_Longitudinal Compliance (braking)(brake on, eng. on, ARB on)'
# test2 = 'Test 2_Lateral Compliance at 0mm X offset (in phase)'
# test3 = 'Test 3_Lateral Compliance at 0mm X offset (anti-phase)'
# test4 = 'Test 4_Lateral Compliance at -30mm X offset (in phase)'
# test5 = 'Test 5_Aligning Torque (in phase)(brake on, eng. on, ARB on)'
# test6 = 'Test 6_Aligning Torque (anti-phase)(brake on, eng. on, ARB on)'
# test7 = 'Test 7_Steering Geometry Mid-Mid                               '
# test8 = 'Test 8_Roll test at Constant Axle Load (brake on, eng. on, ARB on)'
# test10 = 'Test 10_Vertical Bounce test (brake on, eng. on, ARB on)'
# strapped = 'Test 1_Longitudinal (acceleration)(brake off, eng. on, ARB on)'
