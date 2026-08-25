import numpy as np
a = np.array(
    [
        [4,6,8],
        [1,2,4]
    ]
)
b = np.random.randint(1, 45, size = (2,3))
c = np.linspace((0,5), (60,100), num = 7)
print(b.dtype)
print(c.dtype)


# ----Arithmetic operations----

# a + b
sum = np.add(a,b)
print(sum)

# a - b
sub = np.subtract(a,b)
print(sub)

# a ** 2
power = np.pow(a,2)
print(power)

# a % b
quo, rem = np.divmod(b,a)
print(rem)

positive = np.positive(a)
print(positive)

# ----Trignometric operations----

cot = np.reciprocal(np.tan(b))


# Round operations

round = np.around(cot, 2)
print(round)
floor = np.floor(cot)
print(floor)

ceil = np.ceil(cot)
print(ceil)

# --- Matrix Operations ----

# Transpose

transpose = np.transpose(b)
print(transpose)

# Matrix Multiplication

mul = a @ transpose

# OR 
res= a.dot(transpose)

print(mul)
print(res)

# Trace [Diagonal Sum]

d_sum = np.trace(res)
print(d_sum)

# Rank

np.linalg.matrix_rank(a)

# Determinant

b = np.random.randint(1, 5, size = (3,3), dtype = int)
det_b = np.linalg.det(b)
print(det_b)
# Inverse

inv_b = np.linalg.inv(b)
print(inv_b)

# Question :
# Solve Equation : 4x + 2y = 8 , 5x + 3y = 9

A = np.array(
   [
        [4,2],
        [5,3]
   ]
)

B = np.array(
    [
        [8],
        [9]
    ]
)

A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)

# X = np.linalg.solve(A, B)

print(X)

print(A)
print(B)

print(A + B)

