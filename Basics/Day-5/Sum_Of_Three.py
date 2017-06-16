"""
Sum of three given numbers. If 2 are equal, sum must be 0.
"""

x=int(input())
y=int(input())
z=int(input())

if x==y or y==z or x==z :
    sum=0
else :
    sum=(x+y+z)

print(sum)
