from Users import User


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
