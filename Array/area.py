import math

def circle_area (radius):
    return math.pi * radius ** 2

radius = float(input("Enter the radius circle here: "))
area = circle_area(radius)
print("the area of the circle is :",area)