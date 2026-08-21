 # Tuples in python
 # immutble in nature the values inside the tuple cannot be changed
 
# a =("Monday", "Tuesday", 123,234)
 
# print(type(a)) 


# ls = [1,2,3,4,5]

# tup = tuple(ls) # changing the list into tuple

# print(type(tup))

# tup = tuple(a)

# print(tup.index("Tuesday")) # provides the index of element
# print(tup.count("Monday")) # provides the no. of times an element is repeated in tuple


# Unpacking a tuple


# def student():
#     return "Hulash" , 24 , "shahhulash@gmail.com"  # this info is stored as tuple by default

# info = student()

# name , age , mail = info  # this assign variable to each values returned from student() in order

# print(f"Name : {name}")
# print(f"Age : {age}")
# print(f"E-Mail : {mail}")


# # Sets in Python

# a = {2,3,4,5,6,7,8,9}

# print(type(a))


# a = {2,3,4,5,6,7,6,5,4,3,4,5,6,4,3,3,4,45,6,7,8,9}

# print(set(a))


# for i in a:
#     print(i)


# a = {10,20,30,40}

# a.add(50)
# a.discard(20)
# a.pop()

# print(a)

# functions in sets
s1 = {10,20,30,40,50}

s2 = {20,30,40,50,60,70}

s3 = {44,55}

# print(s1 - s2)   # gives s1 only
# print(s2 - s1)   # gives s2 only

# s2 -= s1
# print(s2)

# print(s1.difference(s2)) # give s1 only
# print(s1.intersection(s2))

# s1 &= s2   #gives the intersection
# print(s1)


# print(s3 <= s2)   # s3 is not a subset of s2 False
# print(s2 >= s3)   # superset checking  False

# print(s1.symmetric_difference(s2))


# print(s1 ^ s2)


# print(s1 | s2)  # union



# Dictionary in Python 

# vanilla python
dict = {1:20, 2:40, 3:40}

# print(dict[1])

# dict[4] = 45 # creatinga new value pair

# dict[2] = 44  # updating a key value that already exists

d = dict.fromkeys([4,5,6,7],50)

print(d)

print(d.get(5))