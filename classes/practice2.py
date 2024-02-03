# 9-4 Number Served
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'The restaurant name is "{self.restaurant_name}", they have {self.cuisine_type} food')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!\n')

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, adding):
        self.number_served += adding

    def get_number_served(self):
        print(f"{restaurant.number_served} guest have been served")


restaurant = Restaurant("Does Hoes", "Donuts")
restaurant.describe_restaurant()
restaurant.set_number_served(43)
print(restaurant.number_served)
restaurant.increment_number_served(10)
restaurant.get_number_served()

# 9-5
