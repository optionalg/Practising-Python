""" To find area of a circle,
given radius as input"""

from math import pi 

radius=float(input())
Area=pi*radius*radius
Area=str(Area)
radius=str(radius)
print("Area of the cirlce with radius "+radius+" is : ",Area)
