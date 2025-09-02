"""
# =====================================================
# Determinants and Inverse of a Matrix
# =====================================================

# 1. Determinant
# The determinant is a scalar (single number) that provides important
# information about a matrix.
# 
# Key points:
# - Defined only for square matrices (n x n).
# - If det(A) = 0 → matrix A is singular (non-invertible).
# - If det(A) ≠ 0 → matrix A is invertible.
# - Geometric interpretation:
#   For a 2x2 matrix, the determinant represents the scaling factor
#   of the area formed by its column vectors (parallelogram area).
#
# Formula for 2×2 Matrix:
# det([[a, b],
#      [c, d]]) = ad - bc
#
# Example:
import numpy as np

A = np.array([[2, 3],
              [1, 4]])

det_A = np.linalg.det(A)   # Compute determinant
print("Determinant of A:", det_A)

# Here:
# det(A) = (2*4) - (3*1) = 8 - 3 = 5
# Since det(A) = 5 ≠ 0, the matrix is invertible.


# 2. Checking singular vs invertible
B = np.array([[2, 4],
              [1, 2]])

det_B = np.linalg.det(B)
print("Determinant of B:", det_B)

# det(B) = (2*2) - (4*1) = 4 - 4 = 0
# → Matrix B is singular (NOT invertible)


# 3. Geometric meaning
# For a 2x2 matrix, its column vectors represent two vectors in 2D space.
# The determinant gives the signed area of the parallelogram formed by them.

import matplotlib.pyplot as plt

v1 = np.array([2, 1])   # first column of A
v2 = np.array([3, 4])   # second column of A

plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label="v1")
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label="v2")

# Draw parallelogram
parallelogram = np.array([[0,0], v1, v1+v2, v2])
plt.fill(parallelogram[:,0], parallelogram[:,1], alpha=0.3, label="Parallelogram (area=det(A))")

plt.xlim(-1,6)
plt.ylim(-1,6)
plt.gca().set_aspect('equal')
plt.legend()
plt.show()

# This plot shows:
# - v1 and v2 as vectors
# - The area of the parallelogram = |det(A)| = 5
# → determinant = scaling factor for area

"""

# import numpy as np

# A = np.array([[2, 3], [1, 4]])
# determinant = np.linalg.det(A)
# print("Determinant: ",determinant)


"""
# =====================================================
# Inverse of a Matrix
# =====================================================

# 1. Definition
# The inverse of a matrix A is denoted as A^(-1).
# It satisfies:
# A * A^(-1) = A^(-1) * A = I   (Identity matrix)
#
# - Only square matrices with det(A) ≠ 0 have an inverse.
# - If det(A) = 0, the matrix is singular → no inverse.
#
# Formula for a 2×2 matrix:
# If A = [[a, b],
#         [c, d]]
# then
# A^(-1) = (1 / det(A)) * [[ d, -b],
#                          [-c,  a]]

import numpy as np

# Example 1: Invertible matrix
A = np.array([[2, 3],
              [1, 4]])

det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

if det_A != 0:
    A_inv = np.linalg.inv(A)
    print("Inverse of A:\n", A_inv)

    # Verify: A * A^(-1) = I
    I = np.dot(A, A_inv)
    print("A * A^(-1):\n", I)

# Explanation:
# det(A) = 5
# So A^(-1) = (1/5) * [[ 4, -3],
#                      [-1,  2]]


# Example 2: Singular (non-invertible) matrix
B = np.array([[2, 4],
              [1, 2]])

det_B = np.linalg.det(B)
print("\nDeterminant of B:", det_B)

if det_B == 0:
    print("Matrix B is singular → no inverse exists.")
else:
    B_inv = np.linalg.inv(B)
    print("Inverse of B:\n", B_inv)


# 2. Geometric interpretation
# - The inverse matrix "undoes" the transformation done by the matrix.
# - For example, if A scales/rotates vectors, then A^(-1) reverses
#   that scaling/rotation, bringing vectors back to their original positions.

# Let's test with a vector
v = np.array([1, 2])

Av = A @ v            # Apply matrix A
Ainv_Av = A_inv @ Av  # Apply inverse → should return original v

print("\nOriginal vector v:", v)
print("After A:", Av)
print("After A^(-1):", Ainv_Av)

"""

# import numpy as np

# A = np.array([[2, 3], [1, 4]])
# inverse = np.linalg.inv(A)
# print("Determinant: ",inverse)

"""
"""
"""Eigenvalues and eigenvectors are fundamental concepts in linear algebra that describe 
the fundamental "directions" and "scaling factors" of a linear transformation.

Definition:
If A is a square matrix, then a non-zero vector v is an eigenvector of A if:
    A · v = λ · v
where λ is a scalar known as the eigenvalue corresponding to the eigenvector v.

Geometric Interpretation:
- Eigenvectors represent directions that remain unchanged under the linear transformation
- Eigenvalues represent how much vectors in those directions are stretched or compressed
- Positive eigenvalues > 1 indicate stretching, values < 1 indicate compression
- Negative eigenvalues indicate direction reversal

Properties:
1. An n×n matrix has exactly n eigenvalues (counting multiplicities)
2. Eigenvalues can be real or complex numbers
3. For symmetric matrices, eigenvalues are always real numbers
4. Eigenvectors corresponding to distinct eigenvalues are linearly independent
"""
"""

import numpy as np

# Example 1: Basic 2×2 matrix with real eigenvalues
A = np.array([[4, 1],
              [2, 3]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix A:")
print(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors (as columns):")
print(eigenvectors)

# Verify the eigen equation A·v = λ·v
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lambda_val = eigenvalues[i]
    print(f"\nFor eigenvalue {lambda_val}:")
    print(f"A·v = {A @ v}")
    print(f"λ·v = {lambda_val * v}")
    print(f"Equation holds: {np.allclose(A @ v, lambda_val * v)}")

# Example 2: Symmetric matrix (always has real eigenvalues)
B = np.array([[2, 1],
              [1, 2]])

eigenvalues_b, eigenvectors_b = np.linalg.eig(B)
print("\nSymmetric matrix B:")
print(B)
print("Real eigenvalues:", eigenvalues_b)

# Example 3: Matrix with complex eigenvalues (rotation matrix)
theta = np.pi/4  # 45 degree rotation
C = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])

eigenvalues_c, eigenvectors_c = np.linalg.eig(C)
print("\nRotation matrix C:")
print(C)
print("Complex eigenvalues:", eigenvalues_c)

# Example 4: Matrix diagonalization (A = V·D·V⁻¹)
D = np.diag(eigenvalues)  # Diagonal matrix of eigenvalues
V = eigenvectors          # Matrix of eigenvectors
A_reconstructed = V @ D @ np.linalg.inv(V)

print("\nOriginal matrix A:")
print(A)
print("Reconstructed from eigendecomposition:")
print(A_reconstructed)
print("Reconstruction accurate:", np.allclose(A, A_reconstructed))

# Example 5: Finding dominant eigenvector using power iteration
def power_iteration(matrix, num_iterations=100):
    # Start with a random vector
    b = np.random.rand(matrix.shape[0])
    
    for _ in range(num_iterations):
        # Multiply by matrix and normalize
        b = matrix @ b
        b = b / np.linalg.norm(b)
    
    # Compute corresponding eigenvalue
    eigenvalue = (b @ matrix @ b) / (b @ b)
    
    return eigenvalue, b

dominant_eigenvalue, dominant_eigenvector = power_iteration(A)
print("\nDominant eigenvalue (power iteration):", dominant_eigenvalue)
print("Dominant eigenvector (power iteration):", dominant_eigenvector)
"""
# eigenValues, eigenVectors = np.linalg.eig(A)
# print("EigenValues: ", eigenValues)
# print("EigenVectors: ", eigenVectors)

# B = np.array([[4, 2], [1, 1]])
# eigval, eigvec = np.linalg.eig(B)
# print("EigVal: ",eigval)
# print("EigVect: ",eigvec)


"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float

"""
"""Matrix Decomposition is the process of breaking down a matrix into simpler,
constituent matrices that have specific properties, making certain matrix
operations easier to perform or understand.

Singular Value Decomposition (SVD) is one of the most important matrix
decomposition techniques with applications in data compression, dimensionality
reduction, and solving linear systems.

SVD decomposes any matrix A (m×n) into three matrices:
    A = U · Σ · Vᵀ
where:
    - U is an m×m orthogonal matrix (left singular vectors)
    - Σ is an m×n diagonal matrix with non-negative real numbers (singular values)
    - Vᵀ is an n×n orthogonal matrix (right singular vectors, transposed)

The singular values in Σ are arranged in descending order, and the corresponding
columns of U and V represent the directions of maximum variance in the original matrix."""
"""

# Example 1: Basic SVD computation
print("Example 1: Basic SVD Computation")

# Create a sample matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

print("Original matrix A (4×3):")
print(A)

# Perform SVD
U, S, Vt = np.linalg.svd(A, full_matrices=False)

print("\nLeft singular vectors U (4×3):")
print(U)
print("\nSingular values S:", S)
print("\nRight singular vectors Vt (3×3):")
print(Vt)

# Reconstruct the original matrix from SVD components
Sigma = np.diag(S)
A_reconstructed = U @ Sigma @ Vt

print("\nReconstructed matrix:")
print(A_reconstructed)
print("\nReconstruction error:", np.linalg.norm(A - A_reconstructed))

"""
"""Applications of SVD:

1. Dimensionality Reduction (PCA)
2. Data Compression
3. Solving Linear Systems (Pseudoinverse)
4. Recommender Systems
5. Image Processing
6. Noise Reduction"""
"""

# Example 2: Image Compression using SVD
print("\nExample 2: Image Compression with SVD")

# Load a sample image
image = data.camera()
image = img_as_float(image)

# Perform SVD on the image matrix
U, S, Vt = np.linalg.svd(image, full_matrices=False)

# Compress the image by keeping only the top k singular values
k = 50  # Number of singular values to keep
compressed_image = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]

# Calculate compression ratio
original_size = image.size
compressed_size = U[:, :k].size + k + Vt[:k, :].size
compression_ratio = original_size / compressed_size

print(f"Compression ratio: {compression_ratio:.2f}:1")
print(f"Original size: {original_size} elements")
print(f"Compressed representation: {compressed_size} elements")

# Plot original and compressed images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(compressed_image, cmap='gray')
plt.title(f'Compressed Image (k={k})')
plt.axis('off')
plt.tight_layout()
plt.show()

# Example 3: Dimensionality Reduction with SVD (PCA)
print("\nExample 3: Dimensionality Reduction with SVD")

# Create sample data with 3 features
np.random.seed(42)
n_samples = 100
X = np.random.randn(n_samples, 3)
X = X @ np.array([[1, 0.8, 0.6],
                  [0.8, 1, 0.7],
                  [0.6, 0.7, 1]])  # Add correlation

# Center the data
X_centered = X - np.mean(X, axis=0)

# Perform SVD on the centered data matrix
U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

# Project data onto first two principal components
X_reduced = X_centered @ Vt[:2, :].T

print("Original data shape:", X.shape)
print("Reduced data shape:", X_reduced.shape)
print("Variance explained by components:", S**2 / np.sum(S**2))
print("First two components explain {:.2f}% of variance".format(
    100 * np.sum(S[:2]**2) / np.sum(S**2)))

# Example 4: Solving Linear Systems with SVD (Pseudoinverse)
print("\nExample 4: Solving Linear Systems with SVD")

# Create a matrix that might be singular or poorly conditioned
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([1, 2, 3])

# Regular matrix inversion might fail or be inaccurate
try:
    x_inv = np.linalg.inv(A) @ b
    print("Solution using matrix inversion:", x_inv)
except np.linalg.LinAlgError:
    print("Matrix is singular, cannot use direct inversion")

# Use SVD to compute the pseudoinverse
U, S, Vt = np.linalg.svd(A, full_matrices=False)

# Create the pseudoinverse of Σ
S_inv = np.diag(1 / S)
# Compute the pseudoinverse of A: A⁺ = V · Σ⁺ · Uᵀ
A_pseudoinv = Vt.T @ S_inv @ U.T

# Solve the system using the pseudoinverse
x_svd = A_pseudoinv @ b
print("Solution using SVD pseudoinverse:", x_svd)

# Check the solution
print("A @ x_svd ≈ b:", np.allclose(A @ x_svd, b, atol=1e-10))

# Example 5: Recommender Systems with SVD
print("\nExample 5: Recommender Systems with SVD (Conceptual)")

# Create a user-item rating matrix (rows: users, columns: items)
ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4]
])

print("Original user-item ratings:")
print(ratings)

# Perform SVD on the rating matrix
U, S, Vt = np.linalg.svd(ratings, full_matrices=False)

# Keep only the top k features to reduce dimensionality
k = 2
U_k = U[:, :k]
S_k = np.diag(S[:k])
Vt_k = Vt[:k, :]

# Reconstruct the rating matrix with reduced dimensions
ratings_reconstructed = U_k @ S_k @ Vt_k

print("\nReconstructed ratings with SVD (k=2):")
print(ratings_reconstructed)

"""
"""In recommender systems, SVD helps:
1. Discover latent features that explain user preferences
2. Handle missing values (zero entries in the rating matrix)
3. Make predictions for unrated items

The reconstructed matrix provides estimated ratings for all user-item pairs,
even those that weren't originally rated."""
"""

# Example 6: Visualizing Singular Values
print("\nExample 6: Singular Value Spectrum")

# Create a random matrix with a clear rank
np.random.seed(42)
B = np.random.randn(10, 10)
B = B @ B.T  # Make it positive semidefinite with rank 10

# Perform SVD
U, S, Vt = np.linalg.svd(B)

# Plot the singular values
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(S)+1), S, 'bo-')
plt.xlabel('Singular Value Index')
plt.ylabel('Singular Value Magnitude')
plt.title('Singular Value Spectrum')
plt.grid(True)
plt.show()

# Calculate cumulative energy
cumulative_energy = np.cumsum(S**2) / np.sum(S**2)
print("Cumulative energy captured by top k singular values:")
for k in range(1, min(6, len(S)+1)):
    print(f"Top {k} values: {cumulative_energy[k-1]:.3f}")
"""

# U, S, Vt = np.linalg.svd(A)
# print("U: \n", U)
# print("S: \n", S)
# print("V Transpose: \n", Vt)


######################################## Exercise 1 : Calculate a Determinant and Inverse of a 3 * 3 matrix ########################################
# import numpy as np

# matrix = np.array([[1, 2, 7], [3, 4, 8], [5, 6, 9]])

# determinant = np.linalg.det(matrix)
# inverse = np.linalg.inv(matrix)
# print("Determinant: \n", determinant)
# print("Inverse: \n", inverse)
######################################## Exercise 2 : Compute EigenValues and EigenVectors of a 3 * 3 matrix ########################################
# import numpy as np

# matrix = np.array([[1, 2, 7], [3, 4, 8], [5, 6, 9]])
# EigenValues, EigenVectors = np.linalg.eig(matrix)

# print("EigenValues: \n",EigenValues)
# print("EigenVectors: \n",EigenVectors)

######################################## Exercise 3 : Perform Singular Value Decomposition of a 3 * 3 matrix ########################################
import numpy as np

matrix = np.array([[1, 2, 7], [3, 4, 8], [5, 6, 9]])

U, S, Vt = np.linalg.svd(matrix)

print("U: \n", U)
print("S: \n", S)
print("V Transpose: \n", Vt)

Sigma = np.zeros((3, 3))
np.fill_diagonal(Sigma, S)
reconstructed = U @ Sigma @ Vt
print("Reconstructed Matrix \n", reconstructed)