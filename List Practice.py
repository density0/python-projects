# 3-4 guest list
Invited = ['Matt', 'Delawn', 'Fed', 'Joejam', 'Sherii']

for i in Invited:
    print(f'{i} is invited to have fun ;)')

print('\n')

not_coming = Invited.pop(2)
print(f'{not_coming} wont be coming anymore :c')

Invited.append('Juli')

print('\n')

for i in Invited:
    print(f'{i} is invited to have fun ;)')




print('\nyooo i found a place where even more people can come')
Invited.insert(0, 'bryan')
Invited.insert(3, 'Phil')
Invited.append('Jday')
print('\n')
for i in Invited:
    print(f'{i} is invited to have fun ;)')


print('\nsorry everyone, i can only invite two people jus cause')


Cant_coom = Invited.pop()
print(f'\nSorry {Cant_coom}')

Cant_coom = Invited.pop()
print(f'Sorry {Cant_coom}')

Cant_coom = Invited.pop()
print(f'Sorry {Cant_coom}')

Cant_coom = Invited.pop()
print(f'Sorry {Cant_coom}')

Cant_coom = Invited.pop()
print(f'Sorry {Cant_coom}')

Cant_coom = Invited.pop()
print(f'Sorry {Cant_coom}')

print(f'\n{Invited[0]} youre still invited (;')
print(f'{Invited[1]} youre still invited (;')

del Invited[0:2]


print(Invited)