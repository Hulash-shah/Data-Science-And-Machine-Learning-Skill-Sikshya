# Exercise 1: Bug-Fixing (Float Precision & Mixed Division)
# Find and ﬁx the 2 bugs in this simple checkout calculator snippet so that it calculates the total with tax correctly and prints integer quantities safely.
# Goal: Calculate total price including tax, and display items per person
# item_price = 12.50
# quantity = "4"
# tax_rate = 0.08 # 8% tax

# Bug 1 occurs here when trying to calculate subtotal
# subtotal = item_price * quantity
# total_tax = subtotal * tax_rate
# grand_total = subtotal + total_tax
# num_people = 3

# Bug 2: We want cost_per_person to be an exact float, but items_per_person to be a whole number floor
# cost_per_person = grand_total / num_people
# items_per_person = quantity / num_people

# print(f"Grand Total: ${grand_total}")
# print(f"Items per person: {items_per_person}")



#solution

item_price = 12.50
quantity = "4"
tax_rate = 0.08 # 8% tax




# Bug 1 occurs here when trying to calculate subtotal
subtotal = item_price * int(quantity)
total_tax = subtotal * tax_rate
grand_total = subtotal + total_tax
num_people = 3

# Bug 2: We want cost_per_person to be an exact float, but items_per_person to be a whole number floor
cost_per_person = grand_total / num_people
items_per_person = int(quantity) // num_people

print(f"Grand Total: ${grand_total}")
print(f"Items per person: {items_per_person}")





# # Exercise 2: Code Completion (Operator Precedence & Floor Math)
# # Fill in the blanks ___ to make the assertions pass.
# # 1. Complete the formula for compound interest: A = P(1 + r/n)^(nt)
# principal = 1000
# rate = 0.05
# time = 2
# n_compounds = 12

# # Hint: Use parentheses carefully for precedence and the correct exponent operator
# amount = principal * (1 + rate / n_compounds) __ (n_compounds * time)

# # 2. Get the number of remaining hours after removing full days from a total
# total_hours = 130
# remaining_hours = total_hours ___ 24 # Complete with the correct operator

# # 3. Calculate full 7-day weeks in a total number of days
# total_days = 45
# full_weeks = total_days ___ 7 # Complete with integer division operator

# print(f"Amount: {round(amount, 2)}")
# print(f"Remaining Hours: {remaining_hours}")
# print(f"Full Weeks: {full_weeks}")

# # Expected: 1104.94
# # Expected: 10
# # Expected: 6

#solution:

# 1. Complete the formula for compound interest: A = P(1 + r/n)^(nt)
principal = 1000
rate = 0.05
time = 2
n_compounds = 12

# Hint: Use parentheses carefully for precedence and the correct exponent operator
amount = principal * (1 + rate / n_compounds) ** (n_compounds * time)

# 2. Get the number of remaining hours after removing full days from a total
total_hours = 130
remaining_hours = total_hours % 24 # Complete with the correct operator

# 3. Calculate full 7-day weeks in a total number of days
total_days = 45
full_weeks = total_days // 7 # Complete with integer division operator

print(f"Amount: {round(amount, 2)}")
print(f"Remaining Hours: {remaining_hours}")
print(f"Full Weeks: {full_weeks}")




# Exercise 3: Bug-Fixing (List Mutation & String Slicing)
# This script is supposed to clean up a list of usernames and format a display title, but it has 3 bugs. Find and ﬁx them.
# raw_title = "PYTHON programming course"

# # Bug 1: Strings are immutable, but the programmer tried to fix formatting in-place
# raw_title.strip()
# raw_title.title()
# print(f"Title: '{raw_title}'")

# # Expected: 'Python Programming Course'

# users = ["alice", "bob", "charlie"]
# # Bug 2: The programmer tried to copy the list, but both variables point to the same list!
# updated_users = users
# updated_users.append("david")
# print(f"Original users: {users}")
# print(f"Updated users: {updated_users}")


# # Expected: ['alice', 'bob', 'charlie']
# # Expected: ['alice', 'bob', 'charlie', 'david']
# # Bug 3: Reverse the title string using slicing
# # The programmer wrote step 1 instead of -1

# reversed_title = raw_title[::-1] # Hint: Look closely at why this isn't printing expected output if raw_title wasn't modified above!


# Solution:

# This script is supposed to clean up a list of usernames and format a display title, but it has 3 bugs. Find and ﬁx them.
raw_title = "PYTHON programming course"

# Bug 1: Strings are immutable, but the programmer tried to fix formatting in-place
print(raw_title.strip())
print(raw_title.title())

raw_title = raw_title.strip().title()
print(f"Title: '{raw_title}'")





users = ["alice", "bob", "charlie"]
# Bug 2: The programmer tried to copy the list, but both variables point to the same list!
 
updated_users = users.copy()  # used copy() to copy the elements of users to updated_users
updated_users.append("david")


# update_users = updated_users.append("david")


print(f"Original users: {users}")
print(f"Updated users: {updated_users}")

 # Bug 3: Reverse the title string using slicing
# # The programmer wrote step 1 instead of -1

reversed_title = raw_title[::-1] 
# Hint: Look closely at why this isn't printing expected output if raw_title wasn't modified above!

print(reversed_title)



# Exercise 4: Code Completion (String & List Manipulations)
# Fill in the blanks ___ to transform the user data correctly.

# Solution
# Given input string of comma-separated tags with irregular spacing
tags_input = " python , data-science, machine-learning "

# 1. Split the string into a list of strings by comma
raw_list = tags_input.split(",")

# 2. Extract only the first tag and clean surrounding whitespace
first_tag = raw_list[0].strip()

# 3. Replace hyphens with spaces in the second tag
second_tag_clean = raw_list[1].strip().replace("-", " ")

# 4. Create a new list combining the cleaned tags using list slicing and replacement
cleaned_tags = [first_tag, second_tag_clean]

# 5. Add the last tag (cleaned) to the end of cleaned_tags list
last_tag_clean = raw_list[-1].strip()
cleaned_tags.append(last_tag_clean)

print(cleaned_tags)
# Expected output: ['python', 'data science', 'machine-learning']