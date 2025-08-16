# import pandas as pd

# s = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(s)
"""
pd.Series creates a one-dimensional labeled array.
Here: values = [10, 20, 30] and custom index = ["a", "b", "c"]

Output:
a    10
b    20
c    30
dtype: int64
"""

# data = {"Name": ["Alice", "Bob"],
#         "Age": [25, 30]
#         }
# df = pd.DataFrame(data)
# print(df)
"""
pd.DataFrame creates a table-like structure (rows & columns).
Here we make a DataFrame from a dictionary.

Output:
    Name  Age
0  Alice   25
1    Bob   30
"""

# ######################################################
# print(df.head())
"""
head() shows the first 5 rows of the DataFrame by default.
"""

# print(df.tail(3))
"""
tail(3) shows the last 3 rows of the DataFrame.
"""

# print(df.info())
"""
info() gives details about DataFrame:
- number of rows
- column names
- non-null counts
- data types
"""

# print(df.describe())
"""
describe() gives statistical summary for numeric columns:
count, mean, std, min, max, quartiles.
"""

# print(df["Name"])
"""
Selects a single column by name.
Output is a Series of 'Name'.
"""

# print(df[["Name", "Age"]])
"""
Selects multiple columns by passing a list.
Output is a smaller DataFrame with only Name and Age.
"""

# print(df[df["Age"] > 25])
"""
Boolean indexing (filtering).
Keeps only rows where Age > 25.
"""

# print(df.iloc[0])
"""
iloc uses integer-based indexing.
df.iloc[0] → the first row (position 0).
"""

# print(df.iloc[:, 0])
"""
iloc[:,0] selects all rows from the first column.
"""

# print(df.loc[0])
"""
loc uses label-based indexing.
df.loc[0] → row with index label 0.
"""

# print(df.loc[:, "Name"])
"""
loc[:, "Name"] selects all rows of column 'Name'.
"""

# ######################################################

# df = pd.read_csv("data.csv")
"""
Reads a CSV file into a DataFrame.
"""

# df.to_csv("data.csv", index = False)
"""
Saves the DataFrame into a CSV file.
index=False means it will not save row indices.
"""

# df = pd.read_excel("data.xlsx")
"""
Reads data from an Excel file.
"""

# df.to_excel("data.xlsx", index = False)
"""
Saves the DataFrame to Excel format.
"""

############################ Exercise 1: Load and Explore a Sample Dataset ##########################
# from pathlib import Path
# import pandas as pd

# base_dir = Path(__file__).parent  
# path2 = base_dir / "data" / "iris.csv"
# with open(path2, 'r+') as file:
#     df = pd.read_csv(file)
#     print(df.head())
#     print(df.tail())
#     print(df.iloc[0])
#     print(df.iloc[:, 0])
#     print(df.iloc[-1])
#     print(df.info())
#     print(df.describe())
"""
Here we:
1. Load the famous Iris dataset from a CSV file.
2. Display the first few rows (head).
3. Display the last few rows (tail).
4. Show the first row (iloc[0]).
5. Show the first column (iloc[:,0]).
6. Show the last row (iloc[-1]).
7. Get dataset info (df.info()).
8. Get summary statistics (df.describe()).
"""

############################ Exercise 2: Load and Select Specific Columns and Filter Rows ##########################
# from pathlib import Path
# import pandas as pd

# base_dir = Path(__file__).parent  
# path2 = base_dir / "data" / "iris.csv"
# df = pd.read_csv(path2)
# print(df.head())
# print(df[df["sepal_length"] > 5])
"""
This exercise:
1. Loads the Iris dataset.
2. Displays the first few rows (df.head()).
3. Filters rows where sepal_length > 5.
"""
