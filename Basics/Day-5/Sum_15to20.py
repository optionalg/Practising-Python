"""
Program to print sum of two numbers. If sum lies within 15 and 20, return 20.
"""

def summ(z) :
    if z>14 and z<21 :
        return (20)
    else :
        return(z)

x=int(input())
y=int(input())
z=x+y
print(summ(z))
