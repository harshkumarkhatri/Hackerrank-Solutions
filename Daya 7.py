#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

i=0
while (i < n):
    print(arr.pop(),end=" ")
    i+=1
