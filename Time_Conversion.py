#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    splited_time = s.split(':')
    time_sufix = splited_time[2][2:4]
    splited_time[2] = splited_time[2][0:2]
    
    if(time_sufix == 'PM'):
        if(splited_time[0] != '12'):
            splited_time[0] = str(int(splited_time[0]) + 12)
    elif(splited_time[0] == '12'):
        splited_time[0] = '00'
        
    return('%s:%s:%s' % (splited_time[0], splited_time[1], splited_time[2]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
