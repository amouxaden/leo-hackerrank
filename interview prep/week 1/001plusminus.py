#
# 2021/11/09
# Leo Dan Peña
# Day #1 of HackerRank Three Month Interview Prep Kit
# https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/
#

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    posCount = 0
    negCount = 0
    zerCount = 0
    
    for number in arr:
        if (number >= 1):
            posCount += 1
        elif (number <= -1):
            negCount += 1
        elif (number == 0):
            zerCount += 1
    
    print(format(posCount/len(arr),".6f"))
    print(format(negCount/len(arr),".6f"))
    print(format(zerCount/len(arr),".6f"))

    

if __name__ == '__main__':

    arr = [1, 2, 3, -1, -2, -3, 0, 0]
    print("expected:\n" + "0.375000\n0.375000\n0.250000\n")
    print("result:" )
    plusMinus(arr)

    
