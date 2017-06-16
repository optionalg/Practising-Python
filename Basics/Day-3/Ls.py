"""
Append Ls first to the input string, ignore if already present.
"""

s=input()
l=len(s)
if s[0:2] == "ls" :
    print("Ignore, already present!")
else :
    print("ls"+s)
