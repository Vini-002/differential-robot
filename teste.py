import numpy as np

a = np.array([[[1,2], [3, 4], [5, 6]], [[4, 6], [7, 8], [9, 10]]])

b = np.reshape(a, (6, 2))

print(b)
