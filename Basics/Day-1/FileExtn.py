string=''  # the final output string

def extn(j) : # function to concatenate the characters of the file name after '.'
    if j is not '.' and flag is 1 :
        string+=str(j)      
 
filename=input()
length=len(filename)
lst=list(filename) # list structure of the fikle name
#print(lst)
flag=0  # flag becomes 1 when control reaches '.'

for i in range(length) :
    if lst[i] is '.' :
        flag=1
    elif lst[i] is not '.'  and flag is 0 :
        continue
    else :
        extn(lst[i])
        
print(string)
