"""
Create the tuples into a list.
"""

def createTupledList() :
    l=[]
    t=tuple()
    while True:
      print("Add a tuple ? y/n : ")
      if input()!='y':
        break
      else:
        print("Keep adding the tuple elements : (x to break)")
        while True:
          i=input()
          if i=='x':
            break
          else:
            t+=(i,)
          print(t)
        l.append(t)
    return l

l2=createTupledList()
print(l2)
