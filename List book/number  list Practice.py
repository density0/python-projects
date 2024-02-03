# 4-3
for number in range(1, 21):
    print(number)

# 4-4
one_million_lives = list(range(1, 1000001))

for many in one_million_lives:
    print(many)

# 4-5
sum_mill = list(range(1, 10000001))
print(min(sum_mill))
print(max(sum_mill))
print(sum(sum_mill))

# 4-6
for odd in range(1, 21, 2):
    print(odd)

print('\n')

# 4-7
for x in range(3, 31):
    if x % 3 == 0:
        print(x)

print('\n')

# 4-8
cube = [x**3 for x in range(1, 11)]
print(cube)





