"""
To check the sum or difference or equality of two numebrs is 5.
"""

def check(x,y):
    if x==y or x+y==5 or abs(x-y)==5 :
        return True
    else :
        return False


x=int(input())
y=int(input())

print(check(x,y))
