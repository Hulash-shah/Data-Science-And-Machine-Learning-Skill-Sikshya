import numpy as np

a = np.random.randint(10, 50, size = (5,2,3), dtype = "int16")
print(a)
print(a.shape)
print(a.ndim)

print(a.dtype)

print(a.size)
print("\nReshape\n")
reshape = a.reshape(10,3)
reshape2 = a.reshape(2,5,3)

print(reshape)
print("\nReshape2 :\n")
print(reshape2)


flatten = a.flatten()  # a.ravel()
print(flatten)


sum = a.sum()
print("\nSum : \n",sum)

Column_Wise_Sum = a.sum(axis = 0)
print("\ncolumn Wise Sum :\n",Column_Wise_Sum)


Row_Wise_Sum = a.sum(axis = 1)
print("\nRow Wise Sum :\n",Row_Wise_Sum)


Diagonal_Sum = a.trace()  # diagonal sum

print("\nDiagonal Sum : \n",Diagonal_Sum)

Cumulative_Sum = a.cumsum(axis = 1)

print("\nCumulative Sum : \n",Cumulative_Sum)


product = a.prod(dtype = float)

print("\nProduct : \n",product)


Cumulative_Product = a.cumprod(axis = 1)
print("\nCumulative_PRoduct : \n",Cumulative_Product)

max_value_at_index = a.argmax(axis = 0)
print("\nMax Vallues at index : \n",max_value_at_index)

min_value_at_index = a.argmin(axis = 1)
print("\nMin Vlaues at index : \n",min_value_at_index)

clip = a.clip(max = 40 , min = 20)
print("\n Clip : \n", clip)

# Concatination or joining

arr1 = np.random.randint(1,100, size = (3,3))
arr2 = np.random.randint(1,100, size = (3,3))

print(arr1,arr2)

concat = np.concatenate([arr1,arr2], axis = 1) #hstack
concat2 = np.concatenate([arr1,arr2], axis = 0) #vstack
print("\nConcatination of arrays : \n",concat)
print("\nConcatination of arrays : \n",concat2)

vstack = np.vstack([arr1,arr2])
hstack = np.hstack([arr1,arr2])

print("\nVertical Stacking : \n",vstack)
print("\nHorizontal Stacking : \n",hstack)