"""
To print colours of list 1 whiche are not present in list 2.
"""

colours_1=['white', 'blue', 'orange']
colours_2=['pink','orange','blue']

for i in colours_1 :
    for j in colours_2 :
        if i==j :
            print(i)
