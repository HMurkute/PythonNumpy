import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)


y = np.sin(x) # For cos replace 'sin' with 'cos' or 'tan'

plt.plot(x, y)

plt.show()

# For exponential function we do like below. But first we have to define an array

ar = np.array([1, 2, 3]) # The exponential funciton diplays the array as taking the elements in array as their powers

print(np.exp(ar))
# For logarithm do as below

print(np.log(ar)) # This print the natural logarithm i.e to base e.
print(np.log10(ar)) # This prints the log to base 10.
