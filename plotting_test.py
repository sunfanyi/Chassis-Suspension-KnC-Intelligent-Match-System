# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:14:20 2021

@author: Fanyi Sun
"""

import xlrd
import matplotlib.pyplot as plt
import numpy as np

path = r'D:\Desktop\test for plotting.xlsx'

a = xlrd.open_workbook(path)
sheet1 = a.sheets()[0]

# def lagragian_interpolation(xp,xn,yn):
#     yp = 0
#     for j in range(len(yn)):
#         L = 1
#         for k in range(len(xn)):
#             if k != j:
#                 L *= (xp - xn[k]) / (xn[j] - xn[k])
#         yp += yn[j] * L
#     return yp

x1 = sheet1.col_values(0)
y1 = sheet1.col_values(1)
print(x1[0])
print(x1[-1])
# plt.scatter(x1,y1,s=3,label='sample')
x2 = sheet1.col_values(2)[::3]
y2 = sheet1.col_values(3)[::3]

x2 = np.array(x2)
y2 = np.array(y2)

x2 = x2 - 100
x2_temp = x2
y2_temp = y2
x2 = x2_temp[(x2_temp >= x1[0]) & (x2_temp <= x1[-1])]
y2 = y2_temp[(x2_temp >= x1[0]) & (x2_temp <= x1[-1])]
plt.plot(x2,y2)
plt.scatter(x2,y2,s=20,c='b',marker='o',label='target')
plt.scatter(0,0.5,s=80,marker='^',c='red')
plt.scatter(x2[5:8],y2[5:8],s=20,c='red',marker='o',label='target')
# plt.legend()

# datax = sheet1.col_values(0)[2*n:4*n]
# datay = sheet1.col_values(1)[2*n:4*n]
# =============================================================================
# datax = sheet1.col_values(0)[:1024]
# datay = sheet1.col_values(1)[:1024]
# # plt.scatter(datax,datay,s=1)
# x1 = datax[768:] + datax[:256]
# y1 = datay[768:] + datay[:256]
# 
# x2 = datax[256:768][::-1]
# y2 = datay[256:768][::-1]
# 
# # x1 = x1[::-1]
# # x2 = x2[::-1]
# fit = 0
# for i in range(511):
#     if x1[i+1] > x1[i]:
#         fit += 1
# print(fit)
# # fit = 0
# for i in range(511):
#     if x2[i+1] > x2[i]:
#         fit += 1
#     else:
#         print(x2[i],x2[i+1])
# 
# print(fit)
# print(1024*0.8)
# # x1 = datax[768:]
# # y1 = datay[768:]
# # print(x1)
# 
# 
# # choose the smaller value at x1&x2 to avoid list out of range issue 
# x_leftmost = x1[0] if abs(x1[0]) < abs(x2[0]) else x2[0]
# x_rightmost = x1[-1] if abs(x1[-1]) < abs(x2[-1]) else x2[-1]
# xn = np.linspace(x_leftmost,x_rightmost,50) # 512 to 256, improve 33% speed
# 
# 
# # print(max(x1))
# # print(max(x2))
# # print(min(x1))
# # print(min(x2))
# # print(len(x1))
# # print(len(xn))
# plt.scatter(x1,y1,s=0.1,c='b')
# plt.scatter(x2,y2,s=0.5,c='g')
# def curve_redistribution(xn, x_original, y_original):
#     yn = []
#     for x in xn:
#         min_diff = 1e5
#         # search the closest point
#         for i in range(len(x_original)):
#             # if abs(i-j) < 10:
#             if abs(x - x_original[i]) < min_diff:
#                 min_diff = abs(x - x_original[i])
#                 pos = i
#         if x_original[pos] == x: # they coincide
#             yn.append(y_original[pos])
#             
#         else:
#             if abs(x_original[pos]) < abs(x):
#                 lower = [x_original[pos],y_original[pos]]
#                 upper = [x_original[pos+1],y_original[pos+1]]
#             else:
#                 lower = [x_original[pos-1],y_original[pos-1]]
#                 upper = [x_original[pos],y_original[pos]]
#                 
#             # using linear interpolation:
#             if upper[0] != lower[0]:
#                 yvalue = lower[1] + (x - lower[0]) / (upper[0] - lower[0]) * \
#                                                         (upper[1] - lower[1])
#             else: # avoid 'divided by zero' error
#                 yvalue = (lower[1] + upper[1]) / 2
#             yn.append(yvalue)
#     return yn
# 
# yn1 = curve_redistribution(xn,x1,y1)
# # yn2 = curve_redistribution(xn,x2,y2)
# 
# # yn = [(yn1[i] + yn2[i]) / 2 for i in range(len(xn))]
# 
# plt.show()
# # plt.scatter(xn,yn1,s=2,c='b')
# # plt.show()
# # plt.show()
# # plt.scatter(xn,yn,s=0.5)
# # plt.plot(x,yp)
# 
# # plt.show()
# # plt.scatter(x2,y2,s=1)
# # plt.show()
# 
# 
# 
# =============================================================================
