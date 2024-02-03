# tells if either number is lesser or greater
def lesser_of_two_evens(a, b):
    # checks if both are even or odd
    if a and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(8, 4))

print(lesser_of_two_evens(678, 5))
print('\n')


def animal_crackers(text):
    wordlist = text.split()
    if wordlist[0][0] == wordlist[1][0]:
        print('true')

    else:
        print('false')


animal_crackers('Levelheaded Llama')

animal_crackers('Crazy Kangaroo')


def makes_twenty(n1, n2):
    if (n1 + n2 == 20) or ((n1 or n2) == 20):
        print('True')

    else:
        print('False')


print('\n')
makes_twenty(20, 4)
makes_twenty(5, 15)
makes_twenty(3, 7)
