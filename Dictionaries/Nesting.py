# storing multiple dics in a list, or list of items as a value in a dic

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# can create more aliens using range()
# Make 30 green aliens.

aliens_pop = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens_pop.append(new_alien)

print("\n")

# Show the first 5 aliens.
for alien in aliens_pop[:5]:
    print(alien)
    print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens_pop)}")

for alien in aliens_pop[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens.
for alien in aliens_pop[:5]:
    print(alien)
    print("...")

# storing a list inside a dic
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese']
         }
# Sum the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# Dic in a Dic
games = {
    'Oxygen_not_included':
        {
            'type': 'colony sim',
            'total played': "200 hours",
            'rating': "5/5"
        },
    'Elite Dangerous':
        {
            'type': 'space',
            'total played': "Unknown",
            'rating': "4/5"
        }
        }

for name, info in games.items():
    print(f"\nGame:{name}")

    game_info = f"{info['type']} game \n\trating: {info['rating']}"
    rating = info['total played']

    print(f"\tis a {game_info}")
    print(f"\ttotal played time is {rating}")

