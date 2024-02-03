# 5-3
alien_color = 'green'

if alien_color == 'green':
    print('player has earned 5 points')
else:
    print('')


# 5-4
alien_color = 'red'
if alien_color == 'green':
    print('player has earned 5 points')

elif alien_color == 'yellow':
    print('player has earned 10')

elif alien_color == 'red':
    print('player has earned 15')

else:
    print('player has earned 10 points')


# 5-6
age = 34

if age < 2:
    print('baby')
elif 2 <= age < 4:
    print('toddler')
elif 4 <= age < 13:
    print('kid')
elif 13 <= age < 20:
    print('teen')
elif 20 <= age < 65:
    print('adult')
else:
    print('elder')

# 5-7
fav_fruit = ['watermelon', 'orange', 'blueberries']

if 'orange' in fav_fruit:
    print('you really like oranges!')


# 5-8
admins = ['admin', 'al', 'rachael', 'jess']

for names in admins:
    if names == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {names} welcome back')


print(f'\n{admins}')
# 5-9

admins.clear()

print(admins)

if not admins:
    print('we need more users')

# 5-10
current_users = ['robbert', 'al', 'chloe', 'handerson']
new_users = ['al', 'chloe', 'anna', 'matt']

for user in new_users:

    if user in current_users:
        print(f'{user} is already taken')

# 5-11

number = [1,2,3,4,5,6,7,8,9]
for num in number:
    if 1 >= num <=3:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')



