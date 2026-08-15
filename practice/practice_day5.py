
# Funtions in python
   
   
# #function call
# calc_cgt(20000)

# # funtions helps to reduce redundancy and maked code more usable .same logic can be used for multiple same type operations.



# # types of funtions

# # Module funtions => collection of related funtion , related classes , related variables

# # for example math is a module function

# import math 
# from math import sqrt,  log2

# print(dir(math))

# print(sqrt(224))
# print(log2(16))


# import random

# print(random.random()) # returns random numbers between o and 1 excluding 1

# print(random.randint(1, 100))  # returns random numbers betweeen 1 and 100


# # Practice exercise 6


# def WAF(num):
#     if num % 2 == 0:
#         print("Number is even")
        
    
#     else:
#         print("number is odd")
        
# WAF(5)



# def check(word: str) -> str:
#     count = 0
    
#     for i in word:
#         if i == 'a' or i== 'e' or i == 'i' or i == 'o' or i == 'u':
#          count += 1

#     return count
        
# print(check("vowel"))

# def check_prime(num: int) -> None:
#     if num <= 1:
#         print("Number is not prime")
#         return

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print("Number is not prime")
#             return

#     print("Number is prime")



# def average(numbers: list[int]) -> float:
#     return sum(numbers) / len(numbers)

# print(average([2,3,4,5,6,7]))


# def sum(a,b):
#     return a + b
# print(sum(2,4))





# def calc_cgt(price):  # values we define in fuction are called paramenters . Here price is parameters
#    return price * price * 0.10

# print(calc_cgt(20000))  # values we pass in fuction call are called arguments

# def calc_cgt(price):
#    new_price = price * price * 0.10
#    print(new_price)



# creating a guessing game 
import random

def play_game():
    lucky_number = random.randint(1, 100)
    
   
    
    while True:
        user_number = int(input("Enter your guess"))
        if user_number == lucky_number:
          print ("Your Guess is Correct : You won the Game!!")
          break
    
        elif user_number < lucky_number :
          print("Your guess is too low")
        
    
        elif user_number > lucky_number:
          print("Your guess is too high")
    
    print("Thankyou for playing")
play_game()
    


# naming conventions

# camel case  #   myNameIs
# pascal case  # MyNameIs
# snake_case   # my_name_is