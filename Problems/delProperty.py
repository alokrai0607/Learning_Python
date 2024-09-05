#Used to delete object properties or object itself .
class Employee :
    def __init__(self,name):
        self.name = name
    
E1 = Employee("Alok Kumar rai")
print(E1.name) #it will print

del E1.name
print(E1.name) #it will not print