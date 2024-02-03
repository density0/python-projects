def addition():

    while True:
        try:
            num1 = int(input("Please enter two numbers you want to add: "))

        except ValueError:
            print("that's not a number dumbass")

        else:
            try:
                num2 = int(input("Please enter two numbers you want to add: "))

            except ValueError:
                print("that's not a number dumbass")

            else:
                print(num1.__add__(num2))
                pass


addition()