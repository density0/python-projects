# numbers in input() get turned into strings
# use int(var) to turn back into an int
age = input("How old are you? ")
age = int(age)

if age >= 15:
    print(True)
else:
    print(False)


# Modulo Operator
num = input("Enter a number and I'll show if its odd or even: ")
num = int(num)

if num % 2 == 0:
    print(f"\nThe number {num} is even.")
else:
    print(f"\nThe number {num} is odd.")
