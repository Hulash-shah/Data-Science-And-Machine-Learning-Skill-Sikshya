

        
    # Abstraction in python
    
from abc import ABC, abstractmethod 
class Shape(ABC):
    def __init__(self, length, breadth, height = 0):
        self.l = length
        self.b = breadth
        self.h = height
    
    @abstractmethod
    def area(self):
        pass
    
    def volume(self):
        return "Not applicable for given shape"

    
class Rectangle(Shape):
    
    """
    Calculate Area And Volume of Rectangle
    """
    def area(self):
        return self.l * self.b
    
    def volume(self):
        return self.l * self.b *self.h
    
rect = Rectangle(50, 10, 20)

print(rect.area())
print(rect.volume())

import math

class Circle(Shape):
    def __init__(self, radius):
        self.r = radius
    
    def area(self):
        return math.pi *(self.r ** 2)
    
circle = Circle(4)

print(circle.area())


    
# SOlving Problem

# QQQQQ Practice Problem: The Cyber-Pet Nursery
# ### Create a Pet class with hidden energy stats:

# * Private Attribute: __energy (integer, default 50).

# * Attributes: name (string), children (list of Pet objects, defaults to empty list).

# * Methods:

#     * \_\_init\_\_(self, name, energy=50): Initializes name, sets initial __energy, and creates an empty children list.

#     * get_energy(): Returns the private __energy value.

#     * set_energy(value): Updates __energy, but enforcing a range of 0 to 100:

#         * If value > 100, set __energy = 100.

#         * If value < 0, set __energy = 0.

#     * add_child(child_pet): Appends another Pet instance to self.children.
 
 
#solution
 
class Pet:
    def __init__(self, name, energy=50):
        self.name = name
        self.__energy = energy
        self.children = []

    def get_energy(self):
        return self.__energy

    def set_energy(self, value):
        if value > 100:
            self.__energy = 100
        elif value < 0:
            self.__energy = 0
        else:
            self.__energy = value

    def add_child(self, child_pet):
        self.children.append(child_pet)


pet1 = Pet("Buddy")
pet2 = Pet("Max")

print(pet1.name)
print(pet1.get_energy())

pet1.set_energy(120)
print(pet1.get_energy())

pet2.set_energy(-20)
print(pet2.get_energy())

pet1.set_energy(80)
print(pet1.get_energy())

pet1.add_child(pet2)
print(pet1.children[0].name)
        
        

            
# ### Create a RoboPet class that inherits from Pet:

# * Attributes: Inherits name, __energy, and children.

# * Override Method:
#     * Override set_energy(value) so that robot pets get a 20% bonus to any energy set (e.g., setting energy to 50 actually gives 60 energy). It must still follow the max cap of 100.
    

class RoboPet(Pet):
    def set_energy(self, value):
        bonus_energy = value * 1.20
        super().set_energy(bonus_energy)


dis = RoboPet("Maxim")

dis.set_energy(20)

print(dis.get_energy())

dis.add_child(pet1)
dis.add_child(pet2)
dis.children
        
        
# QQQQ Write a standalone function get_total_family_energy(pet) . 
 
# * Base Case: If pet has no children, return its own energy (pet.get_energy()).
 
# * Recursive Case: Return the pet's own energy plus the sum of its children energy.


def get_total_family_energy(pet):
    total_energy = pet.get_energy()
    
    if pet.children:
       for each in pet.children:
           total_energy += each.get_energy()
    
        
    return total_energy
print(get_total_family_energy(dis))
 
        
        