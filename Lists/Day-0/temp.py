"""
 Python program to get a list, sorted in increasing order
 by the last element in each tuple from a given list of non-empty tuples.
"""

t1=(1,'s','c','d','f',6)
t2=('x','y')
t3=('p','q','r','s')
t4=(t1,)+(t2,)+(t3,)
l=[t4]
print(l)
t4=t1+t2+t3
print(l)
