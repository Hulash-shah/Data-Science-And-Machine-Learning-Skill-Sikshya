
# # Funtions in python

# def palindrome_checker(a):
    
#     og_a = a
#     rev = 0
    
#     while a > 0:
#         rev = rev * 10 + a % 10
#         a = a // 10
        
#     if rev == og_a:
#         print("palindrome")
        
#     else:
#          print("not palindrome")
            
# palindrome_checker(121)
# palindrome_checker(1333)
# palindrome_checker(1212)

# Parameters and Arguments

# parameters are the values that you accepts while calling a funtion

# Arguments are the values tha you provide while calling funtion

# There are three types of arguments

# 1. Default Argumens
# 2. Positional Arguments
# 3. Keyword Arguments


# # 1. Positional — order matters
# def add(a, b):
#     return a + b
# add(5, 3)       # → 8

# # 2. Default — works even without passing a value
# def greet(name="Guest"):
#     print(f"Hello {name}")
# greet()            # Hello Guest
# greet("Hulash")  # Hello Hulash

# # 3. Keyword — pass in any order
# def info(name, age):
#     print(f"{name} is {age}")
# info(age=25, name="Hulash")  # order doesn't matter


# Data Structures in Python

# List
# Tuple
# Set
# Dictionary

'''
When you need to store multiple values in one variable, you use a data structure. Python gives you 4 ready to use:

Structure	Ordered?	Mutable?	Duplicates?	Access by
List	      ✅ Yes  	✅ Yes	   ✅ Yes     Index
Tuple	      ✅ Yes     ❌ No       ✅ Yes     Index
Set	          ❌ No	    ✅ Yes	   ❌ No 	Methods
Dictionary	  ✅ Yes 	✅ Yes   	Keys:❌	  Key

'''

# ls = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7]

# print(ls[1])

# ls[3] = 21

# print(ls)

# print(ls[2: 7: 2])


# # traversing a list on values

# for i in ls:
#     print(i)
    
# # traversing a list on index

# for i in range(0, len(ls)):
#     print(ls[i])



ls = [10, 20, 30, 40, 50]

ls.append(60)   # appends a new values at last of list

ls.insert(2, 25) # inserts 25 at index 2

print(ls)  # output -> [10, 20, 25, 30, 40, 50, 60]

ls.pop()  # pops out the last elements of the list -> [10, 20, 25, 30, 40, 50]

print(ls)

ls.pop(2)  # pops out the element at index 2 output->[10, 20, 30, 40, 50]

print(ls)

ls.remove(30) # removes the first occurence of the provided element from the list

print(ls)  # [10, 20, 40, 50]

ls.clear() # clears all the elements of the list

print(ls) # [] 


