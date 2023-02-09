from abc import ABC, abstractmethod

class Member(ABC):
    @abstractmethod
    def go():
        pass
class Car:
    def go (self):
        print("Car is moving")
class Motorcycle:
    def go (self):
        print("Motorcycle is moving")

#member1 = Member()
car1 = Car()
motorcycle1 = Motorcycle()

car1.go()
motorcycle1.go()