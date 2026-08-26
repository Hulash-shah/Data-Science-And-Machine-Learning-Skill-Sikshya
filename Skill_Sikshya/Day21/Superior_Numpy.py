# import time
# import numpy as np

# a = np.random.rand(90_000_000)
# b = np.random.rand(90_000_000)

# using core python
import time
import random

a = [random.random() for _ in range(90_000_000)]
b = [random.random() for _ in range(90_000_000)]

start = time.time()

c = []

for i in range(len(a)):
    c.append(a[i] * b[i])

end = time.time()

print("Time taken:", end - start) 
# using list comprehension
# st = time.time()
# res = [num1 * num2 for num1, num2 in zip(list)]
# end = time.time()


# using Numpy

# import time
# import numpy as np

# a = np.random.rand(90_000_000)
# b = np.random.rand(90_000_000)

# start = time.time()

# c = a * b

# end = time.time()

# print("Time taken:", end - start)