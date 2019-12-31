from numpy import array
from pandas import Series

my_list = [1, 2, 3, 4 ,5]
np_arr = array(my_list)
my_labels = ["label 1", "label 2", "label 3", "label 4", "label 5" ]
my_dict = {"label 1": 1, "label 2": 2, "label 3": 3, "label 4": 4, "label 5": 15}

#Data and lables from normal python lists
list_series = Series(my_list, my_labels)
print(f" \n \n=== list series === \n {list_series} \n")

#Data from numpy, labels from normal python lists
nparray_series = Series(my_list, my_labels)
print(f"=== nparray series === \n {nparray_series} \n")

#Converts a dictionary into a pandas Series
dict_series = Series(my_list, my_labels)
print(f"=== dict series === \n {dict_series} \n")