class Student :
    def __init__(self,phy,chm,math):
        self.phy = phy
        self.chm = chm
        self.math = math
        self.percentage = str((self.phy+self.chm+self.math)/3)+"%"

Stu1 = Student(95,99,93)
print(Stu1.percentage)