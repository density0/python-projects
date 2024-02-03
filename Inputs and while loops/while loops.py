cur_num = 0
while cur_num <= 5:
    print(cur_num)
    cur_num += 1

# let the user quit
prompt = "\nI'll repeat whatever you say: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'q':
    message = input(prompt)
    print(message)


# using a flag
active = True
while active:
    message = input(prompt)
    if message == 'q':
        active = False
    else:
        print(message)


# using a continue in a loop
cur_num = 0
while cur_num < 10:
    cur_num += 1
    if cur_num % 2 == 0:
        continue
    print(cur_num)