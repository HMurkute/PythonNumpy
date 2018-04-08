import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])

print(a.ndim)  # Gives the dimension of the array.
print(a.itemsize)  # Gives the size occupied by each element in bytes.
print(a.dtype)  # Gives the data type present in that array.
print(a.size)  # Gives the size of the array
print(a.shape) # Gives the shape of the array. The result of this will come (2,3) because we defined 'a' that way.
# (2,3) means 2 rows and 3 columns.


# For reshaping of an array. We are using same value of 'a'.
# Here 'a' is of 2 rows and 3 columns. By reshaping we can manipulate the rows and columns of that array.
# For reshaping, we have to type the below reshape command. I put into comments for testing the command that is below the shape command

# a = a.reshape(3,2)

# print(a)
# For printing particular element of that array. The below command of printing 'a[0,2]' prints the element present at
# 1st row and 3rd column. Indexing in python starts at 0. So that's why [0,2].
print(a[0,2])

# If we want to print multiple columns or rows we use':' . Let's see how

print(a[0:,2]) # This will print the 1st and 2nd row and 3rd column.
