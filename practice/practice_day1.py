#Starting with basic of python
# output , input , variables , data types , concatination




# name = "Hulash"
# age = 24
# cgpa = 9.9
# isStudent = True
# print(name, age)
# print(type(name), type(age), type(cgpa), type(isStudent))

# full_name = input("Enter your name:")
# print("Hello!", full_name)



#concatination

# print("Hello! " + full_name)




#practice exercise 1

# first_name = "Tony"
# last_name = "Stark"
# age = 53
# heaight = 1.83
# Superhero_name = input("Enter the super hero name: ")
# print(f"{first_name} {last_name} is {age} years old and his height is {heaight} meters. He is a superhero named {Superhero_name}")




#type casting = "user does the conversion manually"

# age = input("Enter your age: ")
# print(age)

# new_age = int(age) + 1

# print("The new age is :", new_age)

# print(float(new_age))
# print(bool(new_age))







#type conversion =  "interpreter does the conversion automatically"

# print(1 + 3.5)  #type conversion , implicit

# print (1 + int(2.999999))  #type casting , explicit



#sum program (a,b) = sum

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter the second number: "))

# sum = num1 + num2

# print("The Sum is:" , sum)





#String Methods and operations


# name = "Hulash"

# grade = 'b'

# print(name.upper(), grade.upper()) 

# print(name.lower(), grade.lower())

# print(name , grade)  # strings in python are immutable i.e once an string is created it cannot be changed!!!!

# above function upper() and lower() nly changes the string  for that instance where use but doesnot change the actuale string!!!!






#  find() function
# using find() to see if an element exist in the string or not
# find() function returns the index of the element if it exist

# name = "Hulash Shah"

# print( name.find("a"))
# print(name.find("x"))     # returns -1 if the element doesnot exist -- invalid value



# replace() function 

# used to replace the elments of the string or replaces thewhole string

# print(name.replace("Hulash" , "Hulee"))
# print(name)
# print(name.replace("H" , "p"))

# print(name.replace("a" , "e"))

# print(name.replace("Shah", "Saah"))




# check for presence 


# name = "Hulash Shah"

# print( 'a' in name)   # returns true as (in) checks the presence of character 'a' in the string name

# print('x' in name)   # reuturns false lly.




# Practice exercise 2


# Take prices of three products as input and calculate total  bill amount and average


# price_1 = int(input("Enter the price of first product "))
# price_2 = int(input("Enter the price of second product "))
# price_3 = int(input("Enter the price of third product "))

# total_bill_amount = price_1 + price_2 + price_3

# average_price = total_bill_amount // 3    # the // operator performs the floor division whic discards the decimal part

# print(total_bill_amount)
# print(average_price)      # due to // operator the output's decimal will not be displayed




# QQQ   take input a superhero name and check wheter it starts with 'S'/'s' or not?

# superhero_name = input("Enter the superhero name: ")

# if superhero_name.find('S') == 0 or superhero_name.find('s') == 0:
#     print("superhero name starts with 'S' or 's'", superhero_name)
    
# else:    
#    print("superhero name doesnot start with 'S' or 's'", superhero_name)




