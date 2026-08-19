
# Class And Objects

# Types of Attributes

# 1 Instance attributes

# 2 class attributes


# class Dog:
#     count = 0  # Instance Attributes
    
#     def __init__(self, name: str, age: int ):
#     # Initializer or constructor
#      self.name = name   # Instance Attributes
#      self.age = age     # Instance Attributes
     
#      Dog.count += 1

# dog1 = Dog("Tommy", 4)
# dog2 = Dog("Kutta", 5)

# print(dog1)
# print(dog2)
# print(dog1.age)
# print(dog2.name)
# print(dog1.count)
# print(dog2.count)    


# # Types of Methods


# # 1 Instance Method
# # 2 Class Method
# # 3 Static Method

# class Person:
#     count = 0

#     def __init__(self, name: str, address: str = "Kathmandu"):
#         # Initializer / Constructor
#         self.name = name
#         self.address = address

#         Person.count += 1

#     # Instance method
#     def get_details(self):
#         print(f"I'm {self.name} from {self.address}")

#     # Class method
#     @classmethod
#     def get_count(cls):
#         return cls.count

#     # Static method
#     @staticmethod
#     def get_full_name(first, last):
#         return f"{first} {last}"


# student1 = Person("Hulash", "Kathmandu")

# student1.get_details()

# print("Number of persons:", Person.count)

# student2 = Person("Rahul", "Biratnagar")

# student2.get_details()

# print("Number of persons:", student2.get_count())

# print(Person.get_full_name("Hulash", "Shah"))



class Calculate:
    def __init__(self, name: str , physics: int , chemistry: int , math: int):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.math = math
    
    def total(self):
        
        return sum([self.physics, self.chemistry, self.math])
    
    def average(self):
    
      return  sum([self.physics, self.chemistry, self.math])/3
  
    def display(self):
        print(f"Total Marks : {self.total()}")
        print(f"Average Marks  : {self.average()}")
    
calc1 = Calculate("Hulash", 90,90,90)
calc1.display()



# Inherintance in Python

# Single Inheritance

class Animal:
    def __init__(self, name ,  age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"I'm {self.name}")
        
# class Cat(Animal):
#     ...     # or we can use pass when we don't want anything in class

class Cat(Animal):
    def __init__(self , name1, age1, color):
        super().__init__(name1, age1)
        self.color = color
        
    def details(self):
        print(f"{self.color} Cat : \n{self.name} \nAge: {self.age}")
    
cat = Cat("Luffy", 2, "Brown")

cat.intro()
cat.details()




# Multiple Inheritance

class Parent1:
    def func1(self):
        print("this is parent 1 ")
             
class Parent2:
    def func2(self):
        print("this is parent 2 ")
             
class Parent3:
    def func1(self):
        print("this is parent 3 ")

class Child(Parent3, Parent2, Parent1):  #DFS
    def func4(self):
        print("this is child funtion")
        
obj = Child()

obj.func4()
obj.func2()

obj.func1()   # latest func1() will be returned as the child goes from parent1 to parent3 so func1() in parent3 function will be returned.
    

# Multi-Level Inheritance

class A:
    def method_a(self):
     print(" This is method from class A")


class B(A):
    def method_b(self):
     print(" This is method from class B")


class C(B):
    def method_c(self): 
     print(" This is method from class C")
     
b = B()
c = C()
print(dir(c))


# Solving problem


# Designing a simple hierarchy of employees in a company
 
#     - The Person class stores basic details like name and age.
 
#     - The Employee class inherits from Person and adds an employee ID.
 
#     - The Manager class inherits from Employee and adds a department.
 
# Write these classes and implement a method get_details() in the Manager class that returns a string with name, age, employee ID, and department.
 


class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
class Employee(Person):
    def __init__(self, name1, age1, emp_id):
        super().__init__( name1, age1)
        self.emp_id = emp_id
        
class Manager(Employee):
    def __init__(self , name2, age2 , emp_id1, department):
        super().__init__( name2, age2, emp_id1)
        self.department = department
    
    def get_details(self):
        print(self.name, self.age, self.emp_id, self.department)
    
        
details = Manager("Hulash", 24 , 101 , "CSIT")

details.get_details()





