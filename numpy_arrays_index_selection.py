import numpy as np

# Numpy arrays derived from other arrays
# are pointers to the original array

arr = np.arange(0,11)
# If it was a python normal list, 
# arr and arr2 would be two different 
# objects in memory. Here arr2 is a pointer to arr.
arr2 = arr[:]

# This is how we actually copy a numpy array to 
# another object without pointing to the original one.
arr3 = arr.copy()

# These are broadcastings, also not possible with 
# normal python arrays. Broadcast will obviously
# affect all the variables pointing to the array
arr[0:5] = 100
arr2[2:5] = 99

print(arr)
print(arr2)
print(arr3)

l1, l2, l3 = [1, 2, 3], [4, 5, 6], [7, 8, 9]
arr2d = np.array([ l1, l2, l3 ])

# The same as arr2d[1][2]
print(arr2d)
print(arr2d[1,2])

# gets all rows starting from row ONE of 
# all columns up to (but not including) TWO
print(arr2d[:2,1:])

# returns an array with values True of False for 
# each of the values in arr, according to the condition
bool_arr = arr < 99

# gets all the elements in arr
# that satisfy the conditions of bool_arr
print(arr[bool_arr])
