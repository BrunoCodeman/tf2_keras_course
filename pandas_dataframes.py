from numpy.random import randint
from pandas import DataFrame

random_arr = randint(-100, 100, (5,4))
indexes = ["1st index", "2nd index", "3rd index", "4th index", "5th index",]
columns = ["Column 1", "Column 2", "Column 3", "Column 4", ]

my_dataframe = DataFrame(random_arr,indexes,columns)

print(f"\nDataframe:\n {my_dataframe}")

#print(f"Getting index 0: \n {my_dataframe[0]}")

print(f"\nGetting column 1: \n{my_dataframe['Column 1']}")

print(f"\nGetting column 1 and column 2: \n{my_dataframe[['Column 1', 'Column 2']]}\n\n")

my_dataframe["New Column"] = my_dataframe["Column 1"] * my_dataframe["Column 4"]
print(my_dataframe)

#Deleting the new column.
my_dataframe = my_dataframe.drop("New Column", axis=1)

print(f"\nGetting 1st index: \n{my_dataframe.loc['1st index']}")

print(f"\nGetting 1st and 2nd index: \n{my_dataframe.loc[['1st index', '2nd index']]}")
print(f"\nGetting 1st and 2nd index from columns 2 and 4: \n{my_dataframe.loc[['1st index', '2nd index'],['Column 2','Column 4']]}")
