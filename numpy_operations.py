import numpy as np

arr = np.arange(1,11)
print(arr)
# Adds 5 to each array element. It's valid for all the 4 basic operations
print(arr +5)

#Squareroot for each array element
print(np.sqrt(arr))

#Log for each array element
print(np.log(arr))

# Array mean
print(arr.mean())

# Array variation
print(arr.var())

#Standard Deviation
print(arr.std())

arr2d = np.arange(0,25).reshape(5,5)
print(arr2d)

#Sum the columns
print(arr2d.sum(axis=0))

#Sum the rows
print(arr2d.sum(axis=1))