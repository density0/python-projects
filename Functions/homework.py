import string


def vol(rad):
    return (4 / 3) * 3.14 * (rad ** 3)


print(vol(2))


def ran_check(num, low, high):
    # Check if num is between low and high (including low and high)
    if num in range(low, high + 1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('The number is outside the range.')


print('\t')
ran_check(6, 3, 9)


def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1

        elif c.islower():
            d["lower"] += 1

        else:
            pass

    print(f"Original String : ", s)
    print(f"No. of Upper case characters : ", d["upper"])
    print(f"No. of Lower case Characters : ", d["lower"])


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))


def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x


print("\t")
print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print('\t')
print(multiply([1, 2, 3, -4]))
print('\t')


def palindrome(s):
    s = s.replace(' ', '')  # This replaces all spaces ' ' with no space ''.(Fixes issues with strings that have spaces)

    if s == s[::-1]:
        print(s)
        return True
    else:
        print(s)
        return False

    # can also do
    # return s == s[::-1]   # Check through slicing


print(palindrome('madam'))
print(palindrome('that fat ass'))


def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set of the alphabet
    alphaset = set(alphabet)

    # Remove spaces from str1
    str1 = str1.replace(" ", '')

    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation
    str1 = str1.lower()

    # Grab all unique letters in the string as a set
    str1 = set(str1)

    # Now check that the alpahbet set is same as string set
    return str1 == alphaset


print('\t')
print(ispangram("The quick brown fox jumps over the lazy dog"))
