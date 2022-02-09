#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
      # Write your code here
    
    petrol_tank = 0
    first_pump = 0
    
    for index in range(len(petrolpumps)):
        petrol_tank_possible = True
        petrol_tank = 0
        
        for index1 in range(len(petrolpumps)):
            current_pump_index = (index + index1) % len(petrolpumps)
            
            petrol_tank += petrolpumps[current_pump_index][0]
            petrol_tank -= petrolpumps[current_pump_index][1]
            
            if petrol_tank <= 0:
                petrol_tank_possible = False
                break
                             
        if petrol_tank_possible:
            first_pump = index
            break

    return first_pump
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
