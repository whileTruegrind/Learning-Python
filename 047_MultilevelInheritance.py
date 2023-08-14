class Living:
    grow = True
class Animals (Living):
    def eat(self):
        print(f"{self.name} is eating.")
class Fish (Animals):
    def __init__(self, name, type, legs = 0):
        self.name = name
        self.type = type 
        self.legs = legs
    def swim(self):
        print(f"{self.name} is swimming.")
class Mammal (Animals):
    def __init__(self, name, type, legs = 4):
        self.name = name
        self.type = type 
        self.legs = legs
    def walk(self):
        print(f"{self.name} is walking.")

fish1 = Fish("Shark", "Great White")
mammal1 = Mammal("Cat", "British Shorthair")

print(mammal1.grow)
print(fish1.grow)