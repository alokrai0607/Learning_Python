class Student :
    college_name = "SSPGC"

    def __init__(self , name ,marks) :
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome Student",self.name)

    def getMarks(self):
         print("your marks is : ",self.marks)

s1 = Student("Alok" , 99) 
s1.welcome() 
print(s1.getMarks())                                                                             

