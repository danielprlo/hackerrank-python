#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    are_divisible = 0
    for index_a, element_a in enumerate(ar):
        for element_b in ar[index_a+1:]:
            sum = element_a+element_b
            if sum%k == 0:
                are_divisible += 1
    return are_divisible