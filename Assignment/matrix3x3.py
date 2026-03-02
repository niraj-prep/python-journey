#Array Matrix

import numpy as np

A = np.random.randint(1, 10, size=(3, 3))
B = np.random.randint(1, 10, size=(3, 3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Addition (A + B):")
print(A + B)

print("\nMatrix Multiplication (A x B):")
print(np.dot(A, B))