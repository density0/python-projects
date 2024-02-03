# A list is a collection of items in a particular order

Car_Companies = ['Honda', 'Toyota', 'BMW', 'Mazda']
print(Car_Companies)
print(Car_Companies[0].lower())

# Can use f-strings

Which_One = f'I choose the {Car_Companies[0]} because its fun'
print(Which_One)

# List are mutable, can be changed

Flavors = ['Hot sauce', 'vanilla', 'chocolate', 'plain']
Flavors[1] = 'Banana'
print(f'\n{Flavors}')

# Can add items

Flavors.append('Watermelon')
print(Flavors)

# Can insert items in different positions

Flavors.insert(2, 'Burnt')
print(Flavors)

# Removing items

del Flavors[5]
print(f'\n{Flavors}')

# Moving removed items to a make a new list

Removed_Flavors = Flavors.pop()
print(Flavors)
print(Removed_Flavors)


# Can remove Item by value

Car_Companies.remove('Mazda')
print(f'\n{Car_Companies}')

# Can also do it with variables

Choosing = 'Toyota'
Car_Companies.remove(Choosing)
print(Car_Companies)
print(f"I choose a {Choosing} because it out last all the rest ")

# sort() method changes the order of the list permanently

# can also sort this list in reverse alphabetical order by passing the
# argument reverse=True to the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# reserves() the order of the list
cars.reverse()
print(cars)

# sorted() function lets you display your list
# in a particular order but doesn’t affect the actual order of the list.

print('\noriginal list:')
print(Car_Companies)

print('sorted list')
print(sorted(Car_Companies))