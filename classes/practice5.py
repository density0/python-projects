# 9-13 Dice
from random import randint, choice


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def rolled(self):
        print(randint(1, self.sides))

    def show_dice(self):
        print(f"This dice has {self.sides} sides")


six = Dice()
six.show_dice()
for i in range(1, 10):
    six.rolled()

ten = Dice(10)
ten.show_dice()
for i in range(1, 10):
    ten.rolled()

twenty = Dice(20)
twenty.show_dice()
for i in range(1, 11):
    twenty.rolled()


# 9-14 Lottery
lottery = (10, 'grg', 3, 'dffs', 333, '2345', 343, 3334, 532,
           2355, 4355, 344, 22, '[eep', 'ekid')

for i in range(1, 5):
    winner = choice(lottery)
    print(f"congrats if you got {winner} you won!")

# 9-15 Lottery Analysis
my_ticket = 10
active = True

while active:
    winner = choice(lottery)
    count = 0
    while winner != 10:
        winner = choice(lottery)
        count += 1

        if winner == 10:
            print(count)
            print(winner)
            active = False
