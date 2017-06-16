"""
Check the letter if it is vowel.
"""

x=input()

'''
x=x[0:1]
v=list['a','e','i','o','u']
if (v.count('x')) :
    print("Vowel")
else :
    print("Consonent")
'''

x=x[0:1]

if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' :
    print ("Vowel")
else :
    print("Consonent ")
