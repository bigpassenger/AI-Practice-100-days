"""
Broadcasting in NumPy
---------------------

What is Broadcasting?
----------------------
Broadcasting is a feature in NumPy that allows arrays of different shapes 
to be used together in arithmetic operations without explicitly replicating 
data. NumPy automatically expands the smaller array so that shapes become 
compatible for element-wise operations.

Rules of Broadcasting:
-----------------------
1. Dimensions are aligned from the right.
   - When comparing two arrays, NumPy starts matching dimensions from the 
     last (rightmost) axis and moves left.

2. A dimension is considered compatible if:
   a) It matches the other array’s dimension exactly.
   b) One of the dimensions is 1 (in which case it can be "stretched" to match).

Example:
--------
    Array A shape: (3, 1)
    Array B shape: (1, 4)

    Step 1: Align shapes from the right:
            A: (3, 1)
            B: (1, 4)

    Step 2: Compare dimensions:
            - Last dimension: 1 vs 4 → compatible (since one is 1)
            - First dimension: 3 vs 1 → compatible (since one is 1)

    Result: Shapes are compatible; NumPy broadcasts them to shape (3, 4).

Benefits:
---------
- Avoids unnecessary data replication.
- Allows clean, vectorized code without explicit loops.
"""
# import numpy as np

# arr = np.array([1,2,3])
# print(arr + 10)

# matr = np.array([[1,2,3], [4, 5, 6]]) #shape (2, 3)
# vector = np.array([1, 0, 1]) #shape (, 3)
# print(matr + vector)
"""
Broadcasting rule:
- matr.shape   = (2, 3)
- vector.shape = (3,)

Step 1: Align shapes from the right:
    matr:   (2, 3)
    vector:     (3)

Step 2: Compare dimensions from the rightmost side:
    Last dimension: 3 vs 3 → compatible
    Next dimension: 2 vs (nothing) → vector treated as shape (1, 3)

Step 3: Expand vector along the missing dimension:
    vector becomes:
    [[1, 0, 1],
     [1, 0, 1]]

Step 4: Element-wise addition:
    [[1+1, 2+0, 3+1],
     [4+1, 5+0, 6+1]]

Result:
    [[2, 2, 4],
     [5, 5, 7]]
"""

##############################################################
"""
Aggregation Functions in NumPy
------------------------------

What are Aggregation Functions?
--------------------------------
Aggregation functions take multiple values (often across an array or axis) 
and combine them into a single summary value — for example, sum, mean, 
min, max, standard deviation, etc.

Common Aggregation Functions:
------------------------------
1. np.sum(arr, axis=None)
   - Adds up all elements or along a given axis.
   - axis=None → sum of all elements.
   - axis=0 → sum down columns.
   - axis=1 → sum across rows.

2. np.mean(arr, axis=None)
   - Calculates the average of elements.

3. np.min(arr, axis=None) / np.max(arr, axis=None)
   - Finds the smallest / largest value.

4. np.std(arr, axis=None) / np.var(arr, axis=None)
   - Measures spread (standard deviation) or variance.

5. np.prod(arr, axis=None)
   - Product of elements.

Axis Explanation:
-----------------
Consider:
    data = np.array([[1, 2, 3],
                     [4, 5, 6]])

- np.sum(data, axis=0) → sum column-wise:
      [1+4, 2+5, 3+6] → [5, 7, 9]

- np.sum(data, axis=1) → sum row-wise:
      [1+2+3, 4+5+6] → [6, 15]

Benefits:
---------
- No need for explicit Python loops → much faster.
- Works directly on whole arrays or along specified axes.
- Makes code concise and readable.

Example:
--------
    arr = np.array([[1, 2, 3],
                    [4, 5, 6]])
    total_sum = np.sum(arr)            # → 21
    col_sum   = np.sum(arr, axis=0)    # → [5, 7, 9]
    row_mean  = np.mean(arr, axis=1)   # → [2.0, 5.0]
"""

# import numpy as np

# arr = np.array([[1, 2, 3],[4, 5, 6]])

# print("Sum: ", np.sum(arr))
# print("Mean: ", np.mean(arr))
# print("Max: ", np.max(arr))
# print("Min: ", np.min(arr))
# print("Standard Deviation: ", np.std(arr))
# print("Sum along rows: ", np.sum(arr, axis = 1))
# print("Sum along columns: ", np.sum(arr, axis = 0))


######################################################################

"""
Boolean Indexing in NumPy
-------------------------

What is Boolean Indexing?
-------------------------
Boolean indexing allows you to select elements of an array using a 
boolean mask (True/False values). The mask determines which elements 
are included in the result.

How It Works:
-------------
1. Create a NumPy array.
2. Create a boolean array (mask) of the same shape as the original array.
3. Use the mask inside square brackets to filter values.

Example 1: Basic Filtering
--------------------------
    arr = np.array([1, 2, 3, 4, 5])
    mask = arr > 3        # → [False, False, False, True, True]
    result = arr[mask]    # → [4, 5]

Example 2: One-liner Filtering
------------------------------
    arr[arr % 2 == 0]     # Select even numbers → [2, 4]

Example 3: With 2D Arrays
-------------------------
    data = np.array([[1, 2, 3],
                     [4, 5, 6]])
    mask = data > 3
    # mask → [[False, False, False],
    #          [ True,  True,  True]]
    data[mask]   # → [4, 5, 6]

Combining Conditions:
---------------------
    arr[(arr > 2) & (arr < 5)]  # Elements between 2 and 5 → [3, 4]
    arr[(arr < 2) | (arr > 4)]  # Elements < 2 or > 4 → [1, 5]

Key Points:
-----------
- Boolean mask must match the array's shape.
- Result is always 1D, even if original array is multi-dimensional.
- Very useful for filtering without loops.
"""

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])

# evens = arr[arr % 2 == 0]
# print("Evens: ", evens)

# arr[arr > 3] = 0
# print("Modified Arrays: ", arr)

###############################################################

# import numpy as np

# np.random.seed(42)

# random_array = np.random.rand(3, 3)
# print("Random Array: \n", random_array)

# random_integers = np.random.randint(0, 10, size=(2, 3))
# print("Random Integers: \n", random_integers)

############################## Hands-On Exercises1 #################################

# import numpy as np

# matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# vector = np.array([1, 0, -1])

# print(matrix*vector)
############################## Hands-On Exercises1 #################################

# import numpy as np

# random_matrix  = np.random.randint(1, 51,(5,5))
# print(random_matrix)
# random_matrix[random_matrix<25] = 0
# print(random_matrix)

############################## Hands-On Exercises2 #################################

# import numpy as np
# random_matrix  = np.random.randint(1, 51,(3,3,3))


# print("Standard Deviation: ", np.std(random_matrix, axis= 2))
# print("Sum along rows: ", np.sum(random_matrix, axis = 1))
# print("Sum along columns: ", np.sum(random_matrix, axis = 0))


############################## Hands-On Exercises3 #################################

# import numpy as np

# random_matrix = np.random.randint(1, 51, (3,3))

# print(random_matrix)
# random_matrix[random_matrix % 2 == 0] = 0

# print(random_matrix)