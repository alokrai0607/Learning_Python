import math

def circle_area (radius):
    return math.pi * radius ** 2
#math.pi provides a highly accurate representation of π (up to 15 decimal places).
radius = float(input("Enter the radius circle here: "))
area = circle_area(radius)
print("the area of the circle is :",area)