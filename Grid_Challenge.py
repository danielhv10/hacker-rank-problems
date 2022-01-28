#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    
    for index in range(len(grid)):
        grid[index] = sorted(grid[index])
    
    print(grid)
    
    for index in range(len(grid)):
        for p_index in range(len(grid)):
            if p_index> 0 and ord(grid[p_index][index]) < ord(grid[p_index -1][index]):        
                    return 'NO'         
    return 'YES'

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
