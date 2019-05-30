# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 18:31:01 2015

@author: Sepehr
"""
from pylab import *
d = 100
x = linspace(-1,1,d)
y = linspace(-1,1,d)

z= empty([d,d])
z_new= empty([d,d])
u= empty([d,d])
c=0
for i in range(d):
    c+=0.01
    for j in range(d):
        
        u[i,j]= c
        r = sqrt(x[i]**2 + y[j]**2)
        if abs(1-r)>0.02:
            z[i,j]= 0
        else:
            z[i,j] = 1# exp(-r)
figure(1)  
subplot(2,1,1)   
imshow(z,'rainbow')
#imshow(u,'rainbow')
colorbar()

dt = 0.01
dx = 0.02
dy = 0.02

# dc/dt = -d(ux c_i)/dx - d(uy c_i)/dy
#(c(t+1) - c(t))/ dt = -((u(x+1)c_i - u(x)c_i )/dx)-((u(y+1)c_i - u(y)c_i )/dy)
t=0
while t<2:
    for i in range(d-1):
        for j in range(d):
            new= -dt*u[i,j]*(z[i+1,j] - z[i,j])/dx# - dt*(((z[i+1,j] - z[i,j])*u[i,j]/dx) +\
            #((z[i,j+1] - z[i,j])*u[i,j]/dy))
            
            z_new[i,j] = new
#    if t==0.1:
#        figure(2)
    t+=dt
subplot(2,1,2)
imshow(z_new,'rainbow')
colorbar()