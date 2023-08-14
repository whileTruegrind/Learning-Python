class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("This animal eats")
class Rabbit(Animal):
    def eat(self):
        print(f"{self.name} eats carrots")

rabbit = Animal("Rabbit")
rabbit.eat()
rabbit = Rabbit("Rabbit")
rabbit.eat()