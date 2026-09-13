# Question: File Read and Write
# Write a Program that Uses Functions write_to_file and read_from_file:

# write_to_file(filename, content): Writes content to a file named filename. If the file doesn't exist, it should be created.
# read_from_file(filename): Reads and prints the content of a file named filename. Call write_to_file to write "Hello, Python!" 
# to a file named "greetings.txt", then call read_from_file to read and print the content of this file.


# Solution:


with open(r"C:\Users\shahh\OneDrive\Desktop\Data Science And Machine Learning\Assignments\greetings.txt", mode = 'r+') as file:
    
    file.write("Hello, Python!\n")
    print(file.read())
    
print("Closed")



# Question : Book Keeper
# Following the data below , complete the given Tasks :

# A list of tuples, where each tuple contains information about a book: (title, genre, year_published, times_borrowed).

books = [
    ("The Alchemist", "Fiction", 1988, 250),
    ("The Da Vinci Code", "Mystery", 2003, 300),
    ("A Brief History of Time", "Science", 1988, 150),
    ("The Theory of Everything", "Science", 2002, 100),
    ("Pride and Prejudice", "Fiction", 1813, 200),
    ("To Kill a Mockingbird", "Fiction", 1960, 180),
    ("The Catcher in the Rye", "Fiction", 1991, 220),
    ("Angels & Demons", "Mystery", 2000, 210),
    ("The Grand Design", "Science", 2010, 90),
    ("1984", "Fiction", 1949, 190)
]

# Task 01: Create a Book Filtering Function

# Given the list books as shown below, write a Python function named filter_books that filters books based on genre and publication year. The function should take two parameters: genre (a string) and year (an integer). It should return a list of book titles that match the given genre and have been published on or after the specified year.

# Example usage : print(filter_books("Fiction", 1980))
# Expected output: ['The Alchemist', 'The Catcher in the Rye']
# Try to use List Comprehension with If condition

def filter_books( genre : str , year : int):
    
    return [
        title 
        for title ,book_genre , year_published , time_borrowed in books 
        if book_genre == genre and year_published >= year
        
    ]
    
print(filter_books("Mystery", 2000))
print(filter_books("Fiction",1900))



# Task 02 : Write a Python program that uses a lambda expression to sort this list by publication year in ascending order.
# Print the sorted list of books.

# Try using a lambda expression with the sorted() function

sorted_books = sorted(books , key= lambda book : book[2] )
print(sorted_books)



# Control Flow with Nested Loops and Complex Logic
# Write a Python program that simulates a number guessing game:

# The program should generate a random number between 1 and 100 and give the user 7 attempts to guess it.

# After each wrong guess, the program should provide a hint whether the guess was too high or too low.

# If the user fails to guess the number within the attempts, the program should reveal the number and
# ask if they would like to play again.

import random
guess = 51
i = 1 
for i in range (7) :
    
     random_num = random.randint(1 , 100)
     
     if random_num == guess :
         print ("This was the real guess: ", random_num)
     else:
        if random_num < guess :
          print("guess is greater than this number: ", random_num)
        else:
            print("guess is smaller than this number: ", random_num)
i += 1
print(guess)
print("Would you like to play again?")



# Question:
# Write a Python program to check whether a given number is an Armstrong number or not.

# Definition: An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example:

# 153 is an Armstrong number because ( 1^3 + 5^3 + 3^3 = 153 ).
# 9474 is an Armstrong number because ( 9^4 + 4^4 + 7^4 + 4^4 = 9474 ).
# Input:
# An integer (e.g., 153).

# Output:
# Output "Yes, it's an Armstrong number." if the number is an Armstrong number. Otherwise, output "No, it's not an Armstrong number."

# Constraints:

# The input should be a positive integer.


# <---------Solution-------->


number = int(input("Enter a number:\n"))


og_num = number

no_of_digits = len(str(number))
sum_of_powers = 0

while number > 0 :
    digit = number % 10
    sum_of_powers += digit ** no_of_digits
    number = number // 10
    
if og_num == sum_of_powers :
    print (f"{og_num} is an armstrong number")
else:
    print(f"{og_num} is not a armstrong number")
    
    
    
    
    
# Write a Python program that iterates through integers from 1 to 50. For each multiple of three, print "Fizz" instead 
# of the number; for each multiple of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".
# The FizzBuzz problem is a common coding challenge that is often used in programming interviews to test basic programming skills.
# The problem typically requires writing a function that prints numbers from 1 to a given limit, but with a twist:

# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".



i = 1
for i in range(1 , 50):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", i)
    elif i % 3 == 0:
        print("Fizz", i)
    else:
        if i % 5 == 0:
           print("Buzz",i)

        





  





            

