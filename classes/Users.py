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

