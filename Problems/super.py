class Car :
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")

class TyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

Car1 = TyotaCar("Fortuner","Electric")
print(Car1.name)
print(Car1.start)

