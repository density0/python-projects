fav_pizzas = ['pepperoni', 'philly cheese steak', 'pep with mushrooms & garlic']

for pizza in fav_pizzas:
    print(f'I like {pizza}')
print('I JUST REALLY LOVE PIIZA MMMMMMMMMMM\n')

birds = ['hawks', 'penguins', 'pigeon']

for beak in birds:

    print(f'a {beak} has a unique beak')
print("all birds have distinct beaks")

friend_pizzas = fav_pizzas[:]
print(f'\n{friend_pizzas}')
fav_pizzas.append('buffalo')
print(fav_pizzas)
friend_pizzas.append('plain')
print(friend_pizzas)
