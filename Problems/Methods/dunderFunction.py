#dunder function 

#a+b  is a.__add__(b)
#a-b  is a.__sub__(b)
#a*b  is a.__mul____(b)
#a/b  is a.__truediv____(b)
#a%b  is a.__mod____(b)

class Complex :
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i+",self.img,"j")

    def __add__(self, num2): #dunderFunction
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self, num2): #dunderFunction
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(5,7)
num2.showNumber()

num3 = num1.__add__(num2)
num3.showNumber()

num3 = num2-num1
num3.showNumber()

