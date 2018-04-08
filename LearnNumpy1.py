import numpy as np
#  This program differentiates between the time taken on operations perform on lists and numpy arrays
import time

SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()

result = [(x, y) for x, y in zip(L1, L2)]

print((time.time() - start) * 1000)

result1 = A1 + A2

print((time.time() - start) * 1000)



