"""
Compute (x+y)^2.
"""

def x_plus_y_square(x,y) :
    print((x+y)*(x+y))
    return 1

x=int(input())
y=int(input())

try :
    x_plus_y_square(x,y)
except :
    print("Failed")
