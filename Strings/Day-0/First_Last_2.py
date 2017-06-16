"""
To print first 2 and laste 2 characters of a string by concatenation.
"""


string=input()
l=len(string)
if l>2 :
    string1=string[0:2]
    string2=string[6:8:-1]
    print(string1+string2)
else :
    print(string)
    
