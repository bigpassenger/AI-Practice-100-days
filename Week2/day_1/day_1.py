# # import numpy as np 


# # # Creating an arry from a list
# # arr = np.array([1, 2, 3, 4])
# # print(arr)

# # # Creating a matrix with zeroes from a built-in function
# # zeroes = np.zeros((3,3))
# # print(zeroes)

# # ones = np.ones((2,4))
# # print(ones)

# # range_array = np.arange(1, 10, 2)
# # print(range_array)

# # linspace_array = np.linspace(0, 1, 5)
# # print(linspace_array)

# # ###################Manipulating_arrays######################

# # # Reshaping an array
# # arr = np.array([1, 2, 3, 4, 5, 6])
# # reshaped = arr.reshape((2,3))
# # print(reshaped)

# # arr = np.array([1, 2, 3])
# # expanded = arr[:,np.newaxis]
# # print(expanded)

# # ##################Basic Operations On Arrays ##################

# # # Element-wise Operations
# # a = np.array([1, 2, 3])
# # b = np.array([4, 5, 6])
# # print(a + b)
# # print(a * b)  #1*4,2*5,3*6
# # print(a / b)  # 1/4,2/5,3/6

# # ################# Mathematical Operations #################

# # arr = np.array([4, 16, 25])
# # print(np.sqrt(arr)) #2,4,5
# # print(np.sum(arr)) #45
# # print(np.mean(arr)) #mean
# # print(np.max(arr)) # 25

# # ################ indexing, Slicing, Reshaping ################

# # import numpy as np
 
# # arr = np.array([10, 20, 30, 40, 50])
# # print(arr[2])
# # print(arr[-1])

# # ################ Slicing ####################

# # arr = np.array([10, 20, 30, 40, 50])
# # print(arr[1:4])
# # print(arr[:4])

# # ################ Reshaping ####################

# # reshaped = arr.reshape(2,3)
# # print(reshaped)

# # ############################## Exercise 1 : Generate Arrays for Basic Mathematical Operations #####################
# # import numpy as np

# # a = np.arange(1, 6)
# # b = np.arange(6, 11)

# # print("Add: ", a + b)
# # print("Sub: ", a - b)
# # print("Mult: ", a * b)
# # print("Div: ", a / b)

# ############################# Exercise 1 : Create a 3 * 3 Matrix and Perform Operations #####################

# import numpy as np

# a = np.array([1,2,3,4,5,6,7,8,9])
# a_matrix = a.reshape((3,3))
# print(a_matrix)

# # # Transpose
# transpose = a_matrix.T
# print(transpose)

# another_matrix = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# print("Add: ", a_matrix + another_matrix)
# print("Mult: ", a_matrix * another_matrix)

# ############################# Exercise 3 : Create a 4 * 4 Matrix and calculate the sum of its rows and columns #####################
# import numpy as np
# another_matrix = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# print(another_matrix.sum())

############################# Exercise 3 : write a program to normalize an array(scale values between 0 and 1) #####################
# import numpy as np
# array = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# print((array - array.min()) / (array.max() - array.min()))

############################# Exercise 4: generate a random array and find the minimum and maximum values #####################
# import numpy as np
# array = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# print(array.min())
# print(array.max())