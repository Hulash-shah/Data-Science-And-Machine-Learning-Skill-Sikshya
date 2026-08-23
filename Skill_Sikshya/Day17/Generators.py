# Generators in Python

# def number_generator(start, end):
#     for num in range(start, end + 1):
#         yield num
        
# gen = number_generator(5,80)
# print(gen)

# print(next(gen))


def prime_generator():
    n = 1
    while True:
        n += 1
        if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)):
            yield n


gen = prime_generator()
first_10 = [next(gen) for _ in range(10)]
print(first_10)

def is_prime(n): 
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def prime_generator(limit = 10):
    count , start = 1, 1
    
    while count <= limit:
        start += 1
        if is_prime(start):
            count += 1
            yield start
        
obj = prime_generator(6)

print(list(obj))
    