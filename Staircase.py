#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#



def staircase(n):
    # Write your code here
    
    for size in (range(n)):
        step = ''
        blink = ''.join(' ' for item in range(n -1 -size))
        filled = ''.join('#' for item in range(size +1))
        print(blink + filled)
    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
