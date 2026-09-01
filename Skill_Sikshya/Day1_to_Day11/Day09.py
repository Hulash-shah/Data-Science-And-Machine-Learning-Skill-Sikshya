# ASSIGNMENT DAY 3
# Question : Check for Palindrome
# Write a Python program using a lambda function to check if a given string is a palindrome.

# Example:

# Input: "level"

# Output: True


# Solution

name = input("Enter a String of your choice: ")

check = lambda name: f"{name} is a Palindrme string" if  name  == name[: : -1] else f"{name } is not a palindrome string"

print(check(name))


# The E-Commerce Analytics Pipeline (map, filter, reduce)
# Scenario: You have a list of raw transaction dictionaries:

# transactions = [
#     {"id": 101, "amount": 250.0, "status": "completed", "currency": "USD"},
#     {"id": 102, "amount": 0.0,   "status": "pending",   "currency": "USD"},
#     {"id": 103, "amount": 180.5, "status": "completed", "currency": "USD"},
#     {"id": 104, "amount": 45.0,  "status": "refunded",  "currency": "USD"},
#     {"id": 105, "amount": 500.0, "status": "completed", "currency": "USD"},
# ]
# Task: Using only map(), filter(), functools.reduce(), and lambda expressions (no explicit for or while loops):

# Filter out all non-"completed" transactions.
# Map a 10% tax addition onto the remaining amounts.
# Reduce the mapped values into a single net revenue total formatted to 2 decimal places.


# Solution

transactions = [
    {"id": 101, "amount": 250.0, "status": "completed", "currency": "USD"},
    {"id": 102, "amount": 0.0,   "status": "pending",   "currency": "USD"},
    {"id": 103, "amount": 180.5, "status": "completed", "currency": "USD"},
    {"id": 104, "amount": 45.0,  "status": "refunded",  "currency": "USD"},
    {"id": 105, "amount": 500.0, "status": "completed", "currency": "USD"},
]


check_completed = filter(lambda t:  t["status"] == "completed", transactions )
print((check_completed))


taxed = map(lambda a : a["amount"]*1.1, check_completed)
print((taxed))

from functools import reduce
net_revenue = reduce(lambda x, y: x + y, taxed)
print(f"Net Revenue: {net_revenue:.2f}")


# Scenario:
# You are tasked with designing a system for a vehicle rental company. The company rents out various types of vehicles like 
# Cars and Bikes, and each vehicle has some shared characteristics but also some distinct ones.

# Requirements:
# Each Vehicle has attributes such as:

# vehicle_id: A unique identifier for the vehicle.
# brand: The brand of the vehicle.
# rental_price: Price per day to rent the vehicle.
# Both Car and Bike are types of Vehicles.

# A Car has an additional attribute: number_of_doors.
# A Bike has an additional attribute: bike_type (e.g., mountain bike, racing bike).
# You should provide methods to:

# Calculate total rental cost: Given the number of rental days, calculate the total cost for any vehicle.
# Display vehicle details: For both cars and bikes, display details including the unique attributes (e.g., number_of_doors for cars, bike_type for bikes).
# Implement the following OOP concepts:

# Abstraction: Provide a clean interface for calculating the total rental cost and displaying vehicle details, hiding the internal logic.
# Inheritance: Both Car and Bike should inherit common functionality from the Vehicle class.
# Polymorphism: Use method overriding so that the method for displaying vehicle details works differently for cars and bikes.
# Task:
# Define a Vehicle base class that implements the common attributes and methods.
# Define two subclasses Car and Bike that inherit from Vehicle and implement their specific attributes.
# Use encapsulation by making attributes private and providing public methods to interact with them.
# Use polymorphism to create a display_details method that behaves differently for Car and Bike.

    

# Solution
class Vehicle:

    def __init__(self, vehicle_id, brand, rental_price):
        self.__vehicle_id = vehicle_id
        self.__brand = brand
        self.__rental_price = rental_price

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_brand(self):
        return self.__brand

    def get_rental_price(self):
        return self.__rental_price

    def calculate_rental_cost(self, days):
        return self.__rental_price * days

    def display_details(self):
        print(f"Vehicle ID: {self.__vehicle_id}")
        print(f"Brand: {self.__brand}")
        print(f"Rental Price: {self.__rental_price}")


class Car(Vehicle):

    def __init__(self, vehicle_id, brand, rental_price, number_of_doors):
        super().__init__(vehicle_id, brand, rental_price)
        self.__number_of_doors = number_of_doors

    def display_details(self):
        print("Car Details")
        print(f"Vehicle ID: {self.get_vehicle_id()}")
        print(f"Brand: {self.get_brand()}")
        print(f"Rental Price: {self.get_rental_price()}")
        print(f"Number of Doors: {self.__number_of_doors}")


class Bike(Vehicle):

    def __init__(self, vehicle_id, brand, rental_price, bike_type):
        super().__init__(vehicle_id, brand, rental_price)
        self.__bike_type = bike_type

    def display_details(self):
        print("Bike Details")
        print(f"Vehicle ID: {self.get_vehicle_id()}")
        print(f"Brand: {self.get_brand()}")
        print(f"Rental Price: {self.get_rental_price()}")
        print(f"Bike Type: {self.__bike_type}")


# Creating objects

car = Car(101, "Ferrarii", 50, 4)
bike = Bike(102, "Yatri", 30, "Mountain Bike")


# Display details

car.display_details()


bike.display_details()


# Calculate rental cost

print("Car rental cost:", car.calculate_rental_cost(5))
print("Bike rental cost:", bike.calculate_rental_cost(3))