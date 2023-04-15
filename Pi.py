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

crossed=0
total= int(input("Enter total number of time you want to drop the needle: "))

for i in range(1, total+1):
    head = round(random.uniform(0,1),3) #generates a random position of needle head 
    theta = round(random.uniform(-1000000000,100000000),3) #gives angular orientation of needle
    y= math.sin(theta)
    tip=head+y    
    if tip>= 1 or tip<= 0:
            crossed+=1
p= crossed/total
pi=(2/p)
print(f"The approximate value of pi predicted after {total} experiments is {pi}")
