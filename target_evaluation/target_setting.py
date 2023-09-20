# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 23:37:46 2021

@author: Fanyi Sun
"""


class FrontTarget():
    def __init__(self):
        """
        When the type is interval, 'value' represents the interval where the 
        reliability of this parameter is 100%. 'limit' represents the 
        unacceptable range where the reliability is 0% if the value falls 
        outside of the interval. If the value lie between value[0] and limit[0]
        or value[1] and limit[1], the reliability has a linear characteristic
        with two known boundary conditions. 'other' represents any other 
        characteristic of the curve, eg, [80, 0.7, 150, 0.7] means the 
        reliability is 70% when the value is 80 & 150.
        
        When the type is max. the first item in 'value' represents the critical
        value and the second value is the reliability at this value. The 
        reliability is higher if the value < the critical value and lower 
        if <. 'limit' represents two boundary conditions. The first item in 
        'limit' represents the value at 100% reliability and the second item
        is the value at 0% reliability. (Same if the type is min.)
        """
        self.static_camber = {'type': 'interval',
                              'value': [-1, -0.7], 'limit': [-2, 0]}
        
        self.bump_camber = {'type': 'interval', 
                            'value': [-20, -18], 'limit': [-40, 0]}
        
        self.toe_in = {'type': 'interval', 
                       'value': [0, 0.4], 'limit': [-0.4, 2]}
        
        self.bump_understeer = {'type': 'interval', 
                                'value': [5, 8], 'limit': [0, 20]}
        
        self.caster = {'type': 'interval', 
                       'value': [6, 7], 'limit': [4, 10.5]}
        
        self.kpi = {'type': 'interval', 
                    'value': [3, 8], 'limit': [1, 12]}
        
        self.kpo = {'type': 'max', 'value': [56, 0.8], 
                    'limit': [40, 56 * 1.1]}
        
        self.scrub_r = {'type': 'interval', 
                        'value': [-5, 15], 'limit': [-25, 35]}
        
        self.static_rch = {'type': 'interval',
                           'value': [80, 95], 'limit': [30, 150]}
        
        self.wheel_travel = {'type': 'min', 'value': [80, 0.9], 
                             'limit': [48, 80 * 1.1]}
        
        self.roll_bump = {'type': 'interval',
                          'value': [-1, 1], 'limit': [-2, 2]}
        
        self.ackermann = {'type': 'interval',
                          'value': [55, 70], 'limit': [30, 100]}
        
        self.camber_comp = {'type': 'max', 'value': [0.15, 0.8], 
                            'limit': [0.1, 0.3]}
        
        self.lat_stif = {'type': 'min', 'value': [2500, 0.8], 
                         'limit': [2000, 3000]}
        
        self.lat_F = {'type': 'min', 'value': [0.065, 0.9], 
                      'limit': [0.065 * 0.5, 0.065 * 1.25]}

        self.lat_F_delta = {'type': 'interval',
                            'value': [0.05, 0.09], 'limit': [0, 0.27]}
        
        self.drive_toe_in = {'type': 'interval',
                             'value': [-0.1, 0], 'limit': [-0.3, 0.2]}
        
        self.anti_lift = {'type': 'interval',
                          'value': [1, 2], 'limit': [0, 5]}
        
        self.brake_toe_in = {'type': 'interval',
                             'value': [-0.04, -0.01], 'limit': [-0.1, 0]}
        
        self.caster_comp = {'type': 'min', 'value': [-1, 0.9], 
                            'limit': [-2, -0.8]}

        self.anti_dive = {'type': 'interval',
                          'value': [10, 12], 'limit': [0, 30]}
    
    # This function is not used, a similar one is copied to myFormTargetItem.py
    def updata_interval(self, para):
        value = eval("self.%s['value']" % para)
        if para == 'static_camber':
            self.static_camber['limit'] = [value[0] * 2, 0]
            
        elif para == 'bump_camber':
            self.bump_camber['limit'] = [value[0] * 2, 0]
            
        elif para == 'toe_in':
            self.toe_in['limit'][0] = value[0] - (value[1] - value[0])
            self.toe_in['limit'][1] = value[1] * 5
            
        elif para == 'bump_understeer':
            self.bump_understeer['limit'] = [0, value[1] * 2.5]
            
        elif para == 'caster':
            self.caster['limit'] = [value[0] * 2/3, value[1] * 3/2]
            
        elif para == 'kpi':
            self.kpi['limit'] = [value[0] * 1/3, value[1] * 3/2]
            
        elif para == 'scrub_r':
            self.scrub_r['limit'][0] = value[0] - (value[1] - value[0])
            self.scrub_r['limit'][1] = value[1] + (value[1] - value[0])
            
        elif para == 'static_rch':
            return 
        
        elif para == 'roll_bump':
            self.roll_bump['limit'][0] = value[0] - 0.5 * (value[1] - value[0])
            self.roll_bump['limit'][1] = value[1] + 0.5 * (value[1] - value[0])
        
        elif para == 'ackermann':
            return 
        
        elif para == 'lat_F_delta':
            self.lat_F_delta['limit'] = [0, value[1] * 3]
        
        elif para == 'drive_toe_in':
            self.drive_toe_in['limit'][0] = value[0] * 3
            self.drive_toe_in['limit'][1] = value[1] + 2 * (value[1] - value[0])
        
        elif para == 'anti_lift':
            self.anti_lift['limit'] = [0, value[1] * 2.5]
            
        elif para == 'brake_toe_in':
            self.brake_toe_in['limit'] = [value[0] * 2.5, 0]
            
        elif para == 'anti_dive':
            self.anti_dive['limit'] = [0, value[1] * 2.5]
            
            
    # This function is not used, a similar one is copied to myFormTargetItem.py
    def undate_limit(self, para):
        value = eval("self.%s['value']" % para)[0]
        if para == 'kpo':
            self.kpo['limit'] = [value * 2/3, value * 1.1]
            
        elif para == 'wheel_travel':
            self.wheel_travel['limit'] = [value * 0.6, value * 1.1]
            
        elif para == 'camber_comp':
            self.camber_comp['limit'] = [value * 2/3, value * 2]
            
        elif para == 'lat_stif':
            self.lat_stif['limit'] = [value * 0.8, value * 1.2]
            
        elif para == 'lat_F':
            self.lat_stif['limit'] = [value * 0.5, value * 1.25]
            
        elif para == 'caster_comp':
            self.caster_comp['limit'] = [value * 2, value * 0.8]
            
            
            
class RearTarget():
    def __init__(self):
        self.static_camber = {'type': 'interval',
                              'value': [-1.2, -0.8], 'limit': [-2.4, 0]}
        
        self.bump_camber = {'type': 'interval', 
                            'value': [-25, -22], 'limit': [-50, 0]}
        
        self.toe_in = {'type': 'interval', 
                       'value': [0, 0.4], 'limit': [-0.4, 2]}
        
        self.bump_understeer = {'type': 'interval', 
                                'value': [1.3, 2.2], 'limit': [0, 2.2 * 2.5]}
        
        self.static_rch = {'type': 'interval',
                           'value': [100, 120], 'limit': [60, 280],
                           'other' : [80, 0.7, 150, 0.7]}
        
        self.static_rch_diff = {'type': 'interval',
                                'value': [10, 30], 'limit': [5, 80]}
        
        self.roll_bump = {'type': 'interval',
                          'value': [0, 0.9], 'limit': [-0.45, 1.35]}
        
        self.camber_comp = {'type': 'max', 'value': [0.15, 0.8], 
                            'limit': [0.1, 0.3]}
        
        self.lat_stif = {'type': 'min', 'value': [2500, 0.8], 
                         'limit': [2000, 3000]}
        
        self.lat_F = {'type': 'interval',
                      'value': [0.005, 0.025], 'limit': [0, 0.075]}

        self.lat_F_delta = {'type': 'interval',
                            'value': [0.01, 0.03], 'limit': [0, 0.05]}
        
        self.drive_toe_in = {'type': 'interval',
                             'value': [-0.05, 0.05], 'limit': [-0.2, 0.2]}
        
        self.anti_squat = {'type': 'interval',
                           'value': [10, 12], 'limit': [0, 30]}
        
        self.brake_toe_in = {'type': 'interval',
                             'value': [0.05, 0.125], 'limit': [0, 0.3]}
        
        self.caster_comp = {'type': 'min', 'value': [-0.8, 0.9], 
                            'limit': [-2, -0.6]}

        self.anti_lift = {'type': 'max', 'value': [37, 0.8], 
                          'limit': [11.1, 48.1]}

    
    # This function is not used, a similar one is copied to myFormTargetItem.py
    def updata_interval(self, para):
        value = eval("self.%s['value']" % para)
        if para == 'static_camber':
            self.static_camber['limit'] = [value[0] * 2, 0]
            
        elif para == 'bump_camber':
            self.bump_camber['limit'] = [value[0] * 2, 0]
            
        elif para == 'toe_in':
            self.toe_in['limit'][0] = value[0] - (value[1] - value[0])
            self.toe_in['limit'][1] = value[1] * 5
            
        elif para == 'bump_understeer':
            self.bump_understeer['limit'] = [0, value[1] * 2.5]
            
        elif para == 'static_rch' or para == 'static_rch_diff':
            return 
        
        elif para == 'roll_bump':
            self.roll_bump['limit'][0] = value[0] - 0.5 * (value[1] - value[0])
            self.roll_bump['limit'][1] = value[1] + 0.5 * (value[1] - value[0])
        
        elif para == 'lat_F':
            self.lat_F_delta['limit'] = [0, value[1] * 3]
        
        elif para == 'lat_F_delta':
            self.lat_F_delta['limit'][0] = 0
            self.lat_F_delta['limit'][1] = value[1] + (value[1] - value[0])
        
        elif para == 'drive_toe_in':
            self.drive_toe_in['limit'][0] = value[0] - 2 * (value[1] - value[0])
            self.drive_toe_in['limit'][1] = value[1] + 2 * (value[1] - value[0])
        
        elif para == 'anti_squat':
            self.anti_squat['limit'] = [0, value[1] * 2.5]
            
        elif para == 'brake_toe_in':
            self.brake_toe_in['limit'] = [0, value[1] * 2.4]
            
         
    # This function is not used, a similar one is copied to myFormTargetItem.py
    def undate_limit(self, para):
        value = eval("self.%s['value']" % para)[0]
        if para == 'camber_comp':
            self.camber_comp['limit'] = [value * 2/3, value * 2]
            
        elif para == 'lat_stif':
            self.lat_stif['limit'] = [value * 0.8, value * 1.2]
            
        elif para == 'caster_comp':
            self.caster_comp['limit'] = [value * 2.5, value * 3/4]
            
        elif para == 'anti_lift':
            self.anti_lift['limit'] = [value * 0.3, value * 1.3]
