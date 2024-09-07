class Circle :
    def __init__(self,radius):
        self.radius = radius

    def area (self):
        return (22/1) * (self.radius**2)
    
    def perimeter (self):
        return 2 * (22/7) * self.radius
    

c1 = Circle(5)

print(round(c1.area()))
print(round(c1.perimeter()))
