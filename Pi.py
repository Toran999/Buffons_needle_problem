# This program uses buffon needle problem to estimate the value of Pi
# Pi is an irrational number and its value is difficult to apprximate.
# Buffon noodle method uses the probability to get the rough estimate value of Pi over large iterations.
# When a needle of unit height is dropped between parallelly drawn lines of same length
# Then the probablility that the needle will drop crossing any of those lines is 2/PI
# If a needle is dropped for very large n times and for m times of those n drops if the needle crossed the lines then
# the probability is given by m/n
# to simulate a drop we will use random library 
# The beauty of this method is how PI emerges from completely random process.
# references: Pi and Buffon's Matches - Numberphile https://www.youtube.com/watch?v=sJVivjuMfWA

import random
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

x_axis = []
y_axis = []
#for j in range(0,10000):
for j in range(1,9):
    crossed=0
    total= 10**j

    for i in range(1, total+1):
        head = round(random.uniform(0,1),3) #generates a random position of needle head 
        theta = round(random.uniform(-1000000000,100000000),3) #gives angular orientation of needle
        y= math.sin(theta)
        tip=head+y    
        if tip>= 1 or tip<= 0:
            crossed+=1
    p= crossed/total
    pi=(2/p)
    #x_axis.append(pi)
    x_axis.append(j)
    y_axis.append(pi)
"""
n_bins=60

fig, axs = plt.subplots(1, 1,
                        figsize =(10, 7),
                        tight_layout = True)

 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    axs.spines[s].set_visible(False)
 
# Remove x, y ticks
axs.xaxis.set_ticks_position('none')
axs.yaxis.set_ticks_position('none')
   
# Add padding between axes and labels
axs.xaxis.set_tick_params(pad = 5)
axs.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
axs.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.6)
 
 
# Creating histogram
N, bins, patches = axs.hist(x_axis, bins = n_bins)
 
# Setting color
fracs = ((N**(1 / 5)) / N.max())
norm = colors.Normalize(fracs.min(), fracs.max())
 
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
 """
# Adding extra features   
plt.xlabel("log(total)")
plt.ylabel("value of π")
plt.title('frequecny distribution')

plt.scatter(x_axis,y_axis) 
# Show plot
plt.show()