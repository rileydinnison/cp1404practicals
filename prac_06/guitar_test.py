from prac_06.guitar import Guitar


name = "Gibson L-5 CES"
year = 1925
cost = 500

guitar = Guitar(name, year, cost)
other_guitar = Guitar("Another Guitar", 2020, 1000)

print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
print(f"{other_guitar.name} get_age() - Expected {5}. Got {other_guitar.get_age()}")
print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
print(f"{other_guitar.name} is_vintage() - Expected {False}. Got {other_guitar.is_vintage()}")

