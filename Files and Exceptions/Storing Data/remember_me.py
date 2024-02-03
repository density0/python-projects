import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'

    try:
        with open(filename) as user:
            username = json.load(user)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name?: ")
    filename = 'username.json'
    with open(filename, 'w') as user:
        json.dump(username, user)

    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    guess_name = input("what is your username?: ")
    if username:
        if guess_name != username:
            print(f"That's not right, its {username}")
        else:
            print(f"Welcome back, {username}")

    else:
        username = input("Whats your name? ")
        filename = 'username.json'
        with open(filename, 'w') as user:
            json.dump(username, user)

            print(f"I'll always remember you, {username}")


greet_user()
