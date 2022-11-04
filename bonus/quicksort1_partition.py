#!/bin/python3

import math
import os
import random
import re
import sys

def quickSort(arr):
    pivot = arr[0]

    left = []
    right = []
    equal = []

    equal.append(pivot)

    for i in range(1, len(arr)):
      if arr[i] < pivot:
        left.append(arr[i])
      elif arr[i] > pivot:
        right.append(arr[i])
      else:
        equal.append(arr[i])

    return left + equal + right        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
