#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):

    dic = {}
    for word in magazine:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
            
    for word in note:
        if dic.get(word) != None and dic.get(word) > 0:
            dic[word] = dic[word] - 1
            continue
        else:
            print("No")
            return

    print("Yes")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
