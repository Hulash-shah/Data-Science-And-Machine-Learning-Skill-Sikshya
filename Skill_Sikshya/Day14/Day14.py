# Solving Questions

# filter prime numbers from the given list

test_numbers = [
    -10, -1, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 15, 17, 19, 21, 25,
    27, 47,49, 79, 97, 100, 523, 527, 1000, 7919, 10000, 104729, 1000000
]

for num in test_numbers:

    count = 0
    
    for i in range(1, num + 1):
       
        if num % i == 0:
            count += 1
    if count == 2:
       prime_numbers = list(f"{num}")

print(prime_numbers)


# E

   
    
    

        


    

   

