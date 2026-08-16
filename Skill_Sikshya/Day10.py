
# #
# # transactions = [
# #     {"id": 101, "amount": 250.0, "status": "completed", "currency": "USD"},
# #     {"id": 102, "amount": 0.0,   "status": "pending",   "currency": "USD"},
# #     {"id": 103, "amount": 180.5, "status": "completed", "currency": "USD"},
# #     {"id": 104, "amount": 45.0,  "status": "refunded",  "currency": "USD"},
# #     {"id": 105, "amount": 500.0, "status": "completed", "currency": "USD"},
# # ]


# # res = []

# # for transaction in transactions:
# #     if transaction.get("status") == "completed":
# #         res.append(transaction.get("status"))
# # print(res)


# # Magic Methods in Python

# # _init_ => intitializes an object of a class when created
# # _str_
# # _repr_
# # _len_
# # _call_



# #__init__

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# # __str__

#     def __str__(self):
#         return f"{self.name} / {self.age}"
    

# # __repr__

#     def __repr__(self):
#         return f"Person: {self.name}, {self.age}"
    
# # __len__

#     def __len__(self):
#         return (self.age)

# # __call__

#     def __call__(self, gender = "Male"):
#         return f"{self.name} is a {gender}"
# person = Person("Hulash", 24)

# print(person)

# print(repr(person))

# print(len(person))


# print(person("Male"))   # call



# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __str__(self):
#         return f"({self.x}, {self.y})"
    
#     def __len__(self):
#         return "Run this part" 
    
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
#     def __mul__(self, other):
#         return Point(self.x * other.x, self.y * other.y)
    
    
# p1 = Point(5, 4)

# p2 = Point(6, 7)

# res = p1 + p2

# res2 = p1 * p2
# print(res)
# print(res2)




# class Coordinate:
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def  check(self):
        
#         if self.x > 0 and self.y > 0:
#             print(" first quadrant")
            
#         elif self.x < 0 and self.y > 0:
#             print("second quarant")
        
#         elif self.x < 0 and self.y < 0:
#             print("third quarant")
        
#         elif self.x > 0 and self.y < 0:
#             print("fourth quarant")
#         elif self.x == 0 or self.y == 0:
#             print("On Axis")
            
# cal = Coordinate(0, 0)

# print(cal.check())



# # Alternative
# class Check:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def calc(self):
#         if self.x == 0 or self.y == 0:
#             return "On an axis"

#         quadrant_mapping = {
#             (True, True): "first",
#             (False, True): "second",
#             (False, False): "third",
#             (True, False): "fourth"
#         }

#         return quadrant_mapping.get((self.x > 0, self.y > 0))


# c = Check(6,7)

# print(c.calc())



# # Python OS Module

import os

print(os.getcwd())

# os.mkdir("test")


os.chdir("test")

if os.path.exists("test"):
    pass
else:
    print("file doesnot exist")