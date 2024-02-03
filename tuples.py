# Tuple: ordered, immutable, allows duplicate elements

banana = (1, 2, 3)
chicken = [1, 2, 3]
print(type(banana))
print(type(chicken))
print('\n')


# looping through all values in a tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)


# Can write over new vars to a tuple
dime = (344, 65)
print('Original Dimensions')
print(dime)

dime = (433, 23)
print('\nModified Dimensions')
print(f'{dime}\n')

# Practice

food = ('chicken', 'Steak', 'Buffalo', 'Oxtail', 'plain rice\n')

for ordering in food:
    print(ordering)

food = ('chicken', 'Steak', 'Pasta', 'Soup', 'plain rice')
for ordering in food:
    print(ordering)
