# 9-3 Ice Cream
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The restaurant name is "{self.restaurant_name}", they have {self.cuisine_type} food')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!\n')


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['piss', 'chocolate']

    def all_flavors(self):
        print("boys and girls we have all kinds of flavors like: ")
        for flavor in self.flavors:
            print(f"{flavor} flavored ice cream!!!!!")

"""
bobs = IceCreamStand('bobs icecream parlor', 'world wide!')

bobs.describe_restaurant()
bobs.all_flavors()
"""

# 9-7 Admin
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


# 9-8 Privileges:
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("This is the shit the admins think of:")
        for thoughts in self.privileges:
            print(f"{thoughts}")


class Admin(User):
    def __init__(self, first_name, last_name, friends_list):
        super().__init__(first_name, last_name, friends_list)

        self.priv = Privileges(["pizza gate ate your head", "mommy milk dried up",
                                "your birth is coming"])

"""
robbin = Admin('robbin', 'thunder', 7)
robbin.greet_user()
robbin.priv.show_privileges()
"""
