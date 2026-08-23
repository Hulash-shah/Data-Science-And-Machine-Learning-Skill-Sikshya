"""
Question:-
Math Tutor Using Random, Arithmetic Operators, and OOP
Scenario: Create a MathTutor class that generates random math questions using random and math operators.

Track correct and incorrect answers.
Provide a score at the end.
Handle invalid input using exception handling.
Concepts: Random, Math, Exception Handling, Classes

"""
import random
import math


class MathTutor:

    def __init__(self):
        self.correct = 0
        self.incorrect = 0

    def generate_question(self):
        operation = random.choice(["+", "-", "*", "/", "sqrt", "power"])

        if operation == "+":
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            answer = a + b
            question = f"{a} + {b}"

        elif operation == "-":
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            answer = a - b
            question = f"{a} - {b}"

        elif operation == "*":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            answer = a * b
            question = f"{a} × {b}"

        elif operation == "/":
            b = random.randint(1, 10)
            answer = random.randint(1, 10)
            a = b * answer
            question = f"{a} / {b}"

        elif operation == "sqrt":
            a = random.randint(1, 20)
            answer = math.sqrt(a)
            question = f"√{a}"

        else:
            a = random.randint(1, 10)
            b = random.randint(1, 5)
            answer = math.pow(a, b)
            question = f"{a}^{b}"

        return question, answer

    def ask_question(self):
        question, answer = self.generate_question()

        print(f"\nSolve: {question}")

        while True:
            try:
                user_answer = float(input("Your answer: "))
                break

            except ValueError:
                print("Invalid input! Please enter a number.")

        if math.isclose(user_answer, answer, rel_tol=1e-9):
            print("Correct! ✅")
            self.correct += 1
        else:
            print(f"Incorrect ❌ Correct answer: {answer}")
            self.incorrect += 1

    def show_score(self):
        total = self.correct + self.incorrect

        print("\n--------------------")
        print("       RESULTS")
        print("--------------------")
        print(f"Correct   : {self.correct}")
        print(f"Incorrect : {self.incorrect}")

        if total > 0:
            score = (self.correct / total) * 100
            print(f"Score     : {score:.2f}%")

    def start(self):
        print("Welcome to Math Tutor!")

        try:
            total_questions = int(
                input("How many questions do you want? ")
            )

            if total_questions <= 0:
                print("Please enter a positive number.")
                return

        except ValueError:
            print("Invalid number of questions!")
            return

        for _ in range(total_questions):
            self.ask_question()

        self.show_score()


# Create object
tutor = MathTutor()

# Start the quiz
tutor.start()








"""
Question:-
Multi-file Project Using Modules and Packages
Scenario: You're building a small finance app.

Create a package finance_tools with modules: tax.py and loan.py.
Each module contains utility functions like calculate_tax() and calculate_emi().
Import and use them in a main script that takes user input to do both.
Concepts: Packages, Modules, Importing, Separation of Concerns
"""




#solved as finance_app folder

"""
Exception Handling Scenario: Online Age-Restricted Service
Scenario: You’re building a sign-up system for an online movie rental platform. Some movies are age-restricted (18+). You need to ensure proper validation and error handling during user registration.

Task:

Create a custom exception class called UnderageError that inherits from Exception.

Write a function register_user() that:

Takes a user’s name and age as input.
Raises UnderageError if the user is under 18.
Otherwise, prints a welcome message.
Wrap the function call in a try block and handle the exception.

Use else to confirm successful registration and finally to always print “Thank you for using MovieTime!” regardless of outcome.

Also try to validate if the age input is numeric. Raise a ValueError if not, and handle it separately.
"""


class UnderageError(Exception):
    pass


def register_user(name, age):

    # Validate age
    if not age.isdigit():
        raise ValueError("Age must be a number.")

    age = int(age)

    # Check age restriction
    if age < 18:
        raise UnderageError("User must be 18 or older.")

    print(f"Welcome to MovieTime, {name}!")


name = input("Enter your name: ")
age = input("Enter your age: ")

try:
    register_user(name, age)

except UnderageError as e:
    print(f"Registration failed: {e}")

except ValueError as e:
    print(f"Invalid input: {e}")

else:
    print("Registration successful!")

finally:
    print("Thank you for using MovieTime!")





"""
Problem Statement
We want to build an online shopping cart system that allows users to add products to their cart, calculate the total cost, apply discounts, and generate an invoice. The system should include the following functionalities:

Adding products to the cart
Removing products from the cart
Calculating the total cost
Applying discounts based on user type
Generating an invoice
1. Create the Product class
We create a basic Product class with attributes for the product name and price.

# Your Solution Here
2. Implement the User class
In this step, we create a User class with attributes for the user's name and whether they are a premium member.

# Your Solution Here
3. Create the ShoppingCart class
In this step, we create a ShoppingCart class with methods for adding and removing products from the cart, as well as calculating the total cost of the items in the cart.

Note: Define calculate_total_cost method in the ShoppingCart class, that applies a 10% discount to the total cost if you are premium User.

# Your Solution Here
4. Testing the functionality
Now that we have implemented the necessary classes and methods, let's test our online shopping cart system:

# Your Solution Here
5. Generating Invoice for a given cart
# Your Solution Here
Bonus Challenge
In this case each user share the same cart, which is useless. Also each user can register himself/herself as a premium user, which is not practical again. So, you have to add following two additional features to the above program, to make it more real:

Cart for a user should be independent from other users
Add a new admin feature is_admin that takes in boolean values [True, False], and only admin should be allowed to create other admins and set is_premium=True for other users
# Your Solution Here
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - Rs. {self.price:.2f}"


class User:
    def __init__(self, name, is_premium=False, is_admin=False):
        self.name = name
        self.is_premium = is_premium
        self.is_admin = is_admin
        self.cart = ShoppingCart(self)

    def make_premium(self, user):
        if not self.is_admin:
            print("Only an admin can make a user premium.")
            return

        user.is_premium = True
        print(f"{user.name} is now a premium member.")

    def create_admin(self, user):
        if not self.is_admin:
            print("Only an admin can create another admin.")
            return

        user.is_admin = True
        print(f"{user.name} is now an admin.")


class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to {self.user.name}'s cart.")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product.name} removed from the cart.")
                return

        print("Product not found in cart.")

    def calculate_total_cost(self):
        total = sum(product.price for product in self.products)

        if self.user.is_premium:
            discount = total * 0.10
            total -= discount

        return total

    def generate_invoice(self):
        print("\n========== INVOICE ==========")
        print(f"Customer: {self.user.name}")
        print("-----------------------------")

        subtotal = sum(product.price for product in self.products)

        for product in self.products:
            print(f"{product.name:<20} Rs. {product.price:.2f}")

        print("-----------------------------")
        print(f"Subtotal:              Rs. {subtotal:.2f}")

        if self.user.is_premium:
            discount = subtotal * 0.10
            print(f"Premium Discount:      Rs. {discount:.2f}")
        else:
            discount = 0

        total = subtotal - discount

        print(f"Total:                 Rs. {total:.2f}")
        print("=============================")
        
        
        
        
# Products
laptop = Product("Laptop", 80000)
mouse = Product("Mouse", 1500)
keyboard = Product("Keyboard", 3000)

# Users
user1 = User("Hulash", is_premium=True)

# Add products
user1.cart.add_product(laptop)
user1.cart.add_product(mouse)
user1.cart.add_product(keyboard)

# Calculate total
print("\nTotal cost:", user1.cart.calculate_total_cost())

# Remove product
user1.cart.remove_product("Mouse")

# Generate invoice
user1.cart.generate_invoice()



