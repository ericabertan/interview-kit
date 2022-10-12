#!/bin/python3

import math
import os
import random
import re
import sys

def printArray(arr):
    print(' '.join(str(el) for el in arr))

def insertionSort1(n, arr):
    pivot = arr[n - 1]
    i = n - 2
    while i >= 0 and pivot < arr[i]:
        arr[i + 1] = arr[i]
        printArray(arr)
        i -= 1

    arr[i + 1] = pivot
    printArray(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
