class Car:
    def __int__(self, make, model, year):
        self.make = make
        self.year = year
        self.model = model
        self.odometer_reading = 0

    def getDescriptiveName(self):
        longName = str(self.year) + ' ' + self.make + ' ' + self.model
        return longName.title()

    def readOdometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it")

    def updateOdometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def incrementOdometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__int__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.getDescriptiveName())
