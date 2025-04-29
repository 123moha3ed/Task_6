import numpy as np

A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 4, 3, 2, 1])

addition = A + B
subtraction = A - B
multiplication = A * B
division = A / B

mean_A = np.mean(A)
max_A = np.max(A)
min_A = np.min(A)
dot_product = np.dot(A, B)
A_reshaped = A.reshape(5, 1)