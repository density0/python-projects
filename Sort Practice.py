Visit = ['Japan', 'Mars', 'Earth like planet', 'Saturn', 'Washington']

print(Visit)
print(sorted(Visit))
print(f'{Visit}\n')

print(sorted(Visit, reverse=True))
print(Visit)

Visit.reverse()
print(Visit)

Visit.reverse()
print(Visit)

Visit.sort()
print(Visit)

Visit.sort(reverse=True)
print(Visit)


print("\nThe first three items on the list are:")
print(Visit[:3])

print("\nThree items from the middle of the list are:")
print(Visit[1:4])

print("\nThe last three items in the list are:")
print(Visit[-3:])
