
# complex data types

# list
# they are mutable i.e its value changes

list = [9, 4, 5, 6, 7, 8]   # index starts from 0 and if we want elements from backwards we have lastt elements -1 and move to left as -2 , -3 and so on

print(list, type(list))


print(list[0 : 3])
print(list[-3 : -1])
print(list[:])

for mark in list:
    print(mark)
    
list.append(50)   # appends the new value to the list
print(list)

# if we want to insert a new value at a particular desired index we will use insert() function as:

list.insert(0 , 51)
list.insert(1 , 15)
print(list)

print( 4 in list)  # checks whether the value 4 is present in the list or not and returns boolean value

list.clear()    # this function clears the list removes all the elements of list
print(list , len(list))  # returns [] , 0



# Tuples in python
# they are immutable i.e their value remains same and cannot be changed

marks = (2,3,4,5,6,5,4,7,8,9,0)

print(marks.count(4))  # count() funtion in tuple give the number of times an element is present in the tuple


print(marks.index(4))  # this returns the first index of 4 in the tuple


marks = 3,4,5,4,3,4,5,6,67,8  # we can also declare tuple without parenthesis () . This is also a tuple.

print(type(marks))

# but we use parenthesis normally to make code more readable so generally tuples are declared inside a parenthesis ()



# sets -> unique items collection

marks = {24,45,45,67,76,76,45,24}  # we use curly braces to declare a set . It is a unique collection of items

print(len(marks), marks)  #this returns only the len which includes unique elements i.e duplicates are filtered by sets 

# returns 4 as there are 4 unique elements in the sets 24,45,67,76


for mark in marks :
    print(mark)
    
    
# Dictionary => word : meaning   i.e it stores the info as { key : value } pairs


marks = { "Math": 90 , "Physics": 91 , "Chemistry" :80}  # stored as key : value pairs

print(marks, type(marks)) 

print(marks["Physics"]) # we donot need to use indexing as we can return the needed value by using key assigned to it.


# Dictionary is mutable 

marks["Physics"] = 95

print(marks)  # now the marks of physics will be {'Math': 90, 'Physics': 95, 'Chemistry': 80} <= something like this.


for key in marks:
    print(key , marks[key])  

# output 
# Math 90
# Physics 95
# Chemistry 80


# things to remenber 
# mutable datatypes are slower than immutable datatypes as their values can be changed. Tuples are faster than list.

# so when we want to store data that needs to be changed we store them in list but tha data those don't need changes are stored in  tuples.


# Practice exercise 5

#  QQQ given a list of roll numbers print only the unnique roll nubers.

roll_numbers = [2,4,5,3,4,2,5,4,3,3]

print(set(roll_numbers)) # output => {2, 3, 4, 5}


# QQQQ  Given employee records in the form of a list of tuples, where each tuple contains:

# (Employee ID, Employee Name, Salary)

# Ask the user to enter an Employee ID and search for that ID inside the employee records.

records = [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
]

ee_id = int(input("Enter the Emloyee ID: "))


for employee_id, employee_name, salary in records:
    if ee_id == employee_id :
           print("Employee Found!")
           print("Employee ID:", employee_id)
           print("Employee Name:", employee_name)
           print("Salary:", salary)
           break
else:
     print("Employee not found")
        

