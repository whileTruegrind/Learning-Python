class Prey:
    def __init__ (self, name):
        self.name = name
    def flee (self):
        return f"{self.name} flees"
class Predator:
    def __init__ (self, name):
        self.name = name
    def hunt (self):
        return f"{self.name} hunts"
class PreyPredator (Prey, Predator):
    def __init__(self, name):
        self.name = name
    def both (self):
        return f"{self.flee()} and {self.hunt()}"

prey1 = Prey("Deer")
print(prey1.flee())
print()

predator1 = Predator("Orca")
print(predator1.hunt())
print()

preyPredator1 = PreyPredator("Coyote")
print(preyPredator1.both())  