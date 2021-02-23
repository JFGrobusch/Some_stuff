# -*- coding: utf-8 -*-

from math import *

"""
Created on Tue Feb 23 15:59:16 2021

basic interpolation method

play around with the bounds, number of samples, or the function.
its fun, i promise :) 

@author: Jan Grobusch
"""

def f(x): #function to interpolate
    y = sinh(x)**2
    return(y)

a, b = -2*pi, 2*pi
h = 1E-2 #step size for plotting
n = 50 #number of data points (min 2)



import numpy as np
import matplotlib.pyplot as plt

def interpolate(n): #n is the number of data points
    xl = []
    c = (b-a)/(n-1)
    for i in range(n): xl.append(a + i*c)
        
    fl = []
    for x in xl: fl.append(f(x))
    fl = np.array(fl)
    
    V = [] #generate Vandermonde matrix
    for x in xl:
        v = []
        V.append(v)
        for m in range(n):
            v.append(x**m)
    V = np.array(V)
    al = np.linalg.solve(V, fl) #solves the Vandermonde matrix, returning polynomial coefficients

    def p(x):
        y = 0
        for m in range(n):
            y += al[m] * x**m        
        return(y)
    

    xplot = []
    x = a
    while x <= b:
        xplot.append(x)
        x += h
    
    yplot = []
    for x in xplot: yplot.append(p(x))

    return(fl, xl, yplot, xplot)

fl, xl, yplot, xplot = interpolate(n)

plt.plot(xl, fl, "ro")
plt.plot(xplot, yplot)

xplot2 = []
x = a
while x <= b:
    xplot2.append(x)
    x += h

yplot2 = []
for x in xplot: yplot2.append(f(x))

plt.plot(xplot2, yplot2)
            
        
        
    


    
    


