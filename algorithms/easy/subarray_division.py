# https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
# !/bin/python3

import math
import os
import random
import re
import sys
import queue


#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    fifo = queue.Queue()
    ways_can_be_divided = 0
    for element in s:
        fifo.put(element)
        if fifo.qsize() == m:
            count = 0
            for value in list(fifo.queue):
                count += value
            if count == d:
                ways_can_be_divided += 1
            fifo.get()

    return ways_can_be_divided
