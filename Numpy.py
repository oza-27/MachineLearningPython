# # Python program to demonstrate
# # basic array characteristics
# import numpy as np
#
# # Creating array object
# arr = np.array([[1, 2, 3], [4, 2, 5]])
#
# # Printing type of arr object
# print("Array is of type: ", type(arr))
#
# # Printing array dimensions (axes)
# print("No. of dimensions: ", arr.ndim)
#
# # Printing shape of array
# print("Shape of array: ", arr.shape)
#
# # Printing size (total number of elements) of array
# print("Size of array: ", arr.size)
#
# # Printing type of elements in array
# print("Array stores elements of type: ", arr.dtype)
import numpy as np
# from scipy import sparse
matrix_1 = np.mat(
    [
        [1, 7, 2, 7, 8, 9, 1],
        [1, 1, 1, 9, 1, 2, 2],
        [1, 2, 3, 4, 5, 5, 5],
        [4, 4, 4, 3, 2, 1, 0],
        [7, 8, 9, 7, 8, 9, 7]
    ]
)
matrix_2 = np.mat(
    [
        [2, 8, 3, 8, 9, 10, 2],
        [2, 2, 2, 10, 2, 3, 3],
        [2, 3, 4, 6, 6, 6, 6],
        [5, 5, 5, 4, 3, 2, 1],
        [8, 9, 10, 8, 9, 10, 8]
    ]
)
result = np.mat(
    [

        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
)
# Sparse Matrix = Finds out the non-zero numbers in matrix
# sparse_matrix = sparse.csr_matrix(matrix)
# print(sparse_matrix)
# This both will print max of each row and column
# print(np.max(matrix, axis=0))
# print(np.max(matrix, axis=1))

print("-----------------------------------------------------")
# Convert the matrix to a different shape
matrix_1.reshape(7, 5)
print(matrix_1.reshape(7, 5))

print("-----------------------------------------------------")

# Convert the entire matrix to desire row and adjusted columns
print(matrix_1.reshape(1, -1))
print(matrix_1.reshape(7, -1))
print("-----------------------------------------------------")
# Convert the entire matrix to a single row and possible columns
print("This is an example of the entire matrix to a single row and possible columns")
print(matrix_1.flatten())

print("-----------------------------------------------------")

# Transpose of a matrix
print("This is an example of matrix transposition")
print(matrix_1.transpose())

print("-----------------------------------------------------")
# adding two matrices
print("This is the example of adding two matrices")
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        result[i][j] = matrix_1[i][j] + matrix_2[i][j]
for r in result:
    print(r)

print("-----------------------------------------------------")
# substracting two matrices
print("This is example substracting two matrices")
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        result[i][j] = matrix_1[i][j] - matrix_2[i][j]
for r in result:
    print(r)

print("------------------------------------------------------")
# multiplying two matrices
print("This is an example of multiplication of two matrices")
for a in range(len(matrix_1)):
    for b in range(len(matrix_2[0])):
        for c in range(len(matrix_2)):
            result[a][b] += matrix_1[b][c] * matrix_2[c][b]
for r in result:
    print(r)
print("-------------------------------------------------------")