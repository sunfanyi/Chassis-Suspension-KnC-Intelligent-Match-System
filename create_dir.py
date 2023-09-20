# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:17:48 2021

@author: Fanyi Sun
"""

import os

def create_dir(path, create_intermediate=False):
    path = path.rstrip('\\')
    
    isExist = os.path.exists(path)
    if not isExist:
        if not create_intermediate:
            os.mkdir(path)
        else:
            os.makedirs(path) 
        
    
