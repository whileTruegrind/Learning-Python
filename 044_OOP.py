class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def description(self):
        print(f"{self.make} {self.model} was first manufactured in {self.year}. This car wears an attractive {self.color} color.")

car1 = Car("Nissan", "Skyline GT-R", 2002, "Blue")
car2 = Car("Ferrari", "F40", 1987, "Red")

car1.description()
car2.description()