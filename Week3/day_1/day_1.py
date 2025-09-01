## Addition and Subtraction
"""
Addition and subtraction are element-wise operations on matrices of the same size.
- For two matrices A and B of the same dimensions, A + B adds each corresponding element.
- Similarly, A - B subtracts each corresponding element.
These operations are useful in solving systems of equations, signal processing, and image manipulation.
"""
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Addition: \n", A + B)
print("Subraction: \n", A - B)

## Scalar Multiplication
"""
Scalar multiplication means multiplying every element of a matrix by a single constant (scalar).
- Example: if A = [[1,2],[3,4]] and c = 2, then c*A = [[2,4],[6,8]].
This operation is important for scaling transformations and normalizing vectors/matrices.
"""
import numpy as np
A = np.array([[1, 2], [3, 4]])
c = 2 * A
print("Scalar Multiplication \n", c)

## Matrix Multiplication
"""
Matrix multiplication (also called the dot product) is different from element-wise multiplication.
- Rule: If A is (m×n) and B is (n×p), the result is (m×p).
- Each element in the result is the sum of row elements of A multiplied by column elements of B.
It is used in computer graphics, transformations, quantum mechanics, and machine learning.
"""
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)
print("Matrix multiplication \n", result)

## Identity Matrix
"""
The identity matrix is a square matrix with 1s on the main diagonal and 0s elsewhere.
- Property: For any matrix A, A * I = I * A = A (like multiplying a number by 1).
- It acts as the multiplicative identity in matrix algebra.
"""
I = np.eye(3)
print("Identity Matrix \n", I)

## Zero Matrix
"""
A zero matrix is a matrix in which all elements are zero.
- Property: A + 0 = A (like adding 0 to a number).
- Useful as the additive identity in matrix operations.
"""
Z = np.zeros((2, 3))
print("Zero matrix \n", Z)

## Diagonal Matrix
"""
A diagonal matrix is a square matrix where all off-diagonal elements are zero.
- Only the main diagonal can contain non-zero elements.
- Useful in simplifying computations such as eigenvalues and matrix exponentials.
"""
D = np.diag([1, 2, 3])
print("Diagonal Matrix \n", D)

######################### Exercise1
"""
Exercise 1:
Perform matrix addition, subtraction, and scalar multiplication.
"""
import numpy as np
A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])
addition = A + B
subtraction = A - B
scalarmultiplication = 2 * B

######################### Exercise2
"""
Exercise 2:
Multiply a 3×3 matrix with a 3×1 vector.
This demonstrates matrix-vector multiplication, which is widely used in solving linear systems
and applying transformations to vectors.
"""
import numpy as np
B = np.array([1,0,-1])   # vector
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
result = np.dot(A,B)
print(result)

######################### Exercise3
"""
Exercise 3:
1. Multiply a matrix A by the identity matrix I (result should be A).
2. Create a diagonal matrix.
3. Create a zero matrix.
This shows how identity, diagonal, and zero matrices are used in practice.
"""
import numpy as np 
I = np.eye(3)
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
result = np.dot(A,I)
diagboal = np.diag([1,2,3])
zero = np.zeros((3,3))
