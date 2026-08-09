# operators in python


# Arithmetic operators

# print(5 + 3)
# print(5 - 3)
# print(5 * 3)
# print(5 / 5)     # returs decimal values i.e 1.0 
# print(5 // 5)    # this does not retun decimal values , returns only integers i.e 1
# print(5 % 3)    # modulo -> returns remainder
# print(5 ** 5)   # returns the value of 5 to the power 5 i.e 5^5





# Assignment operators

# x = 6 
# x = x + 2    
# print(x)    # here the value of x becomes 8

# x -= 2     # assigment operator
# print(x)   # here the value of x becomes 6


# x += 1
# print(x)

# x *= 2
# print(x)


# x //= 2
# print(x)

# i = 0 
# i += 1
# print(i)




# Operator precedence

# priorities/Precedence ->  () , * , / , + , -


# expression = 2 + 3 * 5 - 4 //(2+2)
# print(expression)




# Comparision operators

# > , < , <= , >= , == , !=

# print(5>2)
# print(5<2)

# print(5 <= 6)
# print(6>=8)
# print( 9 == 2)
# print( 2 == 2)
# print(3 != 2)
# print(4!=4)



# Logical operators

# and , or ,not 

# or -> if one condn is true it reutrns true
# and -> if one condn is false it returns false
# not -> give the opposite of the given condition


# print( (5>2) or (5 < 3))  # or operation
# print( (5>2) or (5 < 6))

# print( (5>2) and (5 < 3))
# print( (5>2) and (6 < 3))  # and operation
# print( (5>2) or (5 >= 3))

# print(not True)
# print(not False) # not operation


# conditional statements


# age = 44
# if age >= 18:
#     print("you can drive / vote")
    
# elif age < 18 :
#     print("you are a kiddo")
    


# QQ  to print grades A, B, C according to marks obtained

# marks = 75

# if marks > 80 :
#     print("A")
# elif marks >60 and marks <=80:
#     print("B")

# elif marks <= 60 :
#     print("C")
    
    
    
    
    
# practice exercise 3
 
# Building a mini project calculator.
 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("enter the operator (+,-,/,*,**,%): ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
   print(num1*num2)
elif operator == "/":
   print(num1/num2)
elif operator == "%":
   print(num1%num2)
elif operator == "**":
   print(num1**num2)
   
else:
    print("Invalid operation")
   
#    .........and so on for other  operators
    


    
    
    
    
    



