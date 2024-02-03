import json




def store_fav_num():
    filename = 'favorite number.json'
    fav_num = int(input("Please enter your fav num: "))

    with open(filename, 'w') as num:
        json.dump(fav_num, num)


def get_stored_num():
    """Get stored fav num"""
    filename = 'favorite number.json'
    try:
        with open(filename) as num:
            fav_nums = json.load(num)
    except FileNotFoundError:
        return None
    else:
        return fav_nums


def your_num():
    filename = 'favorite number.json'
    fav_num = get_stored_num()

    if get_stored_num():
        print(f"Your fav number is {fav_num}")
    else:
        fav_num = int(input("Please enter your fav num: "))
        with open(filename, 'w') as number:
            json.dump(fav_num, number)
            print(f"your favorite number is {fav_num}")


your_num()
