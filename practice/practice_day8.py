
# Solving some question using for loop

# finding factors of a given number


# num = int(input("Enter a number: "))
# check1 = 0
# sum = 0
# for i in range(1, num+1):
    
#     if num % i == 0:
#       sum = sum + i
      
    
         
# print(f"Sum of factors of {num} is: ",sum)


# check1 = sum - num  
# print(f"Sum after excluding {num} :",check1)    
# if check1 == num :
#     print("perfect number")

# else:
#     print("not a perfect number")     
    
    
# checking a prime number

# num = int(input("Enter a number: "))

# count = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1
# if count == 2:
#     print(f"{num} is a prime number")

# else:
#     print(f"{num} is a composite number")


# reversing a string


# name = "Hulash"


# print(name[: : -1])


# car  = input("Enter a string: ")
# rev = ""
# for i in range(len(car)-1, -1 , -1):
#      rev += car[i]
    
# print(rev)
# # checking if given string is palindrome:

# if rev == car:
#     print("String is palindrome")

# else:
#     print("not a palindrome")



def check_prime(num: int) -> None:
    if num <= 1:
        print("Number is not prime")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Number is not prime")
            return

    print("Number is prime")
    
    
check_prime(174546578)
check_prime(25)
check_prime(29)
check_prime(1)