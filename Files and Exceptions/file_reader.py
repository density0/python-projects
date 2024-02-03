# open() access the file
with open('credit_card.txt') as credit_card:
    contents = credit_card.read()
    print(contents)

print('\n')

# Reading Line by Line
filename = 'credit_card.txt'
with open(filename) as credit_card:
    # to retain access to file outside with block
    # store the file's lines in a list inside the block then work with the list
    lines = credit_card.readlines()


for line in lines:
    pos_colon = line.index(":")
    name = line[0:pos_colon]
    card_info = line[pos_colon+2:]
    line = name + '\n' + card_info
    print(line.rstrip())
    print(len(line))

filename = 'planets.txt'
with open(filename, 'w') as planets:
    # if the file already exist then it'll rewrite the file
    # open() creates the file if it doesn't already exist
    planets.write("Neptune\n")

# Appending to a file
with open(filename, 'a') as planets:
    planets.write("Earth\n")
