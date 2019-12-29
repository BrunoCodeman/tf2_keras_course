#1) Import numpy
import numpy as np
import unittest
import numpy_exercices as npex

class NumpyExercicesTest(unittest.TestCase):

    #2)Create array with ten zeros
    def test_must_create_array_with_ten_zeros(self):
        expected = np.asarray([0 for i in range(0, 10)])
        result = npex.create_array_with_ten_zeros()
        
        self.assertTrue(np.array_equal(expected, result))
    
    #3)Create array with ten ones
    def test_must_create_array_with_ten_ones(self):
        expected = np.asarray([1 for i in range(0, 10)])
        result = npex.create_array_with_ten_ones()
        
        self.assertTrue(np.array_equal(expected, result))
        
    #4)Create array with ten fives
    def test_must_create_array_with_ten_fives(self):
        expected = np.asarray([5 for i in range(0, 10)])
        result = npex.create_array_with_ten_fives()

        self.assertTrue(np.array_equal(expected, result)) 

    #5)Create array of integers from 10 to 50
    def test_must_create_array_with_integers_from_ten_to_fifty(self):
        expected = np.asarray([i for i in range(10, 51)])
        result = npex.create_array_of_integers_from_ten_to_fifty()

        self.assertTrue(np.array_equal(expected, result))
        
    #6)Create array of even integers from 10 to 50
    def test_must_create_array_with_even_integers_from_ten_to_fifty(self):
        expected = np.asarray(range(10, 51, 2))
        result = npex.create_array_of_even_integers_from_ten_to_fifty()
                
        self.assertTrue(np.array_equal(expected, result))

    #7) Create 3x3 matrix with values ranging from 0 to 8
    def test_must_create_three_by_try_matrix_with_values_from_zero_to_eight(self):
        expected = np.array([ [0, 1, 2], [3, 4, 5], [6, 7, 8] ])
        result = npex.create_three_by_three_matrix_from_zero_to_eight()

        self.assertTrue(np.array_equal(expected, result))

    #8) Create a 3x3 identity matrix
    def test_must_create_three_by_three_identity_matrix(self):
        expected = np.array([ [1., 0., 0.], [0., 1., 0.], [0., 0., 1.] ])
        result = npex.create_three_by_three_identity_matrix()
        
        self.assertNotIn(False, result == expected)

    #9) Generate random number between 0 and 1 with numpy
    def test_must_generate_random_numpy_number(self):
        number = npex.random_numpy_number()
        
        self.assertGreater(number, 0)

    #10) Generate an array with 25 random numbers from 
    # a standard normal distribution
    def test_must_create_numbers_from_standard_normal_distribution(self):
        arr = npex.random_25_from_normal_distribution()
        
        self.assertIsNotNone(arr.any())
    
    #11) Create matrix 10x10 from 0 to 1 with 0.01 as step
    def test_must_create_specific_matrix(self):
        arr = [i/100 for i in range(1, 101,)]
        expected = np.asarray(arr).reshape(10, 10)
        result = npex.create_specific_matrix()
        
        self.assertTrue(np.array_equal(expected, result))

    #12) Create array of 20 linear spaced points between 0 and 1
    def test_must_create_linear_spaced_array_with_twenty_positions_between_zero_and_one(self):
        arr = npex.create_linear_spaced_array()
        
        self.assertIsNotNone(arr.all())

    #13) Reproduce the subset of the original matrix
    def test_must_create_other_matrix_from_given_matrix(self):
        to_exclude = [16, 21]
        expected = np.asarray([i for i in range(12, 26) if i not in to_exclude]).reshape(3, 4)
        result = npex.create_new_matrix_from_given_matrix()
        
        self.assertTrue(np.array_equal(expected, result))

    #14) Get the value 20 from the matrix
    def test_must_get_twenty_from_matrix(self):
        expected = 20
        result = npex.get_twenty_from_the_matrix()
        
        self.assertTrue(np.array_equal(expected, result))

    #15) Get array with 2, 7 and 12
    def test_must_get_three_values_from_the_array(self):
        expected = np.asarray([2 ,7, 12]).reshape(3, 1)
        result = npex.get_array_with_three_values()
        
        self.assertTrue(np.array_equal(expected, result))

    #16) Get last row
    def test_must_get_last_row(self):
        expected = np.asarray(range(21,26))
        result = npex.get_array_from_last_row()
        
        self.assertTrue(np.array_equal(expected, result))
    
    #17) Get array with the last two rows 
    def test_must_get_array_from_last_two_rows(self):
        expected = np.asarray(range(16,26)).reshape(2, 5)
        result = npex.get_array_from_last_two_rows()
        
        self.assertTrue(np.array_equal(expected, result))

    #18) Get the sum of all elements in useful_matrix
    def test_must_sum_all_elements_in_the_array(self):
        expected = 325
        result = npex.get_matrix_sum()
        
        self.assertEqual(expected, result)

    #19) Get the stardard deviation of useful_matrix
    def test_must_get_standard_deviation(self):
        expected = 7.211102550927978
        result = npex.get_standard_deviation()
        
        self.assertEqual(expected, result)

    #20) Get the sum of the columns
    def test_must_sum_columnds(self):
        expected = np.asarray([55, 60, 65, 70, 75])
        result = npex.sum_columns()

        self.assertTrue(np.array_equal(expected, result))
