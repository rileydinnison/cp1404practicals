from prac_07.guitar import Guitar


# guitars = []
#
# name = "Gibson L-5 CES"
# year = 1925
# cost = 500
#
# guitar = Guitar(name, year, cost)
# other_guitar = Guitar("Another Guitar", 2020, 1000)
#
# print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")

FILENAME = "guitars.csv"

def main():
    """Read subjects and display subjects"""
    guitar_details = read_guitars(FILENAME)
    display_guitars(guitar_details)


def read_guitars(filename=FILENAME):
    """Read data from file formatted like: name,year,cost."""
    guitars = []
    with open(filename, "r", encoding="utf-8-sig") as input_file:
        for line in input_file:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    guitars.sort()
    return guitars

def display_guitars(guitar_details):
    for i, guitar in enumerate(guitar_details, 0):
        print(f"Guitar {i}: {guitar}")





main()