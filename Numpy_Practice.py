import numpy as np
from scipy import sparse

matrix_1 = np.mat(
    [
        [1, 7, 2, 7, 8, 9, 1],
        [1, 1, 1, 9, 1, 2, 2],
        [1, 2, 3, 4, 5, 5, 5],
        [4, 4, 4, 3, 2, 1, 0],
        [7, 8, 9, 7, 8, 9, 7],
    ]
)

matrix_2 = np.mat(
    [
        [1, 7, 2, 7, 8, 9, 1],
        [1, 1, 1, 9, 1, 2, 2],
        [1, 2, 3, 4, 5, 5, 5],
        [4, 4, 4, 3, 2, 1, 0],
        [7, 8, 9, 7, 8, 9, 7]
    ]
)

print("Dimension of a matrix", matrix_1.ndim)
print("Size of a matrix", matrix_1.size)
print("Shape of a matrix", matrix_1.shape)

# Sparse Matrix
sparse_matrix = sparse.csr_matrix(matrix_1)
print(sparse_matrix)

# Max of each column
print("Max of column : ", np.max(matrix_1, axis=0))
# Min of each column
print("Min of each column : ", np.min(matrix_1, axis=0))

# Convert the matrix to a different shape
matrix_1.reshape(7, 5)
print(matrix_1.reshape(7, 5))

# Convert the entire matrix to desire row and adjusted colimns
print(matrix_1.reshape(1, -1))
print(matrix_1.reshape(7, -1))

# Reshaping array into single
# print("Reshaping into a single array : ")
# print(matrix_1.reshape(5, -2))
# print("Reshaping into a single array : ")
# print(matrix_1.reshape(6, -1))

# Convert the entire matrix into a single row and possible columns
print(matrix_1.flatten())

# Transposition of a matrix
print("this is transposition")
print(matrix_1.transpose())

# Addition of 2 matrix
print(np.add(matrix_1, matrix_2))

# Subtract of 2 matrix
print(np.subtract(matrix_1, matrix_2))

# Multiplication of 2 matrix
print(np.multiply(matrix_1, matrix_2))
