class Student :
    def __init__(self,fullName):
        self.name = fullName
        print("Adding new student in database :  ")

s1 = Student("Alok Kumar Rai")
print(s1.name)