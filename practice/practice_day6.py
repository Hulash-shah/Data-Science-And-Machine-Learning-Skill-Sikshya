
# # Leap year problem


# year = int(input("Enter a year:" ))

# if year % 100 == 0 and year % 400 == 0:
#     print(f"{year} is a leap year")

# elif year % 100 != 0 and year % 4 == 0:
#     print(f"{year} is a leap year")
    
# else:
#     print(f"{year} is not a leap year")
    
    
    
    
# a = "Students"

# for i in range(len(a)):
#     print(f"{i} : {a[i]}")
    
    
    
    
# n = int(input("tell me your number"))

# for i in range(n,0,-1):
#     print(i)


# n = int(input("which table u want? : "))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i} ")
    
    
# # factorial


# n = int(input("Enter a number"))

# f = 1 

# for i in range(1, n + 1):
#    f = f * i
   

# print(f)




# Even Odd Sum

n = int(input("Enter a number"))

evenSum = 0
oddSum = 0

for i in range(1, n + 1):
    if i % 2 == 0 :
        evenSum += i
    
    else:
        oddSum += i

print(evenSum)
print(oddSum)