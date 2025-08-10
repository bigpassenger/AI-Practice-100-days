"""
File Opening Modes in Python (for use with open()):

1. "r"   -> Read mode (default)
           Opens the file for reading only.
           File must already exist, or you'll get a FileNotFoundError.

2. "w"   -> Write mode
           Creates a new file for writing, or overwrites the file if it already exists.
           WARNING: Existing data will be erased.

3. "a"   -> Append mode
           Opens the file for writing but appends data to the end.
           Creates the file if it doesn’t exist.
           Preserves existing content.

4. "r+"  -> Read and Write mode
           Opens the file for both reading and writing.
           File must already exist; otherwise, you'll get FileNotFoundError.
           Does not truncate the file; you can overwrite or update parts.

Other useful variants:
----------------------
"b"  -> Binary mode (e.g., "rb", "wb", "ab")
       Use for non-text files like images or PDFs.

"t"  -> Text mode (default), can be combined with above (e.g., "rt", "wt").

"x"  -> Exclusive creation mode
       Creates a new file; fails if the file already exists.

Examples:
---------
f = open("data.txt", "r")    # read text file
f = open("image.jpg", "rb")  # read binary file
f = open("log.txt", "a")     # append to file
f = open("notes.txt", "w+")  # read and write (overwrite existing)
"""
"""
Reading Files in Python:
------------------------

Steps:
1. Open the file using open("filename", "r")  # 'r' means read mode
2. Use one of the read methods:
   - .read()       -> Reads the entire file as one string.
   - .read(n)      -> Reads the first n characters (or bytes in binary mode).
   - .readline()   -> Reads one line at a time (including newline character).
   - .readlines()  -> Reads all lines and returns them as a list of strings.
3. Close the file using .close() to free resources.

Example:
--------
f = open("data.txt", "r")      # Open for reading
content = f.read()             # Read entire file
print(content)
f.close()                      # Always close the file

Best Practice:
--------------
Use 'with' statement so the file is automatically closed:

with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())    # strip() removes newline at end

Notes:
------
- If the file does not exist in "r" mode, you'll get FileNotFoundError.
- In binary mode ("rb"), data will be read as bytes instead of strings.
"""
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)
"""
Writing to Files in Python:
---------------------------

Steps:
1. Open the file in write ("w"), append ("a"), or read/write ("r+") mode.
   - "w"  -> Overwrites the file (creates if not exists).
   - "a"  -> Appends to the file (creates if not exists).
   - "r+" -> Reads and writes without truncating (file must exist).

2. Use one of the write methods:
   - .write(string)        -> Writes a string to the file.
                              (No automatic newline — add '\n' manually if needed)
   - .writelines(list)     -> Writes a list of strings to the file.
                              (Does not add newlines unless included in strings)

3. Close the file with .close() or use 'with' to auto-close.

Examples:
---------
# Writing a single string
with open("notes.txt", "w") as f:
    f.write("Hello World!\n")
    f.write("This is the second line.\n")

# Writing multiple lines from a list
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("notes.txt", "a") as f:   # Append mode
    f.writelines(lines)

Notes:
------
- Always include '\n' if you want line breaks.
- Use "a" mode to avoid overwriting existing content.
- In binary mode ("wb", "ab"), you must write bytes, not strings.
"""
# with open("sample.txt", "w") as file:
#     file.write("Hello, World!")
#     file.writelines(['Alice', 'Bob', 'Ali'])

"""
Using 'with' Statement for File Handling:
----------------------------------------

The 'with' statement is used to open files in Python and ensures proper resource management.

Advantages:
- Automatically closes the file after the block of code is executed.
- Handles exceptions gracefully, closing the file even if errors occur.
- Makes code cleaner and easier to read.

Syntax:
--------
with open("filename", "mode") as file_object:
    # perform file operations inside this block
    file_object.read() or file_object.write() etc.

Example:
--------
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
# No need to call f.close() — it's automatic

Reading line-by-line:
---------------------
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

Writing example:
----------------
with open("output.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("Writing with 'with' is safe and clean.\n")

Summary:
--------
- Use 'with' whenever opening files.
- It ensures files are properly closed, avoiding resource leaks.
- Cleaner and less error-prone than manual open/close.
"""
#################################################################
"""
Handling Exceptions When Working with Files:
--------------------------------------------

File operations can raise errors, such as:
- FileNotFoundError (trying to read a non-existent file)
- IOError/OSError (issues with reading/writing)
- PermissionError (lack of access rights)

To handle these safely, use try-except blocks.

Example with open() and reading a file:

try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

Explanation:
------------
- try: Attempts to execute the block of code that might cause an error.
- except: Catches and handles specific exceptions.
- Exception as e: Catches any other exceptions not previously handled.
- This prevents the program from crashing unexpectedly.

Tips:
-----
- Always handle at least FileNotFoundError when reading files.
- You can add multiple except blocks for different errors.
- Using 'with' inside try is common for safe file handling.
"""

# try:
#     with open("sample.text", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File Not Found!")

############################## EXERCISE 1 COUNT WORDS IN A FILE ############################################
# def count_words_and_lines(filename):
#     try:
#         with open(filename, "r") as file:
#             lines = file.readlines()
#             line_count = len(lines)
#             word_count = sum(len(line.split()) for line in lines)


#             print(f"Number of lines: {line_count}")
#             print(f"Number of words: {word_count}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
# import random
# import string

# def generate_random_text_with_spaces(length=20, space_prob=0.2):
#     characters = string.ascii_letters + string.digits
#     result = []

#     for _ in range(length):
#         if random.random() < space_prob:
#             result.append(' ')
#         else:
#             result.append(random.choice(characters))

#     return ''.join(result)



# def make_sample(filename,lines):
#     try:
#         for i in range(lines):
#             with open(filename,'a') as file:
#                 file.write(generate_random_text_with_spaces(lines, 0.3))
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# count_words_and_lines("sample.txt")
# make_sample("sample.txt",10)
# count_words_and_lines("sample.txt")

############################## EXERCISE 2 Write and read a list of items  ############################################
# list1 = ['Apple', 'Waterlemon', 'banana', 'cucamber']
# try:
#     with open("sample.txt", 'w+') as file:
#         for item in list1:
#             file.write(item + "\n")
#         file.seek(0)
#         items = file.readlines()
#         for item in items:
#             print(item)
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
############################## EXERCISE 3 Copy a content of a file and past it ############################################
# def read_copy(filename,filename2):
#     try:
#         with open(filename, 'r') as file:
#             content = file.readlines()

#         with open(filename2, 'w') as file:
#             file.writelines(content)
#     except Exception as e:
#         print(f"An unexpected error occurred")

# read_copy("sample.txt","sample2.txt")
# ############################## EXERCISE 4 The number of words ############################################
# import string
# def words_counter(splited_line,user_word):
#     count = 0
#     user_word = user_word.lower().strip(string.punctuation)
#     for word in splited_line:
#         if word.lower().strip(string.punctuation) == user_word:
#             count += 1
#     return count
# def opener(filename,user_word):
#     empty_dic = {}
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             count_of_line = 1
#             for line in lines:
#                 splited_line = line.split()
#                 counts = words_counter(splited_line,user_word)
#                 empty_dic[f'Line{count_of_line}'] = counts
#                 count_of_line += 1
#         return empty_dic
#     except Exception as e:
#         print(f"An unexpected error occurred")

