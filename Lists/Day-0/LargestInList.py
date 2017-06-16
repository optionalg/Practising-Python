"""
Print largest number in  list.
"""

def largest(l):
    flag=0
    large=l.pop()
    try :
        while(large>l.pop()) :
            flag=large
    except IndexError :
        print("")
    return(flag)



l=[]
print("Take input ? y/n : ")
ch=str(input())
while(ch=='y')  :
    print("enter a number : ")
    l.append(int(input()))
    print("Take input ? y/n : ")
    ch=str(input())
print("List : "+str(l))

print("Largest number in the list is : "+str(largest(l)))
