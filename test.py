# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 15:19:53 2015

@author: Sepehr
"""

from pylab import *
dim = 1000
#endT = 50
#dt = 0.001
#
#
#t = linspace(0,endT,endT/dt)
x=linspace(-2,2,dim)
sigma = 0.1
mu = 0
def y(x):
    y= (1/(sigma*sqrt(2*pi)))*exp(-(x-mu)**2/(2*sigma**2))
    return y
#
#figure(1)
#subplot(3,1,1)

#
def D(ans,a,q):
    b = ans
    d=empty(len(b))
    for k in range(q):

        for i in range(len(b)):
            if i<0.99*len(b):
                d[i] = (b[i+1]-b[i])/(a[i+1]-a[i])
            else:
                d[i] = (b[i]-b[i-1])/(a[i]-a[i-1])
        b = d 
    return b
    
#plot(x,D(y(x),x,10))
#ylim(-100,100)
#def DD(b,a):
#    dd=empty(len(b))
#    for i in range(98):
##        if i<0.9*len(b):
#        dd[i] = (b[i+2]-2*b[i+1]+b[i])/(4e-4)**2
##        else:
##            d[i] = (b[i]-b[i-1])/(a[i]-a[i-1])
#        
#    return dd
#subplot(3,1,2)
#y_x = D(y,x)
#plot(x,y_x)
#subplot(3,1,3)
#y_xx = D(y_x,x)     
#plot(x,y_xx)
#
#c =1e-4
#figure(2)
#
#q = 0
#for j in range(len(t)):
#    if j==0 or j==10000 or j==20000:
#        q+=1
#        subplot(3,1,q)
#        plot(x,y,'r')
#        ylim(0,11)
#    old = y
#    y1 = D(old,x)
#    y2 = D(y1,x)
##    for k in range(len(y)):
#    new = dt*(y2)*c + old
#    y = new

    
    
"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

#x = np.arange(0, 2*np.pi, 0.1)        # x-array
t= np.cos(x)
#line, = ax.plot(x, np.sin(x),'ro')
line, = ax.plot(x, y(x),'r')

u = y(x)

def animate(i):
    d=0
    p =  10**(-4)#exp(-4*i)/i
    dt = 1e-5
    new = D(u,x,2)
    u = new
    print(i)
#    for t in range(i):
#        
#        

    line.set_ydata(u)#(y(x+i/1000.0))#(np.sin(x+i/10.0))  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(0, 11,2), init_func=init,
    interval=300, blit=True)
plt.show()