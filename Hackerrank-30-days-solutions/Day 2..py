#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    x=meal_cost*(0.01*tip_percent)
    y=meal_cost*(0.01*tax_percent)
    totalcost=meal_cost+x+y
    print(round(totalcost))
    
    

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
