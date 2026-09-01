

# FUNCTIONS IN PYTHON


print(4,5, sep ="+", end = "\n")

age = int(input("Enter your age \n"))

type(age)


type(4!=2)


isinstance(print("hulash"), str)



len("Hulash")


Bool_list = [False , True, False ,False , True, True]
all(Bool_list)
any(Bool_list)


Bool_list = ["", "ram"]
all(Bool_list)

Bool_list = ["", "ram"]
any(Bool_list)




sum([1,5,7])


min(min([1,5,7]),max([1,5,7]))






file = open("/bin/Hulash.txt", mode='r')

file = open("/bin/Hulash.txt", mode='w')
file.write("This my first text in the file \n")

file.close()

#CONTEXT MANAGER


with open("/bin/Hulash.txt", mode = 'r+') as file:
  print(file.read())
  file.write("I am preparing for AI/Ml \n")
  print(file.read())

print("closed")



ls = [1,1,3,4]
ls.extend("Hulash")
ls



print(dir(2.0))



f = 4.5
f.is_integer()


f = 4.0000
f.is_integer()




#  enumerate() function


ls =["a","b","c"]
res = enumerate(ls)
print(res)


ls = ["a","b","c"]
res = enumerate(ls)
list(res)



ls = ["a","b","c"]
for i, name in enumerate(ls , start = 1):
  print(f"{name} - Roll No. {i}")
  
  
  
  
# zip() funtion
  
name = ["Hulash" , "Bhijan"]
score = [99 , 56]
section = ["A" , "B" , "C"]
zipped = list(zip(name , score ,section))
zipped
for a, b, c in zipped:
  print (a, b, c)
  
  
# eval() funtion

script = "1 + 3"
eval(script)

script = "1+2+3+4+5+6+7+8+9"
eval(script)




# practice questions


number = 18
for i in range(2, number):
  if number % i == 0:
    print(f"{number}  is not a prime number")
  break
else:
  print(f"{number} is a prime number")
  
  
  
x = 10
while x > 0:
  x -= 3
  if x == 4:
   break
else:
  x = -1
print(x)

sum
(list
  (zip
  ([1,2,3],[10,20]))
  [1])



#class task

# Python
# Input matrix:
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
# Expected Output: [4, 16, 36, 64]
# Your code here:
squared_evens = [...]




# solution:

squared_evens = []
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
for items in matrix:
  for num in items:
       if num % 2 == 0:
           squared_evens.append(num**2)
print(squared_evens)



numbers =[1,2,3,4,5]
while numbers:
  value = numbers.pop(0)
  if value % 2 == 0:
      continue
  print(value , end=" ")



# slicing

numbers = [ 2, 4, 6, 7, 8, 5, 4]

# numbers [ start : end : jump]
numbers [3 : 6 : 1]

name = "Hulash"
name [4 :  : -1]


fruit = "Pineapple"
fruit  [1 : : 2]

# PYTHON USERDEFINED FUNCTIONS

def calculate_sum( num1, num2 ) :
   result = num1 + num2
   return result


res = calculate_sum(10,20)
print(res)

res  = calculate_sum([10,20,30], [40,50,60])
print(res)


# TYPE HINTING

def calculate_sum(
     num1: int,
     num2: int ) -> int :

   result = num1 + num2
   return result


res = calculate_sum(10,20)
print(res)



# METHONDS IN PYTHON


def greet ( name : str , greeting : str = "Morning"):
  print(f"Good {greeting} , {name} ")

