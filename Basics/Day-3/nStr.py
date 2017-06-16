"""
To print the n copies of first 2 characters of a given string.
Return twice n times the string if len of string less than 2.
"""

n=int(input())
s=input()
s=s[0:2]

if len(s) <2 :
    print(n*2*s)
else :
    print(n*s)
    
