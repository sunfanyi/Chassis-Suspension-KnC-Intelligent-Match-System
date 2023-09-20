# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:42:50 2021

@author: Fanyi Sun
"""

import os

path = r'D:\Desktop\KnC benchmark\Y283_S60\Y283_BSTT201_KC150311.veh\Std. K&C Tests Engine On Utan stag'

old = ['test 1', 'test 2', 'test 3', 'test 4', 'test 5',
       'test 6', 'test 7', 'test 8', 'test 9', 'test 10']
new = ['test 9_Vertical BouncePitch test (brake on, eng. on, ARB on)',
       'test 10_Vertical Bounce test (brake on, eng. on, ARB on)',
       'test 8_Roll test at Constant Axle Load (brake on, eng. on, ARB on)',
       'test 1_Longitudinal Compliance (braking)(brake on, eng. on, ARB on)',
       'test 2_Lateral Compliance at 0mm X offset (in phase)',
       'test 3_Lateral Compliance at 0mm X offset (anti phase)',
       'test 4_Lateral Compliance at -30mm X offset (in phase)',
       'test 5_Aligning Torque (in phase)(brake on, eng. on, ARB on)',
       'test 6_Aligning Torque (anti-phase)(brake on, eng. on, ARB on)',
       'test 7_Steering Geometry Mid-Mid']

for i in range(10):
    olddir = os.path.join(path, old[i])
    newdir = os.path.join(path, new[i])
    os.rename(olddir, newdir)
