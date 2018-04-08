import numpy as np
# To perform linespacing we use '.linspace' function. Linespacing means printing
# values between two points divided equally.

a = np.linspace(1, 10, 5) # The syntax is like this '(start,stop,no. of values)'.

print(a)

# For finding the min, max, sum we use functions like below
# Let's define an array

a = np.array([(1, 2, 3), (4, 5, 6)])

# Now for sum

print(a.sum()) # Print the sum of the array
print(a.max()) # Print the max number present in the array
print(a.min()) # Print the min number present in the array


# To print sum of rows or columns
# We refer rows as axis 1 and columns as axis 0.
# To calculate we are using array 'a' from the top.

print(a.sum(axis=0))
print(a.sum(axis=1))

# To print the sqrt of the array 'a' we do like below

print(np.sqrt(a))

# To print the standard deviation we do like below

print(np.std(a))

# To do addition, subtract, multiply, divide. For that we have to define a new array let's take 'a' array only.
# To do follow below

b = np.array([(1, 2, 3), (4, 5, 6)])

print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division

