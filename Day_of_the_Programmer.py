#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

#find programmer_day  wich is 256th day of the month in the gregorian calendar

#leap year gregorian
#   year divisible by 400
#   divisible by 4 and not by 100

def dayOfProgrammer(year):
    # Write your code here
    year_n = int(year)
    transition_year = 1918
    day_of_programmer_1918 = f'26.09.1918'
    day_of_programmer = f'13.09.{year}'
    day_of_programmer_leap = f'12.09.{year}'
    
    day_of_programmer_result = ''
    
    if year_n == transition_year:
        day_of_programmer_result = day_of_programmer_1918
    elif year_n < transition_year:
        if year_n % 4 == 0:
            day_of_programmer_result = day_of_programmer_leap
        else:
            day_of_programmer_result =  day_of_programmer
    else:
        
        if year_n % 400 == 0 or year_n % 4 == 0 and year_n % 100 != 0:  
            day_of_programmer_result = day_of_programmer_leap
        else:
            day_of_programmer_result =  day_of_programmer
        
    return day_of_programmer_result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
