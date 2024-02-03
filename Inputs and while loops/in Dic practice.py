# 7-8
sandwich_orders = ['ham sandwich', 'pastrami', 'meatball sub', 'philly cheese steak', 'pastrami', 'turkey',
                   'pastrami']

finished_sandwiches = []

print('there are no more pastrami sandwiches')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(making_sandwich)

print(finished_sandwiches)

# 7-10
polling = {}
x = 0
active = True

while active:
    prompt = input("\nWhat country would you like to vaca?")

    polling[prompt] = x
    x = x+1
    finished = input("is the poll finished? (y/n)")

    if finished == 'y':
        active = False

for country, num in polling.items():
    print(f"{polling}")
