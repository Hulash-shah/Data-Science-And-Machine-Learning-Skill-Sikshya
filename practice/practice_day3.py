# Learning about loops

# range()

# range(5)  # returns values from 0 to 4 .

# range ( 1 ,  8)  # returns values from 1 to 7 

# while loop

# counter = 1
# while counter <=5:
#     print(counter)
#     counter +=1
# print("end of code")


# counter = 1
# while counter <=5:
#     print("Hulash")
#     counter +=1
# print("end of code")


# i = 1
# while i <= 5:
#     print(i * "*")
#     i += 1
# print("end of code")


# i = 5
# while i > 0:
#     print(i * "*")
#     i -= 1
# print("end of code")


# for loops

# nums = range(5)
# for i in nums:
#     print("Hulash")
    

# for i in range(1, 6):
#     print(i)


# for i in range(1, 21):
#     if i % 2 == 0:
#         print(f"{i} is an even number")
#     else:
#         print(f"{i} is not an even number")


# for i in range( 2 , 21 , 2):  # we can pass 3 values in range() function i.e ranfe( start , end , step)
#      print(i)



# multiples of 3 in the range( 1 , 50) but stop when 21


# for i in range( 1,  51):
#    if i % 3 == 0 and i <= 21:
#        print(i)    
# i += 1



# break and continue
# for i in range(1, 51):
#     if i == 21:
#         break
#     if i % 3 == 0:
#         print(i)
# print("out of loop")

# for i in range(1, 51):
#     if i == 21:
#         continue
#     if i % 3 == 0:
#         print(i)
# print("out of loop")




# practice exercise 4


# print odd numbers from 1 to 20

# for i in range(1 , 21):
#     if i % 2 != 0:
#         print(i)




# table of 57 


# for i in range( 1, 11):
#     print( i * 57 )


# multiples of 3 in range(1 to 50 ) skip 15

# for i in range(1, 51):
#     if i == 15:
#         continue
#     if i % 3 == 0:
#         print(i)
    

# input two number and print first number divisible by both numbers between 1 to 1000
a = int(input("enter a number"))
b = int(input("enter another number"))

for i in range( 1, 1001):
    if i % a == 0 and i % b == 0:
        print(i)
        break


 