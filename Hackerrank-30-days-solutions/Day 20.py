#!/bin/python3

import sys
numberOfSwaps=0
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
for i in range(n):
    for j in range(n-1):
        if a[j]> a[j+1]:
            tmp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = tmp
            numberOfSwaps+=1
    if numberOfSwaps==0:
        break
print("Array is sorted in "+str(numberOfSwaps)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[len(a)-1]))
