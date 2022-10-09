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
    total_bribes = 0
    size = len(q)
    
    # A variation of the insertion sort algorithm.

    for j in range(size - 2, -1, -1):
        pivot = q[j]
        bribes_for_this_person = 0
        i = j + 1
        while i < n and pivot > q[i]:
            q[i-1] = q[i]
            i += 1
            total_bribes += 1
            bribes_for_this_person += 1

            if bribes_for_this_person > 2:
                print('Too chaotic')
                return

        q[i-1] = pivot
 
    print(total_bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
