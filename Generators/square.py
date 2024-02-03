def squares(n):

    a = 1
    b = 0

    for num in range(n):

        a, b = b**2, b+1
        yield a


for i in squares(10):
    print(i)


