#1) Import numpy
import numpy as np

useful_matrix = np.arange(1, 26).reshape(5, 5)
#2)Create array with ten zeros
def create_array_with_ten_zeros():
    return np.zeros(10)

#3)Create array with ten ones
def create_array_with_ten_ones():
    return np.ones(10)

#4)Create array with ten fives
def create_array_with_ten_fives():
    return np.ones(10) * 5

#5)Create array of integers from 10 to 50
def create_array_of_integers_from_ten_to_fifty():
    return np.arange(10, 51)

#6)Create array of even integers from 10 to 50
def create_array_of_even_integers_from_ten_to_fifty():
    return np.arange(10, 51, 2)
    
#7) Create 3x3 matrix with values ranging from 0 to 8
def create_three_by_three_matrix_from_zero_to_eight():
    return np.arange(0,9).reshape(3, 3)

#8) Create a 3x3 identity matrix
def create_three_by_three_identity_matrix():
    return np.eye(3)

#9) Generate random number between 0 and 1 with numpy
def random_numpy_number():
    return np.random.rand()

#10) Generate an array with 25 random numbers from 
# a standard normal distribution
def random_25_from_normal_distribution():
    return np.random.randn(25)

#11) Create matrix 10x10 from 0 to 1 with 0.01 as step
def create_specific_matrix():
    arr = np.arange(1,101)/100
    return arr.reshape(10, 10)

#12) Create array of 20 linear spaced points between 0 and 1
def create_linear_spaced_array():
    return np.linspace(start=0, stop=1, num=20)

#13) Reproduce the subset of the original matrix
def create_new_matrix_from_given_matrix():
    return useful_matrix[2:, 1:]

#14) Get the value 20 from the matrix
def get_twenty_from_the_matrix():
    return useful_matrix[3, 4]

#15) Get array with 2, 7 and 12
def get_array_with_three_values():
    return useful_matrix[:3,1:2]

#16) Get last row
def get_array_from_last_row():
    return useful_matrix[4]


 #17) Get array with the last two rows 
def get_array_from_last_two_rows():
    return useful_matrix[3:]
