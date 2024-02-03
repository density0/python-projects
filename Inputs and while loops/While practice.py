# 7-4
prompt = "\nWhat pizza toppings would you like?"
prompt += "\nEnter 'q' when you added all your toppings"
mess = ""
building = True
while building:
    mess = input(prompt)
    print(f"I'll add {mess} to your pizza")
    if mess == 'q':
        building = False

# 7-5
age = "\nWhat is your age?"

mess = ""
movie = True
while movie:
    mess = input(age)
    mess = int(mess)

    if mess < 3:
        print("Tickets are free!")
    elif 12 >= mess >=3:
        print("Tickets are $10!")
    elif mess > 12:
        print("Tickets are $15!")

    stop = input("Would you like to stop?")

    if stop == 'y':
        break
