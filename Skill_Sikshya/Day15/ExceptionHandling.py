# Exception Handling In Python

# try:
#     num = int(input("Enter a number: "))
#     print(6 / num)
    
# except ValueError as e:
#     print(e)
#     print("Invalid Input")
    
    
# Catching Multiple Exceptions

# try:
#     num = int(input("Enter a number: "))
#     print(6 / num)
    
# except ValueError as e:
#     print(e)
#     print("Invalid Input")
    
# except ZeroDivisionError as e:
#     print("cannot divide by zero")
    
# except Exception as e:
#     print("Unknown Error", e)  # this part is used when we are unknown about what type of erros will occur.
#     print(0)
    
# print("End of program")



# type conversion error

# value = "abc"

# try:
#     print(int(value))

# except (ValueError, TypeError) as e:
#     print(f"{value} -> cannot be converted to int: -> {e}")
    
    
# user defined exception

# class InvalidAgeException(Exception):
#     pass

# def check_customer(age):
#     if age >= 18:
#         print("good to go")
        
#     else:
#         raise InvalidAgeException("Must be an adult to but liquor, age > 18")
    

# try:
#     check_customer(
#         int(input("Enter your age: "))
#     )
    
# except InvalidAgeException as e:
#     print("transaction Cancelled - User Under Age 18")

# except (ValueError, TypeError) as e:
#     print("Enter a valid age , int -> age")

    
    
# the else block in python Exception Handling


# try:
#     x = float(input("Number: "))
#     y = int(input("Number: "))
#     result = x / y
# except ValueError as e:
#     print("Invalid Input - ", e)
#     result = 1
    
# else:
#     print("Final Result", result)
    
    

# The finally Block


# try:
#     x = float(input("Number: "))
#     y = int(input("Number: "))
#     result = x * y
# except ValueError as e:
#     print("Invalid Input - ", e)
#     result = 1
    
# else:
#     print("Final Result", result)
    
# finally:
#     print("End of Program")
    
    
# Error Handling
# lst = ["a","b","c","d"]
 
# def get_elements(index):

#     return lst[index]
 
# If index value  > len(lst) --> Error

# In that condition , return last element of the list
 
# lst = ["a", "b", "c", "d"]

# def get_elements(index):
#     try:
#         return lst[index]
#     except IndexError:
#         print("Fallback to last element")
#         return lst[-1]


# print(get_elements(1))   
# print(get_elements(3))   
# print(get_elements(5))  



# Python Decorators

# # Example

# class Test:
    
#     @staticmethod
#     def something():
#         print("Hello")
    
# # Implementation
    
#     def decorator(function):   #<- Function as argument/parameter
        
#         # Inner Function
#         def wrapper():
            
#             print("Before Function Call")
#             print(function().upper()) # actual funtion call
#             print("After Function Call")
            
#         return wrapper # return function as value

#     @decorator 
#     def greet():
#         return "Hello World"

#     greet()
    
    
# validating an email 

import uuid
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Execution Time: {end - start:.6f} seconds")

        return result

    return inner

def validate_email(func):
    def inner(user_email):
        if user_email.endswith("@gmail.com"):
            return func(user_email)
        
        return "only support email from gmail"
    
    return inner

@calculate_time       
@validate_email
def get_reset_code(email):
    return str(uuid.uuid1())[:8]

print(get_reset_code("shahhulash@gmail.com"))
print(get_reset_code("shahhulash@gmail.com.np"))


