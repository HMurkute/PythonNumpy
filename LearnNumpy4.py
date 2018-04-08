import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])
b = np.array([(1, 2, 3), (4, 5, 6)])
# If we want to stack the arrays horizontally or vertically we use functions like below mentioned,

print(np.vstack((a,b))) # Stack vertically
print(np.hstack((a,b))) # Stack horizontally



print(a.flatten())
print(a.flatten('F')) # We use F for column wise

# Another way  If we want to convert the array into one row we do like below

print(a.ravel())
