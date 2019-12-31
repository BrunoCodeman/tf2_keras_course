from numpy.random import randint
from pandas import DataFrame

random_arr = randint(-100, 100, (5,4))
indexes = ["1st index", "2nd index", "3rd index", "4th index", "5th index"]
columns = ["Column 1", "Column 2", "Column 3", "Column 4", ]

my_df = DataFrame(random_arr,indexes,columns)

print(f"\nDataframe:\n {my_df}")

#print(f"Getting index 0: \n {my_df[0]}")

print(f"\nGetting column 1: \n{my_df['Column 1']}")

print(f"\nGetting column 1 and column 2: \n{my_df[['Column 1', 'Column 2']]}\n\n")

my_df["New Column"] = my_df["Column 1"] * my_df["Column 4"]
print(my_df)

#Deleting the new column.
my_df = my_df.drop("New Column", axis=1)

print(f"\nGetting 1st index: \n{my_df.loc['1st index']}")

print(f"\nGetting 1st and 2nd index: \n{my_df.loc[['1st index', '2nd index']]}")
print(f"\nGetting 1st and 2nd index from columns 2 and 4: \n{my_df.loc[['1st index', '2nd index'],['Column 2','Column 4']]}")


#Filtering Data
print(my_df[my_df["Column 1"] > 0])

#Filtering with two conditions
print(my_df[(my_df["Column 1"] > 0) & (my_df["Column 4"] > 1)])

##Other useful functions
#Turns the old index into a column
print(my_df.reset_index())

new_indexes = [f"New {i+1}" for i in range(5)]
my_df["New Column"] = new_indexes

#Drops the old index and set a new one
print(my_df.set_index("New Column"))

#Mean, std, and other useful data
my_df.describe()

#Info about values and data types
my_df.info()

#Info about data types
my_df.dtypes()
