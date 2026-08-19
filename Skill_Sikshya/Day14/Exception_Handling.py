# Exception Handling

# Types of Errors 

# Syntax Errors
# Runtime Errors
# Logical Errors

# Exceptions

# Built-in Exceptions

# User-Defined Exceptions


# number = 56.33

# if isinstance(number, int):
#     print(f"Square Root : {number ** 0.5}")
    
# else:
#     raise TypeError(f"Value should be int, not {type(number)}")


# Python raise Statement

# Syntax :  raise Exceptontype("Exception Message")


# def divide(x, y):
#     if y == 0 :
#         raise ValueError("Divisor Should not Be Zero")
    
#     return x / y

# divide(4,0)


# User Defined Exceptions


# class InvalidAgeException(Exception):
#     # Raise when age is leass than 18
#     pass

# def check_customer(customer_id):
#     age = 15
    
#     if "liquor" :
#         if age >= 18:
#             print("Good to go")
            
#         else:
#             raise InvalidAgeException("Must be an Adult to buy liquor, Age > 18")
        
    
# check_customer(9090)
    
    
# ATM error


# class InsufficientBalance(Exception):
#     # raise when balance is in sufficient
#     def __init__(self, withdraw):
#         self.withdraw = withdraw
    
#     def check_balance(self):
#         Balance = 20000
            
        
#         if Balance < self.withdraw:
#             raise InsufficientBalance("Your account has Insufficient Balance")
        
#         print("Good to go")
        
# InsufficientBalance(50000).check_balance()


class InsufficientBalance(Exception):
    # raise when balance is in sufficient
    pass
    
    
def check_balance(Balance, withdraw):
        Balance = 20000
            
        if Balance < withdraw:
            raise InsufficientBalance("Your account has Insufficient Balance")
        
        print("Good to go")
        
        
check_balance(50000,6000)



