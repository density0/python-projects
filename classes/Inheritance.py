class Car:
    """a simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Prints a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer dumbass")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):

        """Print a statement about the range this battery provides."""
        ranges = 0
        if self.battery_size == 75:
            ranges = 260
        elif self.battery_size == 100:
            ranges = 315

        print(f"This car can go about {ranges} miles on a full charge")

    # 9-9 Battery Upgrade
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Rep aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


""""
lucid = ElectricCar('lucid', 'lucid air', 2023)
print(lucid.get_descriptive_name())
lucid.battery.describe_battery()
lucid.battery.get_range()
lucid.battery.upgrade_battery()
lucid.battery.get_range()
"""
