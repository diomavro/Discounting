#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 29 May 2019
@author: Ole Peters
"""
import matplotlib.pyplot as plt
import numpy as np

t0=0
ta=1
tb=2
x0=np.arange(1,10000,1)
Dxa=10
Dxb=25
r=0.0

ga=1/(ta-t0)*np.log(1+(Dxa/(x0*np.exp(r*(ta-t0)))))+r
gb=1/(tb-t0)*np.log(1+(Dxb/(x0*np.exp(r*(tb-t0)))))+r

print(ga,gb)

plt.plot(x0,ga-gb,linestyle='-',color='blue')
#plt.plot(x0,gb,linestyle='-',color='red')
plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)
plt.xlabel('$x(t_0)$',fontsize=16)
plt.ylabel('$g_a-g_b$',fontsize=16)

plt.xlim(0,500)
plt.ylim(-.03,.03)
plt.savefig("./../ga_gb.pdf", bbox_inches='tight')
plt.show()
