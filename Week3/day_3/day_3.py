"""Introduction to Derivatives and Their Role in Optimization

What are Derivatives?

Derivatives measure the rate at which a function changes with respect to its input.

For a function f(x), the derivative f'(x) indicates the slope of the tangent line at a point x.

Role in Optimization:

Derivatives are fundamental in optimization problems, as they help locate local minima and maxima of functions.

In machine learning, derivatives are used in gradient-based optimization algorithms (e.g., Gradient Descent) to minimize loss functions.

Common Derivatives:

For f(x) = x², f'(x) = 2x.

For f(x) = sin(x), f'(x) = cos(x).

Python Example: Calculating and Visualizing Derivatives
"""
# import sympy as sp

# x = sp.Symbol('x')
# f = x ** 2
# derivative = sp.diff(f, x)
# print('Derivative \n', derivative)
##############################################################
"""
Gradient

A vector containing all partial derivatives of a multivariable function

Points in the direction of the steepest ascent of the function

Its magnitude indicates the rate of increase in that direction
"""
# x, y = sp.symbols('x y')
# f = x**2 + y**2
# grad_x = sp.diff(f, x)
# grad_y = sp.diff(f, y)

# print("Partial Derivatives:", grad_x, grad_y)
##############################################################
"""
# Gradient Descent Optimization Algorithm

- What is Gradient Descent?
  - Iterative optimization algorithm used to minimize a function
  - Updates parameters in the direction of the negative gradient to find the minimum

- Update Rule: θ = θ - α∇f(θ)
  - θ: Parameters of the model
  - α: Learning rate (step size)

- Why is Gradient Descent Important in Machine Learning?
  - Fundamental algorithm for training most machine learning models
  - Used to minimize loss functions and find optimal parameters
  - Forms the basis for many advanced optimization algorithms (Adam, RMSprop, etc.)
  - Essential for training neural networks through backpropagation

Key Considerations for Gradient Descent:
1. Learning Rate Selection:
   - Too small: slow convergence
   - Too large: may overshoot and fail to converge

2. Variants of Gradient Descent:
   - Batch Gradient Descent: Uses entire dataset for each update
   - Stochastic Gradient Descent (SGD): Uses one sample per update
   - Mini-batch Gradient Descent: Uses a subset of data per update

3. Challenges:
   - Getting stuck in local minima
   - Plateau regions with very small gradients
   - Saddle points in high-dimensional spaces
"""
############################# Exercise 1: Compuite Derivatives of Basic Functions #################################
# import sympy as sp

# x = sp.symbols('x')

# f = x ** 2 + 2*x + 2
# derivative = sp.diff(f, x)
# print('Derivative \n', derivative)

############################# Exercise 2: Compuite Gradients #################################

# import sympy as sp
# import numpy as np

# x, y = sp.symbols('x y')

# f = x ** 3 + y ** 2 + 2*x + 2*y
# grad_x = sp.diff(f, x)
# grad_y = sp.diff(f, y)

# grad_vector = np.array([grad_x, grad_y])
# print("Partial Derivatives Vector:", grad_vector)

############################# Exercise 3: Implements Gradient Descent for Linear Regression #################################
# import numpy as np
# import sympy as sp

# def gradient_descent(f, f_gradient, start, learning_rate=0.1, n_iter=100):
#     """
#     Basic gradient descent optimization algorithm
    
#     Parameters:
#     f: function to minimize
#     f_gradient: gradient function of f
#     start: starting point for optimization
#     learning_rate: step size (alpha)
#     n_iter: number of iterations
    
#     Returns:
#     history: list of points visited during optimization
#     """
#     history = [start]
#     current = start
    
#     for i in range(n_iter):
#         # Update rule: θ = θ - α∇f(θ)
#         gradient = f_gradient(current)
#         current = current - learning_rate * gradient
#         history.append(current)
        
#     return np.array(history)