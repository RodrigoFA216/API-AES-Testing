import numpy as np

A = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

a = 0

for element in A:
    for i in element:
        a += i

print(a / A.shape[0])
