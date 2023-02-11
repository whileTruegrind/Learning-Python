class Duck:
    def talk(self):
        print("The duck is quacking")
    def walk(self):
        print("The duck is walking")
class Chicken:
    def talk(self):
        print("The chicken is clucking")
    def walk(self):
        print("The chicken is walking")
class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the bird!")

duck1 = Duck()
chicken1 = Chicken()
person1 = Person()

person1.catch(duck1)
person1.catch(chicken1)