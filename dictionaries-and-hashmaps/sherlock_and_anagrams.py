#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sortWord(word):
    sorted_string_array = sorted(word)
    return ''.join(sorted_string_array)

def produceSubstrings(s):
    substring_list = []
    n = len(s)
    for i in range(0, n - 1):
        for j in range(0, n):
            substring = s[j:j+i+1]
            if len(substring) == i+1:
                substring_list.append(substring)
    return substring_list

def identifyAnagrams(substrings):
    dict_count = {}
    for sub in substrings:
        sub = sortWord(sub)
        if dict_count.get(sub) is None:
            dict_count[sub] = 1
        else:
            dict_count[sub] += 1
    return dict_count

def computeCombinations(n, r):
    return int((n * (n - 1)) / r)

def countAnagramPairs(anagrams):
    count_anagrams = 0
    for anagram in anagrams.keys():
        number_of_anagrams = anagrams.get(anagram)
        if number_of_anagrams > 1:
            number_of_comb = computeCombinations(number_of_anagrams, 2)
            count_anagrams += number_of_comb
    return count_anagrams

def sherlockAndAnagrams(s):
    substrings = produceSubstrings(s)
    anagrams = identifyAnagrams(substrings)
    return countAnagramPairs(anagrams)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
