# 7-1
car = input("Pick a car: ")
print(f"Lets see if i can find you a {car}")

# 7-2
people = input("\nHow many people are in your group: ")
people = int(people)
if people > 8:
    print("You'll have to wait for an open table")
else:
    print("here's a table for you")

# 7-3
num = input("\nIs your number a multiple of 10?: ")
num = int(num)

if num % 10 == 0:
    print(f"{num} is a multiple of 10")
else:
    print(f"{num} is not a multiple of 10")

