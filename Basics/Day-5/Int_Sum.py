"""
To check if two given objects are of int type and compute their sum.
"""

def int_sum(x) :
    if(int(x)) :
        return x
    else :
        return 'Na'

try :
    x=int(input())
    y=int(input())
    x=int_sum(x)
    y=int_sum(y)
    print(x+y)
except ValueError :
    print(" Program error in value.")
