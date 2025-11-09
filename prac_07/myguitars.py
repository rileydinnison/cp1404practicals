from prac_07.guitar import Guitar

import csv

FILENAME = "guitars.csv"

def main():
    """Read subjects and display subjects"""
    guitar_details = read_guitars(FILENAME)
    add_guitar(guitar_details)
    display_guitars(guitar_details)
    save_guitars_to_csv(FILENAME, guitar_details)



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

def add_guitar(guitar_details):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitar_details.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")
    guitar_details.sort()
    return guitar_details

def save_guitars_to_csv(FILENAME, guitar_details):
    """Save the guitars list to the CSV outfile, overwriting any existing content."""
    with open(FILENAME, 'w', newline='', encoding='utf-8') as outfile:
        write_file = csv.writer(outfile)
        for guitar in guitar_details:
            write_file.writerow([guitar.name, guitar.year, guitar.cost])



main()