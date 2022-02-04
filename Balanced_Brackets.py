#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    #List size must be pair
    if (len(s) %2 != 0):
        return 'NO'
    
    stack = []
    closing = ['}', ']', ')']
    pairs = {'}':'{', ']':'[', ')':'('}
        
    for bracket in s:
        if bracket in closing:
            if not stack or stack.pop() != pairs.get(bracket):
                return 'NO'
        else:
            stack.append(bracket)
      
    return 'YES' if not stack else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
