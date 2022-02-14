#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    
    max_hourglass = -9 * 7 # min posible value
    
    for i in range(4):
        for p in range(4):
            
            current_hourglass = arr[i][p] + arr[i][p+1] + arr[i][p+2] + arr[i+1][p+1] + arr[i+2][p] + arr[i+2][p+1] + arr[i+2][p+2]

            if current_hourglass > max_hourglass:
                max_hourglass = current_hourglass
            
    return max_hourglass
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
