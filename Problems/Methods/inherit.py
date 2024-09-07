class Car:

    @staticmethod
    def Start():
        print("Car Started")

    @staticmethod
    def Stop():
        print("Car Stopped")

class Tata(Car) :
    def __init__(self,carName):
        self.carName = carName


car1 = Tata("Tata Safari")
car2 = Tata("Tiago")

print(car1.Start())
print(car1.Stop())

