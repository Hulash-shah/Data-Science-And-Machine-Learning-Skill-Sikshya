# PropertyDecorstor


# Getter

# class Person:
#     def __init__(self, name):
#         self.full_name = name
     
#     @property            # when we use this now the name method changes to getter attribute.So, we can now run this as an attribute.
#     def name(self):
#         print("Getting Name")
#         return self.full_name
    
# obj = Person("Hulash")
# print(obj.name)         # calling as an attribute

# import uuid

# class Person:
#     def __init__(self, name):
#         self.__full_name = name
     
#     @property            # when we use this now the name method changes to getter attribute.So, we can now run this as an attribute.
#     def user_id(self):
#         print("Getting Name")
#         return f" {self.__full_name[-5 :]}_{str(uuid.uuid1())[:8]}"
    
# obj = Person("Hulash")
# print(obj.user_id)    



# Setter

class Person:
    def __init__(self, name):
        self.full_name = name
     
    @property            # when we use this now the name method changes to getter attribute.So, we can now run this as an attribute.
    def name(self):
        print("Getting Name")
        return self.full_name
    
    @name.setter
    def name(self, value):
        print("Getting Name")
        self.full_name = value
        
    
obj = Person("Hulash")
print(obj.name)         # calling as an attribute


Person.name = "Hulash Shah"
print(obj.name)


# Deleter

class Person:
    def __init__(self, name):
        self.__full_name = name
     
    @property            # when we use this now the name method changes to getter attribute.So, we can now run this as an attribute.
    def name(self):
        print("Getting Name")
        return self.__full_name
    
    @name.setter
    def name(self, value):
        print("Getting Name")
        self.__full_name = value
        
   
    @name.deleter
    def name(self):
        print("Deleting Name")
        self.__full_name = ""
            
obj = Person("Hulash")
print(obj.name)         # calling as an attribute

del obj.name

# print(obj.name)