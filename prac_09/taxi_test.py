from prac_09.taxi import Taxi


my_taxi = Taxi("Prius 1", 100)
Taxi.drive(my_taxi, 40)
print(my_taxi)
print("Current Fare: ", Taxi.get_fare(my_taxi))
Taxi.start_fare(my_taxi)
Taxi.drive(my_taxi, 100)
print(my_taxi)
print("Current Fare: ", Taxi.get_fare(my_taxi))