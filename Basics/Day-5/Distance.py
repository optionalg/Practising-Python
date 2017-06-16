"""
Compute the distance between 2 points.
"""

import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)^2+(y2-y1)^2)

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

try :
    d=distance(x1,y1,x2,y2)
    print(d)
except :
    print("Program failed. ")
