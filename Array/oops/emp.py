class Employee :
    def __init__(self,name,dep,sal):
        self.name = name
        self.dep = dep
        self.sal = sal

    def showDetails(self):
        print("name of Employee is :",self.name)
        print("department of Employee is :",self.dep)
        print("salary of Employee is :",self.sal)

E1 = Employee("Alok","Accounts","100000")
E1.showDetails()