#"Writing Clean, 'Pythonic' Code"
""" 
What is Pythonic Code?

    *Pythonic code refers to writing Python in a way that follows its idioms, style, and readability standards, taking advantage of the language's unique features rather than just mimicking patterns from other programming languages.

    *Best Practices

    *Use descriptive variable names: Variable names should clearly express their purpose, making the code self-explanatory.

    *Write modular code with functions and classes: Break code into reusable, organized units to improve maintainability and readability.

    *Follow PEP 8 style guidelines: Adhere to Python’s official style guide (PEP 8) for consistent formatting, indentation, and naming conventions.

    *Avoid redundancy; leverage Python’s powerful built-ins: Use Python's built-in functions and data structures to write shorter, cleaner, and more efficient code rather than reinventing the wheel.
"""
###############################################################################################################
# List Comprehensive
# # [expression for item in iterable if condition]

# # # Create a list of squares
# squares = [x**2 for x in range(10)]
# print(squares)

# # # Filter Even Numbers
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)

###############################################################################################################
"""
A lambda function in Python is a small, anonymous function created with the `lambda` keyword.
It is useful for short, simple operations where defining a full function with `def` would be excessive.

Syntax:
    lambda arguments: expression
- arguments: parameters separated by commas
- expression: a single statement whose value is returned automatically

Example:
    # Normal function
    def square(x):
        return x ** 2

    # Lambda equivalent
    square_lambda = lambda x: x ** 2
    print(square_lambda(5))  # Output: 25

Multiple arguments:
    add = lambda a, b: a + b
    print(add(3, 7))  # Output: 10

Common uses:
1. With map():
    nums = [1, 2, 3, 4]
    squares = list(map(lambda x: x ** 2, nums))  # [1, 4, 9, 16]

2. With filter():
    nums = [1, 2, 3, 4, 5]
    even_nums = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

3. With sorted():
    pairs = [(1, 2), (3, 1), (5, 0)]
    sorted_pairs = sorted(pairs, key=lambda x: x[1])  # [(5, 0), (3, 1), (1, 2)]

Pythonic tip:
    Use lambdas for short, simple tasks.
    If the function gets complex, use `def` for readability.
"""
# add = lambda x, y: x + y
# print(add(3,5))

###############################################################################################################
"""
The `map()` function in Python applies a given function to each item of an iterable (like a list, tuple, etc.) 
and returns a map object (an iterator). You can convert it to a list, tuple, or other iterable type.

Syntax:
    map(function, iterable)

Parameters:
- function: a function (can be built-in, user-defined, or a lambda) that takes one argument
- iterable: a sequence (list, tuple, string, etc.) whose elements will be processed

Example with a normal function:
    def square(x):
        return x ** 2

    nums = [1, 2, 3, 4]
    result = map(square, nums)
    print(list(result))  # Output: [1, 4, 9, 16]

Example with a lambda function:
    nums = [1, 2, 3, 4]
    result = map(lambda x: x ** 2, nums)
    print(list(result))  # Output: [1, 4, 9, 16]

Multiple iterables:
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    result = map(lambda a, b: a + b, nums1, nums2)
    print(list(result))  # Output: [5, 7, 9]

Key points:
- `map()` is lazy; it returns an iterator, so you often wrap it with `list()` or `tuple()` to view results.
- It is often used with `lambda` for concise transformations.
- It's Pythonic for transforming sequences without writing explicit loops.
"""

# numbers = [1, 2, 3, 4]
# squares = map(lambda x: x**2,numbers)
# print(list(squares))

#################################################################################################################################
"""
The `filter()` function in Python constructs an iterator from elements of an iterable for which a given function returns True.

Syntax:
    filter(function, iterable)

Parameters:
- function: a function that tests each element; should return True (keep element) or False (discard element).
            If None is passed, it simply removes all elements that are False in a boolean context.
- iterable: a sequence (list, tuple, etc.) to filter.

Example with a normal function:
    def is_even(x):
        return x % 2 == 0

    nums = [1, 2, 3, 4, 5, 6]
    result = filter(is_even, nums)
    print(list(result))  # Output: [2, 4, 6]

Example with a lambda function:
    nums = [1, 2, 3, 4, 5, 6]
    result = filter(lambda x: x % 2 == 0, nums)
    print(list(result))  # Output: [2, 4, 6]

Using `None` as the function (removes falsy values like 0, "", None, False):
    values = [0, 1, "", "Python", None, True]
    result = filter(None, values)
    print(list(result))  # Output: [1, 'Python', True]

Key points:
- `filter()` is lazy; it returns an iterator, so wrap with `list()` or `tuple()` to see results.
- Use when you want to keep only certain elements based on a condition.
- Often combined with `lambda` for concise filtering logic.
"""

# numbers = [1, 2, 3, 4]
# evenList = filter(lambda x: x % 2 == 0, numbers)
# print(list(evenList))

##################################################################################################################
"""
The `reduce()` function in Python applies a given function cumulatively to the items of an iterable, 
reducing the iterable to a single accumulated value.

Note:
- `reduce()` is not a built-in function in Python 3; it must be imported from the `functools` module.

Syntax:
    from functools import reduce
    reduce(function, iterable[, initializer])

Parameters:
- function: a function that takes two arguments and returns a single result.
- iterable: the sequence of items to process.
- initializer (optional): a starting value; if provided, it is placed before the first element in the computation.

Example without initializer:
    from functools import reduce
    nums = [1, 2, 3, 4]
    result = reduce(lambda x, y: x + y, nums)
    print(result)  # Output: 10
    # Calculation steps: ((1 + 2) + 3) + 4 = 10

Example with initializer:
    from functools import reduce
    nums = [1, 2, 3, 4]
    result = reduce(lambda x, y: x + y, nums, 10)
    print(result)  # Output: 20
    # Calculation steps: (((10 + 1) + 2) + 3) + 4 = 20

Other examples:
    # Find maximum
    nums = [5, 3, 8, 2]
    max_value = reduce(lambda a, b: a if a > b else b, nums)
    print(max_value)  # Output: 8

Key points:
- `reduce()` is useful for cumulative computations like sum, product, maximum, concatenation, etc.
- If your goal is just to sum numbers, use Python's built-in `sum()` (more readable and faster).
- Use `reduce()` when the accumulation logic is custom and can't be replaced with built-in functions.
"""

# from functools import reduce
# numbers = [1, 2, 3, 4]
# product = reduce(lambda x,y: x * y, numbers)
# print(product)

##################################################################################################################

"""
The `os` module in Python provides functions to interact with the operating system.  
It allows you to work with file paths, directories, environment variables, processes, and more.

Import:
    import os

Common uses:

1. **Working with directories**
    os.getcwd()                 # Get current working directory
    os.chdir("path")            # Change current directory
    os.listdir("path")          # List files and folders in a directory
    os.mkdir("new_folder")      # Create a new directory
    os.makedirs("a/b/c")        # Create nested directories
    os.rmdir("folder")          # Remove an empty directory
    os.removedirs("a/b/c")      # Remove nested empty directories

2. **Working with files**
    os.remove("file.txt")       # Delete a file
    os.rename("old.txt", "new.txt")  # Rename a file or folder

3. **Path operations** (often used with `os.path`)
    os.path.join("folder", "file.txt")   # Join paths safely
    os.path.exists("path")               # Check if a path exists
    os.path.isfile("path")               # Check if path is a file
    os.path.isdir("path")                # Check if path is a directory
    os.path.abspath("file.txt")          # Get absolute path
    os.path.basename("path/to/file.txt") # Get file name
    os.path.dirname("path/to/file.txt")  # Get directory name

4. **Environment variables**
    os.environ["VAR_NAME"]               # Get value of an environment variable
    os.environ["NEW_VAR"] = "value"      # Set an environment variable

5. **Running system commands**
    os.system("echo Hello World")        # Execute a system command (less recommended; use subprocess module for security)

Example:
    import os
    print("Current Directory:", os.getcwd())
    if not os.path.exists("test_folder"):
        os.mkdir("test_folder")
    print("Directories:", os.listdir())

Key points:
- Use `os.path` for path manipulations to ensure cross-platform compatibility.
- For file operations, `pathlib` (introduced in Python 3.4) is often more modern and convenient.
- For running external commands, `subprocess` is safer than `os.system()`.
"""
 
# import os
# import time
# print(os.getcwd())
# os.mkdir("test_dir")

##################################################################################################################
"""
The `sys` module in Python provides functions and variables that interact directly with the Python interpreter.  
It allows you to access command-line arguments, control script execution, and inspect Python's environment.

Import:
    import sys

Common uses:

1. **Command-line arguments**
    sys.argv                # List of command-line arguments passed to the script
    # sys.argv[0] is the script name
    # sys.argv[1:] are the additional arguments

    Example:
        # script.py
        import sys
        print("Script name:", sys.argv[0])
        print("Arguments:", sys.argv[1:])

        # Run in terminal:
        # python script.py hello world
        # Output:
        # Script name: script.py
        # Arguments: ['hello', 'world']

2. **Exiting the program**
    sys.exit()              # Exit the script
    sys.exit(0)             # Exit with success
    sys.exit(1)             # Exit with error

3. **Python version**
    sys.version             # Python version as a string
    sys.version_info        # Version as a tuple (major, minor, micro)

4. **System-specific information**
    sys.platform            # Name of the OS platform (e.g., 'win32', 'linux', 'darwin')
    sys.executable          # Path to the Python interpreter
    sys.path                # List of directories where Python looks for modules

5. **Standard input/output/error streams**
    sys.stdin               # Standard input stream
    sys.stdout              # Standard output stream
    sys.stderr              # Standard error stream

    Example:
        sys.stdout.write("Hello\n")
        sys.stderr.write("Error message\n")

6. **Recursion limit**
    sys.getrecursionlimit()     # Get current recursion limit
    sys.setrecursionlimit(2000) # Set new recursion limit (use with caution)

Key points:
- `sys` is used for interacting with the interpreter itself.
- It's helpful for command-line tools, debugging, and environment inspection.
- Use `argparse` for more advanced command-line argument parsing instead of manually handling `sys.argv`.
"""
# import sys

# print(sys.argv)
# print(sys.version)

################################## Hands-On Project : Command-Line Task Manager ################################################################################

tasks = {}

def Create_task(task:str):
    tasks[task] = ""

def Check_task(number_of_task:int):
    key = list(tasks.keys())[number_of_task-1]
    tasks[key] = 'Done'

def Delete_task(number_of_task:int):
    key = list(tasks.keys())[number_of_task - 1]
    del tasks[key]
    print("The Task deleted!")

while True:
    for i, (key, value) in enumerate(tasks.items()):
        print(f"{i+1}_{key}: {value}")
    print()
    print()
    print("Choose an action:")
    print("1. Add a task")
    print("2. Mark a task as done")
    print("3. Delete a task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == '1':
        task_name = input("Enter the new task: ").strip()
        Create_task(task_name)
        print("Task added.\n")
        
    elif choice == '2':
        if not tasks:
            print("No tasks to mark done.\n")
            continue
        task_num = input("Enter the number of the task to mark as done: ").strip()
        if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
            Check_task(int(task_num))
            print("Task marked as done.\n")
        else:
            print("Invalid task number.\n")
            
    elif choice == '3':
        if not tasks:
            print("No tasks to delete.\n")
            continue
        task_num = input("Enter the number of the task to delete: ").strip()
        if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
            Delete_task(int(task_num))
            print()
        else:
            print("Invalid task number.\n")
            
    elif choice == '4':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.\n")