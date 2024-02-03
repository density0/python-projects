from Inheritance import Car


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
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

