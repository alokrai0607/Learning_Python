class Car :

    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False

    def carStart(self):
        self.clutch = True
        print ("Clutch Press")
        self.acc = True
        print("Accelrator press")
        print("car started")

Audi = Car()
Audi.carStart()