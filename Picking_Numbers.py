#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here

    unique_values = set(a)
    values_dict = {}
    max_counter = 0
    
    for item in unique_values:
        values_dict[item] = a.count(item)
        
    for item in unique_values:
        
        if item +1 in values_dict:
            current_sum = values_dict[item] + values_dict[item +1]
            if  current_sum > max_counter:
                max_counter = current_sum
        elif values_dict[item] > max_counter:
            max_counter = values_dict[item]
                
    return(max_counter)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
