# 9-1: Restaurant:

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The restaurant name is "{self.restaurant_name}", they have {self.cuisine_type} food')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!\n')


restaurant = Restaurant('ni noes', 'Italian')
print(f'I fucking love love LOVE {restaurant.restaurant_name}! they make the best {restaurant.cuisine_type} food')
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2: Three Restaurants
""" Go to page 239 """
hamburger = Restaurant("MacDonald's", 'American')
hamburger.describe_restaurant()

Jamaican = Restaurant("Jamaica", 'Jamaican')
Jamaican.describe_restaurant()

mars = Restaurant("Mons Pizzeria", "Martain")
mars.describe_restaurant()


# 9-3: Users
class User:
    def __init__(self, first_name, last_name, friends_list):
        self.first = first_name
        self.last = last_name
        self.friends = friends_list
        self.login_attempts = 0

    def greet_user(self):
        print(f"\nHello {self.first} {self.last}!")

    def many_friends(self):
        print(f"You have {self.friends} Friends")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def get_login_attempt(self):
        print(f"{self.login_attempts} attempts were made")


jacob = User("Jacob", "Habros", 74)
jacob.greet_user()
jacob.many_friends()
jacob.increment_login_attempts()
jacob.get_login_attempt()
jacob.reset_login_attempts()
jacob.get_login_attempt()


al_steam = User("Bees", "Peas", 30)
al_steam.greet_user()
al_steam.many_friends()
