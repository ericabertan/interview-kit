#!/bin/python3

import math
import os
import random
import re
import sys

def countSwaps(a):
    counter = 0
    for i in range(0, len(a)):
        for j in range(0, len(a) - 1):
            if (a[j] > a[j + 1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                
                counter += 1
                
    print("Array is sorted in {0} swaps.".format(counter))
    print("First Element: {0}".format(a[0]))
    print("Last Element: {0}".format(a[-1]))
                

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
