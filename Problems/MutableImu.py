tr = "Alok"
str[0] = "K"
print(str)   #TypeError: 'str' object does not support item assignment because String is immutable in python


student = ["Shiva" , 25 , 98.2 , True]
student[0] = "Alok"
student[3] = False
print(student)   #['Alok', 25, 98.2, False]  it will change because list is mutable in python .
