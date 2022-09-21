#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    control = 0
    lastStep = [0] * steps
    i = 0
    valleys = 0
    
    while i < steps:
        
        if path[i] == 'U':
            control += 1
        
        if path[i] == 'D':
            control -= 1
            
        lastStep[i] = control
        if control == 0 and lastStep[i-1] == -1:
            valleys += 1
            
        i += 1
        
    return valleys
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
