# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:27:29 2021

@author: Fanyi Sun
"""

class FrontWeight():
    def __init__(self):
        self.front = 0.5
        
        self.general = 0.0465
        self.longitudinal = 0.1376
        self.lateral = 0.1376
        self.vertical = 0.267
        self.steer = 0.1444
        self.roll = 0.2670
        
        self.toe_in = 0.6
        self.static_camber = 0.4
        
        self.drive_toe_in = 0.3560
        self.anti_lift = 0.1088
        self.brake_toe_in = 0.3486
        self.caster_comp = 0.0778
        self.anti_dive = 0.1088

        self.camber_comp = 0.0767
        self.lat_stif = 0.1549
        self.lat_F = 0.3374
        self.lat_F_delta = 0.4311
        
        self.bump_camber = 0.2
        self.bump_understeer = 0.6
        self.wheel_travel = 0.2

        # self.caster = 0.1113
        # self.kpi = 0.1113
        # self.kpo = 0.2101
        # self.scrub_r = 0.2413
        # self.ackermann = 0.3260
        self.caster = 0
        self.kpi = 0
        self.kpo = 0
        self.scrub_r = 0
        self.ackermann = 1

        self.static_rch = 0.5
        self.roll_bump = 0.5
        
        
class RearWeight():
    def __init__(self):
        self.rear = 0.5
        
        self.general = 0.0577
        self.longitudinal = 0.1609
        self.lateral = 0.1609
        self.vertical = 0.3103
        self.roll = 0.3103
        
        self.toe_in = 0.6
        self.static_camber = 0.4
        
        self.drive_toe_in = 0.3560
        self.anti_squat = 0.1088
        self.brake_toe_in = 0.3486
        self.caster_comp = 0.0778
        self.anti_lift = 0.1088
        
        self.camber_comp = 0.0767
        self.lat_stif = 0.1549
        self.lat_F = 0.3374
        self.lat_F_delta = 0.4311
        
        self.bump_camber = 0.4
        self.bump_understeer = 0.6

        self.static_rch = 0.2
        self.roll_bump = 0.4
        self.static_rch_diff = 0.4 