#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    print(sum(arr)-max(arr), sum(arr)-min(arr))
    

if __name__ == '__main__':

    arr = 7, 69, 2, 221, 8974

    print("expected = 299 9271")
    print("result   = ", end = '')

    miniMaxSum(arr)

