
# Date-Time Modules in Python

import datetime

# birth_date = datetime.date(2002, 6, 5)

# print(birth_date)

# today = datetime.date.today()
# print(today)
# # Arthmetic Operation
# age = today - birth_date

# print(age)

# NST = datetime.timezone(datetime.timedelta(hours = 5, minutes = 43))
# print(today > birth_date)


# print(datetime.date.fromtimestamp(1786343544))


# print(datetime.date.fromisoformat("1998-06-14"))

# # Day 12

# print(today.strftime("%a - %d %b, %Y")) # string format time (strftime)


# dt = datetime.datetime(2026, 8, 18, 7, 18, 50 , tzinfo = NST)
# print(dt)


# today =datetime.datetime.now()
# print(today)


# # print(today - dt)


# year_5 = datetime.timedelta(days = 5 * 365)

# print((today + year_5))
# NST = datetime.timezone(datetime.timedelta(hours = 5, minutes = 43))



# # time module

# import time

# print(time.time())  # current time in seconds

# print(time.ctime()) # current time

# print(time.localtime())

# print(time.gmtime())

# print(time.strftime("%H hour, %M minustes, %S seconds"))

# # sleep


# print("Loading...")

# time.sleep(5)
# print("completed")  # loads after 5 seconds


# start = time.time()

# print("Funtion Started")

# time.sleep(3)

# print("Function Ended")

# end = time.time()

# print((end - start))


# Packages in Python

"""
In Python, a package is a way of organizing related modules into a directory hierarchy. A package helps structure large programs, 
improves code reusability, and avoids naming conflicts.

What is a Package?
A module is a single Python file (.py) containing functions, classes, or variables.
A package is a directory that contains one or more modules and may contain sub-packages.
Package Structure

Example:

mypackage/
│
├── __init__.py
├── math_utils.py
├── string_utils.py
└── subpackage/
    ├── __init__.py
    └── helper.py
    
__init__.py: Marks the directory as a Python package (optional in Python 3.3+, but still commonly used).

math_utils.py and string_utils.py: Modules inside the package.

subpackage: A package inside another package.
"""




# try:
#     from sklearn.preprocessing import OneHotEncoder  # type: ignore[import-not-found]
# except ImportError:
#     OneHotEncoder = None

# from my_calculator.multi_numbers import Product_of_numbers

# Product_of_numbers(4,5)



# pass check


# PassCheck Class
# pass_check = PassCheck("hello23456")
# pass_check() -> Strong or Weak Password
 
# Strong:

# * length >= 8

# * alpha + numerical
 
class Passcheck:

    def __init__(self, password):
        self.password = password

    def pass_check(self):
        count_alpha = 0
        count_num = 0

        for i in self.password:
            if i.isdigit():
                count_num += 1
            elif i.isalpha():
                count_alpha += 1

        if len(self.password) >= 8 and count_num >= 1 and count_alpha >= 1:
            print("strong pass")
        else:
            print("weak pass")


check = Passcheck("dfhuidfhweru4546")

check.pass_check()