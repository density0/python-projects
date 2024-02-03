file_name = ["animes.txt", "random.txt", "PORN PORN THIS IS PORN.txt"]


def moving_files(file_name):
    try:
        with open(file_name) as hidden:
            contents = hidden.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


for file in file_name:
    moving_files(file)
    print("\n")
