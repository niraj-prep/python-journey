#Matrix Operation (5x3) | (3x2) | (5x2)

import numpy as np

print("Enter elements of 5x3 matrix row by row:")
A = []
for i in range(5):
    row = list(map(int, input(f"Row {i+1} (3 values): ").split()))
    A.append(row)

print("\nEnter elements of 3x2 matrix row by row:")
B = []
for i in range(3):
    row = list(map(int, input(f"Row {i+1} (2 values): ").split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

product = np.dot(A, B)

print("\nMatrix A (5x3):")
print(A)

print("\nMatrix B (3x2):")
print(B)

print("\nProduct Matrix (5x2):")
print(product)