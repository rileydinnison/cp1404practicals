"""
CP1404 Practical
UnreliableCar class tests
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    """Test unreliable cars."""
    good_car = UnreliableCar("Toyota", 100, 90)
    bad_car = UnreliableCar("Mazda", 100, 9)
    for i in range(1, 10):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:7} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:7} drove {bad_car.drive(i):2}km")

    print(good_car)
    print(bad_car)

main()