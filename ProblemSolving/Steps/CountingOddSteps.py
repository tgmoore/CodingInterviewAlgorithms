# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 11:05:51 2019

@author: tgmoore
"""
import math

def fastIndex(n):
   return [int(math.sqrt(n)), int(math.sqrt(n))**2]

with open("input.txt", "rU") as file:
    for line in file:
        if line.strip():
            spl = line.split(" ")
            # First, compute the necessary distance to "walk"
            distance = int(spl[1]) - int(spl[0])
            
            # Then compute the number of steps (steps) and the total distance travelled
            #   taking the largest distance per step possible (oddTriangleSteps) without
            #   travelling more than distance
            steps, oddTriangleSteps = fastIndex(distance)
            
            # Then take additional steps based on the remainder distance to be travelled:
            #   Either the distance is 0 and no additional steps should be taken
            #           or the distance is odd and a single additional step can be taken
            #               at a previously travelled odd step distance
            #           or the distance is even and two additional steps can be taken, one
            #               at a previously travelled odd step distance and one at distance
            #               one
            # We can guarantee that the largest odd remainder is an already-travelled step
            #   distance since every odd number up to oddTriangleSteps has been travelled
            #   and if the odd remainder is larger than any previously travelled odd step
            #   distance, then the number of steps can be increased by at least 1 instead
            if (distance - oddTriangleSteps)>0 and (distance - oddTriangleSteps)%2 == 0:
               steps += 2
            elif (distance - oddTriangleSteps)>0:
               steps += 1
            
            print(steps, "\n")