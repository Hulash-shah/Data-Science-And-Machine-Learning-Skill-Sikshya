
# # Python OS Module

import os

# print(os.getcwd())

# # os.mkdir("test")


# os.chdir("test")

# if os.path.exists("test"):
#     pass
# else:
#     print("file doesnot exist")
    
    
# # Make folder without error


# print(os.makedirs("test", exist_ok = True))  #makes a directory if same directories doesnt exist

# print(os.path.join("test", "file.txt")) # create a new file inside directory


# print(os.listdir())  # lists the directories

# print(os.listdrives()) # lists the drives

# print(os.rmdir("test")) # removes the directory

# os.remove("test")


#  Working with Environment Variables


# print(os.environ)

# print(os.getenv("OneDrive"))



# Random Modules In Python

import random

# print(random.random())  # generates  number between [0,1)

# print(random.uniform(10,20))  # generates unifrom random numbers taking means


# print(random.randint(10,20))

# print(random.randrange(10,20,1))  
# print(random.randrange(10,20,2))  # generates random even numbers


# Sequence Related Functions

# cards = ["nine", "ten", "jack", "queen", "king", "ace"]

# random.shuffle(cards)

# print(random.choices(cards))

# print(random.choices(cards))

# print(random.choices(cards))

# print(random.choices(cards, k = 3))  # with replacement

# print(random.sample(cards, k = 3) ) # without replacement



# Distributions and Probability Density Functions






# Random-Related Functions

# random.seed(456)    # if the seed is same then the random numbers generated for everyone will be same
# print(random.random())


# print(random.randint(1, 100))


# Date-Time Modules in Python

import datetime

birth_date = datetime.date(2002, 6, 5)

print(birth_date)

today = datetime.date.today()
print(today)

# Arthmetic Operation
age = today - birth_date

print(age)


print(today > birth_date)


print(datetime.date.fromtimestamp(1786343544))


print(datetime.date.fromisoformat("1998-01-31"))
