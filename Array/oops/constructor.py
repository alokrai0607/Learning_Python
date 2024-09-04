class Student :
    def __init__(self,fullName,marks):
        self.name = fullName
        self.marks = marks
        print("Adding new student in database :  ")

s1 = Student("Alok Kumar Rai",96)
print(s1.name)
print(s1.marks)