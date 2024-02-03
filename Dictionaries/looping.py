fav_foods = {'icecream' : 'choccy',
             'sandwiches': 'hambugers',
             'soups': 'none',
             'pork': 'none'}

# looping through all key-value pairs
for key, value in fav_foods.items():
    print(f"\nKeys: {key}")
    print(f"Value: {value}")

print("\n")

# print all keys
for name in fav_foods.keys():
    print(name.title())

print("\n")
# looping in particular order
for name in sorted(fav_foods.keys()):
    print(f"{name.title()}")

print("\n")
# print all values
for food in fav_foods.values():
    print(food.title())

print("\n")
# to get a none repetitive list we can use set()
for food in set(fav_foods.values()):
    print(food.title())
