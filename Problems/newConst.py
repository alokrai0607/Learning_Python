#Create a student class that takes name & marks of 3 subjects as arguments in constructor . Then Create a method to print the average .

class Student :
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks


    def stavg(self):
        sum = 0 
        for i in self.marks:
            sum += i
        print("Hii", self.name , "You avg score is ",sum/3)

s1 = Student("Alok Rai", [99,98,95])
s1.stavg()

