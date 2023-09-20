# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:47:56 2021

@author: Fanyi Sun
"""

class Weight():
    def __init__(self):
        self.wt_overall = {'test1': 0.0458,'test2': 0.0381,'test3': 0.0135,
                           'test4': 0.0718,'test5': 0.0324,'test6': 0.0139,
                           'test7': 0.1745,'test8': 0.2352,'test10': 0.3291,
                           'strapped': 0.0458}
        
        # Longitudinal Compliance (braking)(brake on, eng. on, ARB on)
        self.wt_test1 = {'Longitudinal Wheel Centre Compliance [mm/N]':
                             {'weight': 0.169, 'curve': 0.137, 'slope': 0.238,
                              'trend_change_left': 0.313, 
                              'trend_change_right': 0.313},
                         'Longitudinal Toe Compliance [deg/N]':
                             {'weight': 0.296, 'curve': 0.4, 'slope': 0.6},
                         'Longitudinal Camber Compliance [deg/N]': 
                             {'weight': 0.169, 'slope': 1},
                         'Longitudinal Spin Compliance [deg/N]': 
                             {'weight': 0.110, 'slope': 1},
                         'Longitudinal Tyre Stiffness [N/mm]': 
                             {'weight': 0.0425, 'slope': 1},
                         'Force Anti-Dive Angles [deg/N]':
                             {'weight': 0.07, 'slope': 0.3, 'y-intercept': 0.7},
                         'Anti-Dive Front/Anti-Lift Rear Curve Fits [N/N]':
                             {'weight': 0.1425, 'slope': 1}
                         }
            
        # Lateral Compliance at 0mm X offset (in phase)
        self.wt_test2 = {'Lateral Toe Compliance [deg/N]':
                             {'weight': 0.215, 'curve': 0.286, 'slope': 0.203,
                              'slope2000': 0.17, 'slope2000_diff': 0.341},
                         'Force Roll Centre Height [mm/N]':
                             {'weight': 0.215, 'curve': 0.144, 'slope': 0.223,
                              'y-intercept': 0.367, 
                              'max_RCH': 0.087, 'min_RCH': 0.179},
                         'Lateral Wheel Centre Compliance [mm/N]': 
                             {'weight': 0.127, 'slope': 1},
                         'Lateral Wheel Centre Stiffness projected on ground [N/mm]': 
                             {'weight': 0.104, 'slope': 1},
                         'Lateral Camber Compliance [deg/N]': 
                             {'weight': 0.171, 'slope': 1},
                         'Lateral Tyre Stiffness [N/mm]': 
                             {'weight': 0.04, 'slope': 1},
                         'Load Transfer (Roll Centre Curve Fits) [N/N]': 
                             {'weight': 0.127, 'slope': 1}
                         }
        
        # Lateral Compliance at 0mm X offset (anti-phase)
        self.wt_test3 = {'Lateral Wheel Centre Compliance [mm/N]': 
                             {'weight': 0.189, 'slope': 1},
                         'Lateral Wheel Centre Stiffness projected on ground [N/mm]': 
                             {'weight': 0.140, 'slope': 1},
                         'Lateral Toe Compliance [deg/N]': 
                             {'weight': 0.212, 'slope': 1},
                         'Lateral Camber Compliance [deg/N]': 
                             {'weight': 0.212, 'slope': 1},
                         'Lateral Tyre Stiffness [N/mm]': 
                             {'weight': 0.072, 'slope': 1},
                         'Force Roll Centre Height [mm/N]': 
                             {'weight': 0.176, 'slope': 0.35, 'y-intercept': 0.65}
                         }
        
        # Lateral Compliance at -30mm X offset (in phase)
        self.wt_test4 = {'Lateral Toe Compliance [deg/N]':
                             {'weight': 0.215, 'curve': 0.177, 'slope': 0.195,
                              'slope2000': 0.195, 'slope2000_diff': 0.433},
                         'Force Roll Centre Height [mm/N]':
                             {'weight': 0.215, 'curve': 0.196, 'slope': 0.231,
                              'y-intercept': 0.392, 
                              'max_RCH': 0.090, 'min_RCH': 0.090},
                         'Lateral Wheel Centre Compliance [mm/N]': 
                             {'weight': 0.127, 'slope': 1},
                         'Lateral Wheel Centre Stiffness projected on ground [N/mm]': 
                             {'weight': 0.104, 'slope': 1},
                         'Lateral Camber Compliance [deg/N]': 
                             {'weight': 0.171, 'slope': 1},
                         'Lateral Tyre Stiffness [N/mm]': 
                             {'weight': 0.040, 'slope': 1},
                         'Load Transfer (Roll Centre Curve Fits) [N/N]': 
                             {'weight': 0.127, 'slope': 1}
                         }
        
        # Aligning Torque (in phase)(brake on, eng. on, ARB on)
        self.wt_test5 = {'Toe Compliance [deg/Nm]': 
                             {'weight': 0.355, 'slope': 1},
                         'Camber Compliance [deg/Nm]': 
                             {'weight': 0.355, 'slope': 1},
                         'Tyre Aligning Stiffness [Nm/deg]': 
                             {'weight': 0.131, 'slope': 1},
                         'Steering Wheel Compliance [deg/Nm]': 
                             {'weight': 0.160, 'slope': 1}
                         }
            
        # Aligning Torque (anti-phase)(brake on, eng. on, ARB on)
        self.wt_test6 = {'Toe Compliance [deg/Nm]': 
                             {'weight': 0.332, 'slope': 1},
                         'Camber Compliance [deg/Nm]': 
                             {'weight': 0.332, 'slope': 1},
                         'Tyre Aligning Stiffness [Nm/deg]': 
                             {'weight': 0.197, 'slope': 1},
                         'Steering Wheel Compliance [deg/Nm]': 
                             {'weight': 0.139, 'slope': 1}
                         }
        
        # Steering Geometry Mid-Mid
        self.wt_test7 = {'Percentage Ackermann':
                             {'weight': 0.191, 'curve': 0.297, 'limit': 0.540,
                              'value20': 0.082, 'value-20': 0.082},
                         'Instantaneous Steering Ratio [/deg]':
                             {'weight': 0.058, 'curve': 0.260, 'y-intercept': 0.327,
                              'non-consistence': 0.413},
                         'Scrub Radius v Handwheel Steer [mm/deg]':
                             {'weight': 0.123, 'curve': 0.195, 'slope': 0.177,
                              'y-intercept': 0.242, 'ychange_max': 0.119,
                              'ychange_3/4': 0.112, 'ychange_1/2': 0.080, 
                              'ychange_1/4': 0.075},
                         'Mechanical Trail v Handwheel Steer [mm/deg]':
                             {'weight': 0.107, 'curve': 0.195, 'slope': 0.177,
                              'y-intercept': 0.242, 'ychange_max': 0.119,
                              'ychange_3/4': 0.112, 'ychange_1/2': 0.080, 
                              'ychange_1/4': 0.075},
                         'Camber Angle v Handwheel Steer [deg/deg]':
                             {'weight': 0.161, 'curve': 0.248, 'slope': 0.248,
                              'slope_grad0': 0.209, 'limit': 0.295},
                         'Steering Ratio [deg/deg]': 
                             {'weight': 0.052, 'slope': 1},
                         'Handwheel Torque v Handwheel Steer [Nm/deg]': 
                             {'weight': 0.038, 'slope': 1},
                         'Kingpin Inclination Angle v Handwheel Steer [deg/deg]':
                             {'weight': 0.084, 'slope': 0.4, 'y-intercept': 0.6},
                         'Kingpin Castor Angle v Handwheel Steer [deg/deg]':
                             {'weight': 0.078, 'slope': 0.4, 'y-intercept': 0.6},
                         'Kingpin Offset v Handwheel Steer [mm/deg]':
                             {'weight': 0.107, 'slope': 0.3, 'y-intercept': 0.7}
                         }
            
        # Roll test at Constant Axle Load (brake on, eng. on, ARB on)
        self.wt_test8 = {'Roll Steer v Roll Angle [deg/deg]':
                             {'weight': 0.147, 'slope': 0.196, 'curve_0to2': 0.133, 
                              'curve_2to4': 0.133, 'curve_above4': 0.044,
                              'slope_diff1': 0.185, 'slope_diff2': 0.185, 
                              'slope_diff4': 0.092},
                         'Roll Steer v Wheel to Body [deg/mm]':
                             {'weight': 0.147, 'slope': 0.234,
                              'curve_0to20': 0.164, 'curve_above20': 0.070, 
                              'slope50': 0.139, 'slope50_diff': 0.393},
                         'Roll Stiffnesses [Nm/deg]': 
                             {'weight': 0.056, 'slope': 1},
                         'Wheel Vertical Loads v Roll Angle [N/deg]': 
                             {'weight': 0.058, 'slope': 1},
                         'Wheel Vertical Rates [N/mm]': 
                             {'weight': 0.061, 'slope': 1},
                         'Roll Camber v Roll Angle [deg/deg]': 
                             {'weight': 0.138, 'slope': 1},
                         'Roll Camber v Wheel to Body [deg/mm]': 
                             {'weight': 0.138, 'slope': 1},
                         'Track Change [mm/deg]': 
                             {'weight': 0.025, 'slope': 1},
                         'Static Roll Weight Transfer Coefficient [/deg]': 
                             {'weight': 0.042, 'slope': 1},
                         'Kinematic Roll Centre Height [mm/deg]': 
                             {'weight': 0.084, 'slope': 1},
                         'Virtual Swing Arm Length [mm/deg]': 
                             {'weight': 0.037, 'slope': 1},
                         'Virtual Swing Arm Angle [deg/deg]': 
                             {'weight': 0.037, 'slope': 1},
                         'Track change variation [mm/mm]': 
                             {'weight': 0.030, 'slope': 1}
                         }


        # Vertical Bounce test (brake on, eng. on, ARB on)
        self.wt_test10 = {'Wheel Rates [N/mm]':
                              {'weight': 0.072, 'curve': 0.173, 'slope': 0.245,
                               'trend_change_left': 0.291, 
                               'trend_change_right': 0.291},
                          'Bump Steer [deg/mm]':
                              {'weight': 0.146, 'slope': 0.160, 'curve_0to20': 0.041,
                               'curve_20to50': 0.037, 'curve_50to70': 0.019, 
                               'curve_above70': 0.017, 'value20': 0.227,
                               'deviation-70': 0.160, 'slope50': 0.113, 
                               'slope50_diff': 0.227},
                          'Lateral Wheel Centre Displacement [mm/mm]':
                              {'weight': 0.087, 'slope': 0.327, 'curve_0to50': 0.156,
                               'curve_above50': 0.104, 'max_ychange': 0.413},
                          'Longitudinal Wheel Centre Displacement [mm/mm]':
                              {'weight': 0.067, 'slope': 0.260, 'curve_0to50':0.229,
                               'curve_above50': 0.098, 'max_ychange': 0.413},
                          'Track Change [mm/mm]':
                              {'weight': 0.040, 'slope': 0.327, 'curve_0to20': 0.065,
                               'curve_20to50': 0.065, 'curve_50to100': 0.130, 
                               'max_ychange': 0.413},
                          'Tyre Radial Rates [N/mm]': 
                             {'weight': 0.036, 'slope': 1},
                          'Ride Rates [N/mm]': 
                             {'weight': 0.043, 'slope': 1},
                          'Bump Camber [deg/mm]': 
                             {'weight': 0.121, 'slope': 1},
                          'Bump Spin [deg/mm]': 
                             {'weight': 0.084, 'slope': 1},
                          'Wheelbase Change [mm/mm]': 
                             {'weight': 0.039, 'slope': 1},
                          'Kinematic Roll Centre Height [mm/mm]':
                             {'weight': 0.159, 'slope': 0.3, 'y-intercept': 0.7},
                          'Virtual Swing Arm Length [mm/mm]':
                             {'weight': 0.045, 'slope': 0.4, 'y-intercept': 0.6},
                          'Virtual Swing Arm Angle [deg/mm]':
                             {'weight': 0.061, 'slope': 0.4, 'y-intercept': 0.6}
                          }
        
            
        # Longitudinal (acceleration)(brake off, eng. on, ARB on)
        self.wt_strapped = {'Longitudinal Wheel Centre Compliance [mm/N]':
                             {'weight': 0.184, 'curve': 0.137, 'slope': 0.238,
                              'trend_change_left': 0.313, 
                              'trend_change_right': 0.313},
                         'Longitudinal Toe Compliance [deg/N]':
                             {'weight': 0.330, 'curve': 0.4, 'slope': 0.6},
                         'Longitudinal Camber Compliance [deg/N]': 
                             {'weight': 0.184, 'slope': 1},
                         'Longitudinal Spin Compliance [deg/N]': 
                             {'weight': 0.1115, 'slope': 1},
                         'Longitudinal Tyre Stiffness [N/mm]': 
                             {'weight': 0.0412, 'slope': 1},
                         'Anti-Lift Front/Anti-Squat Rear Curve Fits [N/N]': 
                             {'weight': 0.15, 'slope': 1}
                         }
        
    
