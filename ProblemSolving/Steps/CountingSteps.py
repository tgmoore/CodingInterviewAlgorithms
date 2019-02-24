# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:07:42 2019

@author: tgmoore
"""
import math
#Counting steps solution
#   input: two integers x y
#   output: minimum steps

def indexOfNearestSmallerTriangularNumber(n):
    tri = 0
    index = 0
    while (math.floor(n)-index) > tri:
        index += 1
        tri += index
    return [index, tri]

def fastIndex(n):
    m=int(math.sqrt(2*n+.25) - .5) #solve it for the explicit formula
    return [m, int((m*(m+1))/2)]
    
#Take in two integers
#   find the difference
#   divide by 2, call it total
#   find the index of the nearest smaller triangular number
#   subtract the triangular number from total
#   if twice total is larger than index + 1, add 2

with open("input.txt", "rU") as file:
    for line in file:
        if line.strip():
            spl = line.split(" ")
            # First, compute the necessary distance to "walk"
            distance = int(spl[1]) - int(spl[0])
            halfway = distance/2
            steps, triangleSteps = fastIndex(halfway)
            stepCount = 2*steps
            if 2*(halfway - triangleSteps) > steps+1:
                stepCount += 2
            elif halfway - triangleSteps > 0:
                stepCount += 1
        
            print(stepCount, "\n")