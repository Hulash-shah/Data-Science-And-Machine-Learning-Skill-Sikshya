# Iterators in Python

# lst = [2,3,4,5,6]

# iterator = iter(lst)

# print(next(iterator))


# __iter__ and __next__() iterators

# class Fibonacci:
#     def __init__(self, limit = 10):
#         self.limit = limit
#         self.step = 0
#         self.current = 0
#         self.next = 1
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.step >= self.limit:
#             raise StopIteration
        
#         result = self.current
#         self.current, self.next = self.next, self.current + self.next
#         self.step += 1
        
#         return result
    
#     def __len__(self):
#         return self.limit
    
# fib = Fibonacci(15)

# # print(list(fib))

# for i in fib:
#     print(i)
   
# range_ite = range(4)
# print(range_ite)

# def is_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False

#     return True


# class PrimeNumbers:

#     def __init__(self, count):
#         self.count = count
#         self.current = 2
#         self.generated = 0

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.generated >= self.count:
#             raise StopIteration

#         while not is_prime(self.current):
#             self.current += 1

#         prime = self.current

#         self.current += 1
#         self.generated += 1

#         return prime


# obj = PrimeNumbers(10)

# for prime in obj:
#     print(prime)

# Checking prime numbers using iterators
      
def is_prime(n): 
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

class PrimeNumbers:
    def __init__(self, count):
        self.count = count
        self.current = 2
        self.generated = 0
        
    def __iter__(self):
        return self    
           
    def __next__(self):
        
        if self.generated >= self.count:
            raise StopIteration
        
        while not is_prime(self.current): 
            self.current += 1
            
        prime = self.current
        
        self.current += 1
        self.generated += 1
        
        return prime
        
obj = PrimeNumbers(10)

for prime in obj:
    print((prime))

        


