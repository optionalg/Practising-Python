"""
Product of all List Items.
"""
def input2(x) :
    a.append(x)
    
def product(a):
    try :
        y=1
        while(1) :
            y*=a.pop()
    except IndexError :
            return(y)


a=[]

print("Take input ? y/n : ")
ch=str(input())
while ch=='y' :
    print("Enter a number as input : ")
    x=int(input())
    input2(x)
    print("Take input ? y/n : ") 
    ch=str(input())

print("Please enter a number : ")
print(a)

print(product(a))
