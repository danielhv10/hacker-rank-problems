#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    
    prefix_set = set()
    word_set = set()
    
    for word in words:
        
        if word in prefix_set:
            print("BAD SET")
            print(word)
            return
        
        check = ''
        for char in word:
            
            check += char
            prefix_set.add(check)
            
            if check in word_set:
                print("BAD SET")
                print(word)
                return
            
        word_set.add(word)
        
    print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
