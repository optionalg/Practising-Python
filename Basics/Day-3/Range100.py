"""
Program to find a number within 100 of 1000 or 2000
"""

x=int(input())
y=1100
z=900
if x <1100 and x>900 :
    print("within 1000")
elif x<2100 and x>1900 :
    print("within 2000")
else :
    print("Default")
