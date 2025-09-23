"""
Program gets number of items and price of each item.
The total is then calculated and displayed
"""
total = 0

number_of_items = int(input("Number of items: "))

# Checks whether the number of items is 0 or greater
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Asks for each individual price for each item
for item in range(1, number_of_items + 1):
    price = float(input(f"Price of item: "))
    total += price

# If total is greater than $100, a 10% discount is applied
if total > 100:
    total *= 0.9
print(f"The total amount of all items is ${total:.2f}")
