import numpy as np

#optional parameter: step
array_with_ten_elements = np.arange(0,10) 
print(array_with_ten_elements)

#optional parameter: dtype(i.e integer in place of the default float type)
array_of_3_float_zeros = np.zeros(3)
print(array_of_3_float_zeros)

# Four rows and 10 columns. np.ones 
other_array_of_zeros = np.zeros((4,10)) 
print(other_array_of_zeros)

#arrays of 41 spaced numbers between 0 and 20
linspace_arr = np.linspace(0,20,41)
print(linspace_arr)

#Return a 2-D array with ones on the diagonal and zeros elsewhere.
diagonal_arr = np.eye(6)
print(diagonal_arr)

#Generate the same 4 numbers always
np.random.seed(42)
rand_array = np.random.rand(4)
print(rand_array)

#Reshape the array. Does not affect the original array
arr = np.arange(25)
print("\noriginal array\n")
print(arr)
to_reshape = np.random.rand(0,50, 10)
reshaped_arr = arr.reshape(5,5)
print("\nreshaped array\n")
print(reshaped_arr)

try:
    print("\ntrying to reshape the array into 4x7\n")
    arr.reshape(4,7)

except Exception as ex:
    #Can't reshape because 25 elements can't fit on an 4x7 array
    print(f"Exception - {ex}")

finally:
    
    random_array = np.arange(5, 40, 3, dtype=int)
    print(f"\nrandom_array: {random_array}")
    
    #max value on array
    _max = random_array.max()
    print(f"\nmax value on random_array: {_max}")

    #index of max value on array
    _argmax = random_array.argmax()

    print(f"\nindex of max value on random_array: {_argmax}")
    #min value on array

    _min = random_array.min()
    print(f"\nmin value on random_array: {_min}")

    #index of min value on array
    _argmin = random_array.argmin()
    print(f"\nindex of min value on random_array: {_argmin}")
