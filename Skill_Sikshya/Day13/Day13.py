# Practice Day

# # checking a prime number

# from math import isqrt

# def check_prime(num : int) -> None :

#     if num <= 1:
#         print(f"{num} is not prime")
#         return
    
#     for i in range(2, isqrt(num) + 1 ):
#         if num % i == 0:
#             print(f"{num} is not prime")
#             return
        
       
#     print(f"{num} is prime")
    
# check_prime(29)



# # counting alphabets , digits, and special characters in a given string


# password = input("Enter a password: ")

# count_alpha = 0
# count_digit = 0
# count_spchr = 0

# for i in password:
#     if i.isdigit():
#         count_digit += 1
    
#     elif i.isalpha():
#         count_alpha +=1
    
#     else:
#         count_spchr += 1
        
# print(f"No. of Alphabets : ", count_alpha)
# print(f"No. of Digits : ", count_digit)
# print(f"No. of Special Characters : ", count_spchr)



# counting alphabets , digits, and special characters in a given string 
# Using unicodes

# 0 - 9 (unicodes from 48 to 57) 
# a- z  (97 to 122)
# A - Z  (65 - 90)

# password = input("Enter a password: ")

# count_alpha = 0
# count_digit = 0
# count_spchr = 0

# for i in password:
#     if ord(i) >= 48 and ord(i) <= 57:
#         count_digit += 1
    
#     elif ord(i) >= 97 and ord(i) <= 122 or ord(i) >= 65 and ord(i) <= 90:
#         count_alpha +=1
    
#     else:
#         count_spchr += 1
        
# print(f"No. of Alphabets : ", count_alpha)
# print(f"No. of Digits : ", count_digit)
# print(f"No. of Special Characters : ", count_spchr)



"""
While Loop

"""


# a = 0 
# while True:
#     print(a)
#     a += 1


# a = 456

# while a != 0:
#   print( a % 10)
#   a = a // 10 



# reverse of an integer


# a = int(input("Enter a number : "))

# rev = 0 

# while a > 0:
    
#     rev = rev * 10 + a %  10
#     a = a // 10

# print(rev)


# checking a number is palindrome or not


# a = int(input("Enter a number : "))

# og_a = a

# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
    
# if rev == og_a:
#     print("Palindrome")

# else:
#     print("Not Palindrome")


# Rock Paper Scissors Game
import random

choices = ["Rock", "Paper", "Scissors"]

print("Your choices are: Rock, Paper, Scissors")

while True:

    human = input("Enter your play: ").strip().capitalize()

    if human not in choices:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue

    comp = random.choice(choices)

    if (
        (human == "Rock" and comp == "Scissors")
        or (human == "Paper" and comp == "Rock")
        or (human == "Scissors" and comp == "Paper")
    ):
        print(f"You won!\nYou: {human}\nComputer: {comp}")

    elif human == comp:
        print(f"It's a draw!\nYou: {human}\nComputer: {comp}")

    else:
        print(f"You lose!\nYou: {human}\nComputer: {comp}")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
    
        
    