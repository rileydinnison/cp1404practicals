
MINIMUM_NUMBER_OF_LETTERS = 3

password = input("Enter password: ")

while len(password) < MINIMUM_NUMBER_OF_LETTERS:
    print("Invalid")
    password = input("Enter password: ")

for i in range(len(password)):
    print("*", end="")
