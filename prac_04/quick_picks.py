import random

NUMBERS_IN_LINE = 6
MINIMUM = 1
MAXIMUM = 45


number_of_quick_picks = int(input("How many quick picks? "))
while number_of_quick_picks < 0:
        print("Invalid amount")
        number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick = []
    for n in range(NUMBERS_IN_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))