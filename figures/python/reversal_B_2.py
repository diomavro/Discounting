#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:54:25 2018

@author: obp48
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
from matplotlib.ticker import NullFormatter
plt.ion()

fig1, ax1 = plt.subplots()

t0=0
ta=1
tb=2
x0=20
Dxa=10
Dxb=25
tPR=(Dxa*tb-Dxb*ta)/(Dxa-Dxb)

#Payouts
plt.plot([ta, ta], [x0, x0+Dxa], 'b-', lw=3)
plt.plot([tb, tb], [x0, x0+Dxb], 'r-', lw=3)

#wealth levels
plt.plot([-.3, 2.5], [x0, x0], 'k:', lw=1)
plt.plot([-.3, 2.5], [x0+Dxa, x0+Dxa], 'k:', lw=1)
plt.plot([-.3, 2.5], [x0+Dxb, x0+Dxb], 'k:', lw=1)

# slopes
plt.plot([t0,ta], [x0, x0+Dxa], 'b:', lw=2)
plt.plot([t0,tb], [x0, x0+Dxb], 'r:', lw=2)

plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

print(plt.yticks())

plt.yscale('log')
ax1.yaxis.set_major_formatter(NullFormatter())
ax1.yaxis.set_minor_formatter(NullFormatter())
print(plt.yticks())
plt.xticks([t0,ta,tb], ['$t_0$','$t_a$','$t_b$'], rotation=0)
plt.yticks([x0,x0+Dxa,x0+Dxb], ['$x(t_0)=x(t_0)^{PR}$','$x(t_0)+\Delta x_a$','$x(t_0)+\Delta x_b$'], rotation=0)
print(plt.yticks())
plt.xlim(-0.2,2.5)
plt.ylim(x0,x0+Dxb+10)
plt.savefig("./../reversal_B_2.pdf", bbox_inches='tight')
plt.show()
