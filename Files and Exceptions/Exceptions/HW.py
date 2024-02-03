
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("thats not a string?")

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("\nYou can't divide by zero")
finally:
    print('All done now')


def ask():
    active = True
    while active:
        try:
            square = int(input("\nInput an integer: "))

        except ValueError:
            print("That's not a number dumbass")
        else:
            print("good job!")
            active = False
            return print(square**2)


ask()


