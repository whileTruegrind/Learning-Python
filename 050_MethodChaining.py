class Car:
    def turnOn(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive")
        return self
    def stop(self):
        print("You hit the brakes")
        return self
    def turnOff(self):
        print("You kill the engine")
        return self
car1 = Car()
car1.turnOn().drive().stop().turnOff()