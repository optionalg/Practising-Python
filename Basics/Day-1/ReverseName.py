"""Program to accept first and last name of the user and print then in reverse"""

print("Please provide your first name")
Fname=input()
print("and your last name")
Lname=input()

'''
FnameLen=len(Fname)
LnameLen=len(Lname)
Fname2=""
Lname2=""

for i in FnameLen :
    Fname2+=string.append(Fname

for i in LnameLen :
    Lname2+=Lname[i]

Fname=Fname[-FnameLen:]
Lname=Lname[-LnameLen:]
'''
                          
print("The reversed name string is : "+Lname[::-1]+" "+Fname[::-1])
