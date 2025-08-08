# # # # # # # # # # #  import a module
# from math import sqrt
# import math
# print(math.sqrt(16))
# # # # # # # # # # #  import ... as .
# import math as m
# # # # # # # # # # # Function with parameters and return value
# def add_numbers(a, b):
#     # c = a + b
#     # return c
#     return a + b
# result = add_numbers(5, 3)
# print("Sum: ", result)

# def function_name(parameters):
#     #Code block
#     return result

# # # # # # # # # # #  Global Scope

# greeting = "Hi"

# def say_hello():
#     print(greeting + " from inside the function")

# say_hello()
# print(greeting + " from outside the function")

# # # # # # # # # # #  Local Scope
# def greet():
#     message = "Hello World"
#     print(message)

# greet()
#print(message)
# # # # # # # # # # #  Exercise 1: Create a Function to Calculate Factorials # # # # # # # # # # #
# def Factorial(num:int):
#     """
#     This Function will calculate the Factorial of a number.

#     Args: 
#         num: An integer of a number for calculating the factorial.
#     """
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * Factorial(num-1)

# def print_f(num:int):
#     """
#     This Function will print the Factorial of a number using Factorial Function.

#     Args: 
#         num: An integer of a number for calculating the factorial.
#     """
#     result = Factorial(num)
#     print(f"The factorail of {num} is {result}")

# print_f(22)
# # # # # # # # # # #  Exercise 2: Create a Mathatical Module to Calculate +-*/ # # # # # # # # # # #
# import math_operations as mo

# num1 = 2
# num2 = 4

# print("Addition: ", mo.add(num1, num2))
# print("Subtraction: ", mo.subtract(num1, num2))
# print("Multiplication: ", mo.multiply(num1, num2))
# print("Division: ", mo.divide(num1, num2))
# # # # # # # # # # #  Exercise 3: Create a function to check if a number is even or odd # # # # # # # # # # #
# def even_odd(num:int):
#     """
#     This Function will guess if the number is even or odd.

#     Args: 
#         num: An integer of a number for the guess.
#     """
#     guess = num % 2
#     if guess == 0:
#         return True
#     else:
#         return False
