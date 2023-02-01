class Car:
    wheels = 4
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def description(self):
        print(f"{self.make} {self.model} was first manufactured in {self.year}. This car wears an attractive {self.color} color.")

car1 = Car("Mercedes", "AMG G63", 2013, "Black")
car1.wheels = 6
car2 = Car("Ferrari", "F40", 1987, "Red")
print(f"Number of Wheels in {car1.make} {car1.model} = {car1.wheels}")
print(f"Number of Wheels in {car2.make} {car2.model} = {car2.wheels}")
Car.wheels = 2 # Affects all instances