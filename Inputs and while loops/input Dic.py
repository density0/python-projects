responses = {}
# flag
poll_active = True
while poll_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which planet would you like to visit? ")

    # Store planet in the dic.
    responses[name] = response

    # ask if the user wants more places to visit
    repeat = input("Would you like to add more places to visit? (y/n) ")
    if repeat == 'n':
        poll_active = False


for name, response in responses.items():
    print(f"{name} would like to go to {response}")

