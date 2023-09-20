# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:57:03 2021

@author: Fanyi Sun
"""

import numpy as np


a = np.array([[np.nan, 0.0052868252021679345], [np.nan, -0.010676627201332247], [np.nan, np.nan], [np.nan, np.nan]])
b = np.array([[np.nan, 0.018076825202167933], [np.nan, -0.0018226272013322463], [np.nan, np.nan], [np.nan,np.nan]])

print(a)
print(b)
print(a+b)
diff = np.abs((a - b) / b)
similarity = np.nanmean(1 / (1 + diff))
print(similarity)

a = np.array([np.nan,1,np.nan,np.nan])
b = np.array([1,2,3,np.nan])
# print((np.isnan(a)==np.isnan(b)))
print((np.isnan(a)==False) & (np.isnan(b)==False))
a = []
if not a:
    print(1)
# a = a[(np.isnan(a)==False) and (np.isnan(b)==False)]
# print(a)
# =============================================================================
# print((0.9556491217172831 + 0.9104752719339859 +0.8244011747479655+ 0.696831611671048)/4)
# 
# a = [0.23793498044971062, [np.nan,0.25], 0.22491570862845833, [np.nan,0.25]]
# # [1,2,[np.nan,0.5],5,[np.nan,0.1]]
# # print([np.isnan(x).any() for x in a].count(True)/len(a))
# missing_proportion = [np.isnan(x).any() for x in a].count(True) / len(a)
# print('nan portion: %f' % missing_proportion)
# 
# obtained = np.sum([x for x in a if not np.isnan(x).any()])
# total = 1 - np.sum([x[1] for x in a if np.isnan(x).any()])
# print(obtained)
# print(total)
# avg_simi = obtained / total
# print(obtained/total)
# 
# weight_adjust = (1 - missing_proportion **2) ** 0.5
# a = [avg_simi * x[1] * weight_adjust if np.isnan(x).any() else x for x in a]
# print(a)
# 
# a = [0.49720887986549767,
# 0.6138794507917789,
# 0.6558582830544277,
# 0.7387467776948529,
# 0.9225709004414981
# ]
# avg = np.mean(a)
# print('avg',avg)
# b = (5 - (3/8 + 1) **2) ** 0.5 - 1
# print('b:',b)
# a.append(avg*b)
# a.append(avg*b)
# a.append(avg*b)
# print(a)
# print(np.mean(a))
# =============================================================================
# =============================================================================
# a = [1,2,3,4,4]
# print(a[a.index(2)+1])
# 
# a = [None,None]
# if not any(a):
#     print(1)
#     
# a = [np.nan,np.nan,1]    
# print(np.isnan(a).all())
# if not any(a):
#     print(1)
# 
# a = np.array([np.nan,2,-1])
# b = np.array([np.nan,3])
# ans = np.nanmean(np.abs(a))
# # ans = 1/np.nan
# print(ans)
# =============================================================================

# =============================================================================
# a = 8
# b = eval('a')
# print(b)
# 
# 
# exec(f"{'a'} =0")
# print(a)
# 
# a = 5
# globals()['a'] = 0
# print(a)
# =============================================================================
# x = np.array([1,3,2,44,5,6,1,4,5])
# y = np.array([5,3,-1,6,8,99,0,1,3])
# a = np.intersect1d(y[x<4],y[x>1])
# print(a)

# =============================================================================
# a = [np.nan,2.1,1,2,3.1,np.nan]
# print(np.nanmean(a))
# 
# a = [2.1,1,2,3.1]
# print(np.mean(a))
# 
# # from fractions import Fraction
# # for x_pos in ['3/4', '1/2', '1/4']:
# #     print(Fraction(x_pos)*(2/7))
# #     # print('ychange_'+x_pos)
# #     # print(float(x_pos))
# #     # print('ychange_{}'.format(x_pos))
# 
# a = [np.nan,2.1,1,2,3.1,np.nan]
# a = [x for x in a if not np.isnan(x)]
# print(a)
# row = 9
# 
# 
# for i in ['B','C','D','E','F','G','H','I','J','K','L','M','N']:
#     print('=1/%s%d'%(i,row))
#     
#     
# a = np.isnan(np.nan)
# print(a)
# 
# =============================================================================
# =============================================================================
# x1 = np.array([-5,-2,-1,2,3,4,5])
# y1 = np.array([4,3,5,1,5,-1,-1])
# 
# x2 = np.array([-5,-1,-9,-3,1,5,2])
# y2 = np.array([6,2,5,1,5,1,4])
# 
# x = list(x1[x1<0]) + list(x2[x2>0])
# y = list(y1[x1<0]) + list(y2[x2>0])
# print(x)
# print(y)
# =============================================================================
