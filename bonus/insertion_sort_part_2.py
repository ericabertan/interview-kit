#!/bin/python3

import math
import os
import random
import re
import sys


def printArray(arr):
  print(' '.join(str(el) for el in arr))

def insertionSort2(n, arr):
    
    for i in range(1, n):
      pivot = arr[i]
      j = i - 1
      while j >= 0 and pivot < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
      arr[j+1] = pivot
      printArray(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
