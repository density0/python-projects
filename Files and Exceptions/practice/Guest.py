more_guest = True
with open('Arrived_Guest.txt', 'a') as guest:

    while more_guest:
        name = input("Please input your name: ")
        guest.write(f"{name} has arrived!\n")
        choice = input("are there more guest arriving?: Y/N").capitalize()

        if choice not in 'Y':
            more_guest = False
        else:
            pass

