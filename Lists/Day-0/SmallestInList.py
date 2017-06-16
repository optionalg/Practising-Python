"""
Print smallest number in  list.
"""

def smallest(l):
    flag=0
    small=l.pop()
    try :
       while(small<l.pop()) :
            flag=small
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

if len(l)==1 :
    print("Smallest number in the list is : "+str())
else :
    print("Smallest number in list : "+str(smallest(l)))
