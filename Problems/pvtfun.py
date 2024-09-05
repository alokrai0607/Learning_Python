class Person :
    __name = "anonymous"

    def __hello(self):
        print("I am calling from Hello Pvt fuction")
    def welcome(self):
        self.__hello()
P1 = Person()
print(P1.welcome())