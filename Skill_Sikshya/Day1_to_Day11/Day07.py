
# Inheritance 

# Hierarchichal Inheritance

# class Animal:
#     def __init__(self, name ,  age):
#         self.name = name
#         self.age = age
    
#     def intro(self):
#         print(f"I'm {self.name}")
        
# # class Cat(Animal):
# #     ...     # or we can use pass when we don't want anything in class

# class Cat(Animal):
#    def speaks(self):
#        return "Meow"
   
# class Dog(Animal):
#    def speaks(self):
#        return "woof"

# class Lion(Animal):
#    def speaks(self):
#        return "Roar"

# cat = Cat("Luffy", 3)
# dog = Dog("Tommy", 7)
# lion = Lion("Simba", 6)

# cat.intro()

# print(dog.speaks())

# print(lion.speaks())
   
   
# # Hybrid Inheritance


# class Animal:
#     def __init__(self, name ,  age):
#         self.name = name
#         self.age = age
    
#     def intro(self):
#         print(f"I'm {self.name}")
        
        
# class Mammal(Animal):
#     def __init__(base, name, age, fur = False):
#         super().__init__(name, age)
#         base.fur = fur
    
#     def birth(base):
#       print(f"{base.name} gives  birth to live ones")
      
#     def Birds(Animal):
#         def fly(self):
#             return f"{self.name} can fly"
        
# b = Mammal("Dog", 7)

# b.birth()


        

# Method Ovrloading in Python


# class Example:
#     def add(self , a, b, c = 0):
#         return a + b + c

# e = Example()

# print(e.add(2,4))
# print(e.add(4, 5, 6))
# print(e.add(2,4))
# print(e.add(2, 4, 5))
# print(e.add("1", "2","3"))


# class Calculate:
#     def add1(self, *args):
#         return sum(args)
    
# calc = Calculate()

# print(calc.add1(2,3,4,55))
     
    

# MethodOverriding in Python

# class Animal:
#     def sound(self):
#         print("making sound")

# class Dog(Animal):
#     def sound(self):
#         super().sound()  # super keyword
#         print("Dog makes woof sound")
        
# dog = Dog()

# dog.sound()



# Encapsulation in Python

# 1. Private
# 2. Protected
# 3. Public

class Example():
    def __init__(self):
        self.public =  1
        self.__private = 44
        self._protected = 34
        
    def public_method(self):
        print("Public method")
        
    def __private_method(self):
        print("Private Method")
        
    def _protected_method(self):
        print("Protected Method")    
        
        
e = Example()

e.public_method()
# e.__private_method()
e._protected_method()


class SunClass(Example):
    def get_public(self):
        print(self.public)
    
    def get__private(self):
            print(self.__private)
    
    def get_protected(self):
            print(self._protected)
            
s = SunClass()

s.get_public()



# Solving Problem


"""
The Secure Smart Home Automation System
You are building the core backend module for a smart home system. You need to design an architecture that secures sensitive settings while allowing developers to easily extend the system for custom devices.

The Problem Statement
   1. Create a parent class named SmartDevice with the following requirements:

   * A public attribute device_name.

      * A protected attribute _firmware_version initialized to "v1.0".

      * A private attribute __system_key initialized to "SECRET_KEY_123".

      * A public method get_device_status() that returns a string containing the device name and firmware version.

   2. Create a child class named SmartCamera that inherits from SmartDevice:

   * It should initialize with its own device_name and a new public attribute video_resolution (e.g., "1080p").

      * Inside SmartCamera, write a method named exploit_test() that tries to print/return all three inherited parent attributes directly (device_name, _firmware_version, and __system_key).

   3. Write an external testing block (outside the classes) to:

   * Instantiate a SmartCamera object named "Living Room Cam".

      * Call the camera's get_device_status() method to prove inheritance works.

      * Call exploit_test() and observe which attribute causes an AttributeError.

      * The Twist: Use Python's name mangling syntax to bypass the restriction and successfully print the __system_key from outside the class anyway.
 
 
 """

    
class SmartDevice:
    def __init__(self, name):
        self.name = name
        self._firmware_version = "V1.0"
        self.__system_key = "SECRET_KEY_123"
        
        
    def get_device_status(self):
        print(f"{ self.name} : {self._firmware_version}")
        
    
class SmartCamera(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
       
        self.video_resolution =  "4k"
        
    def exploit_test(self):
        print(f"Device Name:{self.name}\nVersion: {self._firmware_version}\nSystem_Key: self.__system_key ")
    
Living_Room_Cam = SmartCamera("Sony")    
        
Living_Room_Cam.get_device_status()
Living_Room_Cam.exploit_test()
print(Living_Room_Cam._SmartDevice__system_key)



        
    # Abstraction in python
    
from abc import ABC, abstractmethod 
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def volume(self):
        return "Not applicable for given shape"
    
shape = Shape()
    
    