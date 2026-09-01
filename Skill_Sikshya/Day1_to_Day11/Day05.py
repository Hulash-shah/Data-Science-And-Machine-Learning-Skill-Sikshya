
# map() , filter() , reduce()

# def get_cube(*num):
#     return num **3


# ls = [ 1, 2,3, 4,4,6]

# map_obj = map(get_cube , ls) # generative approach

# # print(map_obj)

# list(map_obj)


 # map()  and filter() funtion
# def get_cube(num):
#     return num ** 3

# ls = [1, 2, 3, 4, 4, 6]

# map_obj = map(get_cube, ls)

# print(list(map_obj))



# filter_obj = filter(lambda num: num % 2 == 0 , ls)
# print(list(filter_obj))


# filter_obj = filter(lambda num: num % 2 != 0 , ls)
# print(list(filter_obj))


# reduce() funtion

# from functools import reduce

# def add(x, y):
#     return x + y

# my_list = [1,3,4,5,6,7,89,3]


# res = reduce( add, my_list)
# print(res)

# list_merge = [[1,2,3], [4,5,6], [5,6,7,8]]

# result = reduce(add , list_merge)
# print(result)



# Recursive Function



# def fib(n):
#     # Base Case
#     for n in cache:
        
#      if n == 0 :
#         return 0
#      elif n == 1:
#         return 1
#      else:
#         # Recursive case
#       return fib(n-1) + fib(n-2)
# print(fib(8))
# print(fib(100))
        
        
# Memoizing the Recursive Algorithm
# As you saw in the code above, the Fibonacci function calls itself several times with the same input. Instead of a new call every time, you can store the results of
# previous calls in something like a memory cache. You can use a Python list to store the results of previous computations. This technique is called memoization.

# cache = { 0 : 0, 1 : 1}

# def fib(n):
#     # Base Case
#     if n in cache:
#         return cache[n]
#     else:
#         # Recursive case
#         res = fib(n-1) + fib(n-2)
#         cache[n] = res
#         return res
# print(fib(255))



# Factorial of 5 ,
# 4! * 5 3! * 4 * 5 2! * 3 * 4 * 5 1! * 2 * 3 * 4 * 5

cache = [1,1]

def factorial(n):
    # Base case
    if n < len(cache):
        return cache[n]
        
    else:
        res =  factorial(n-1) * n
        cache.append(res)
        return res
print(factorial(14))