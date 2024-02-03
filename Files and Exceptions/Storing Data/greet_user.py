import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = 'username.json'
try:
    with open(filename) as user:
        username = json.load(user)

except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as user:
        json.dump(username, user)
        print(f"I'll always remember you {username}")
else:
    print(f"Welcome back, {username}")
