#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    total_bribes = 0
    # Iterate from end
    for i in range(len(q) - 1, -1, -1):
        
    # Compare value with its index + 1 (its correct position)
        if q[i] == i + 1:
            continue
                        
    # If 1 distance away
        if i - 1 >= 0 and q[i - 1] == i + 1:
            total_bribes += 1
            q[i - 1] = q[i]
                        
    # If 2 distance away
        elif i - 2 >= 0 and q[i - 2] == i + 1:
            total_bribes += 2
                    
            q[i - 2] = q[i - 1]
            q[i - 1] = q[i]

        else:
            print('Too chaotic')
            return
    
    print(total_bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
