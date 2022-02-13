#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    if x1 == x2:
        return('YES')
    elif x1 < x2:
        first_kangaroo = x1
        first_kangaroo_step = v1
        second_kangaroo = x2
        second_kangaroo_step = v2
    else:
        first_kangaroo = x2
        first_kangaroo_step = v2
        second_kangaroo = x1
        second_kangaroo_step = v1
    
    distance_between_kagaroos = second_kangaroo - first_kangaroo
    
    first_kangaroo_jump = first_kangaroo + first_kangaroo_step
    second_kangaroo_jump = second_kangaroo + second_kangaroo_step
    distance_between_kagaroos_after_jump = second_kangaroo_jump - first_kangaroo_jump
    
    
    if distance_between_kagaroos <= distance_between_kagaroos_after_jump:
    
        return('NO')
    
    else:
        distance_reducted = distance_between_kagaroos - distance_between_kagaroos_after_jump
        if distance_between_kagaroos % distance_reducted == 0:
            return('YES')
        
        else:
            return('NO')
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
