MINIMUM_NUMBER_OF_LETTERS = 3


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks based on length of password"""
    for i in range(len(password)):
        print("*", end="")


def get_password():
    """Get password and determine if length is long enough"""
    password = input("Enter password: ")
    while len(password) < MINIMUM_NUMBER_OF_LETTERS:
        print("Invalid")
        password = input("Enter password: ")
    return password


main()
