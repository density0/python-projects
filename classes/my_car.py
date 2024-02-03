from Inheritance import Car
from electric_car import ElectricCar as EC


my_new_car = Car('toyota', 'supra', 2024)
my_new_car.odometer_reading = 23

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print('\n')
my_lucid = EC('Lucid', 'Air', 2024)
print(my_lucid.get_descriptive_name())
