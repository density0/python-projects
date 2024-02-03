"""Generator functions allow you to declare a function that behaves like an iterator"""


# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_first_n = sum(firstn(3))

print(sum_of_first_n)


