# Create class Engine (power) and Wheels (_size).
# Derive the class Car (model) from Engine & Wheels. 
# Display details of the car using method overriding

class Engine:
    def __init__(self,power):
        self.power=power
    def display(self):
        print(f"Power:{self.power} hp")

class Wheels:
    def __init__(self,size):
        self._size=size
    def display(self):
        print(f"Wheel size:{self._size} inches")

class Car(Engine,Wheels):
    def __init__(self,model,power,size):
        self.model=model
        Engine.__init__(self, power)
        Wheels.__init__(self, size)

    def display(self):
        print(f"model:{self.model}")
        super().display()
        Wheels.display(self)

c1 = Car("Tesla Model S", 1020, 19)
c1.display()

