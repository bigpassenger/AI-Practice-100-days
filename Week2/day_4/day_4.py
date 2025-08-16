# df = df.dropna()
""" 
dropna() removes rows that contain missing values (NaN).
Example:
   A   B
0  1 NaN
1  2  3
df.dropna() → removes row 0 because it has NaN.
"""

# df = df.dropna(axis = 1)
""" 
axis=1 removes entire columns that contain NaN.
Example:
   A   B
0  1 NaN
1  2  3
df.dropna(axis=1) → removes column B.
"""

# df["coulmn_name"] = df["column_name"].fillna(0)
"""
fillna(0) replaces missing values with 0.
Example:
Age = [25, NaN] → [25, 0]
"""

# df.fillna(method = "ffill")
"""
Forward fill (ffill) replaces NaN with the last known non-null value.
Example: [10, NaN, 20] → [10, 10, 20]
"""

# df.fillna(method = "bfill")
"""
Backward fill (bfill) replaces NaN with the next available non-null value.
Example: [10, NaN, 20] → [10, 20, 20]
"""

# df["column_name"] = df["column_name"].interpolation()
"""
interpolate() fills NaN using linear interpolation by default.
Example: [10, NaN, 30] → [10, 20, 30]
"""

# ############################################

# df = df.rename(columns={"old_name": "new_name"})
"""
rename() changes column names.
Example: 'Name' → 'Student_Name'
"""

# df["column_name"] = df["column_name"].astype("float")
"""
astype("float") converts column data type to float.
Example: [1,2,3] → [1.0, 2.0, 3.0]
"""

# df["column_name"] = pd.to_datetime(df["column_name"])
"""
Converts column to datetime format.
Example: '2024-01-01' → 2024-01-01 00:00:00
"""

# df["new_column"] = df["old_column"] * 2
"""
Creates a new column based on transformation.
Example: old_column [1,2] → new_column [2,4]
"""

# #################################################Concatenation,Merging,Joining#################################################

# combined = pd.concat([df1, df2], axis = 0)
"""
Concatenation along rows (axis=0). Stacks DataFrames vertically.
"""

# combined = pd.concat([df1, df2], axis = 1)
"""
Concatenation along columns (axis=1). Joins side by side.
"""

# merged = pd.merge(df1, df2, on = "common_column")
"""
Merge on a common column (default inner join).
"""

# merged = pd.merge(df1, df2, how="left", on="common_column")
"""
Left merge: keeps all rows from df1, matches with df2 if possible.
"""

# merged = pd.merge(df1, df2, how="inner", on="common_column")
"""
Inner merge: keeps only rows with matching keys in both DataFrames.
"""

# joined = df1.join(df2, how="inner")
"""
join() works like merge but matches on the index by default.
"""

################################################Exercise 1#################################################
# import pandas as pd
# import numpy as np

# data = {
#     "Name": ["Alice", "Bob", np.nan, "David"],
#     "Age": [25, np.nan, 30, 35],
#     "Score": [85, 90, np.nan, 88]
# }

# df = pd.DataFrame(data)
# print(df)
"""
Created a DataFrame with some missing values.
"""

# df["Age"] = df["Age"].fillna(df["Age"].mean())
"""
Replaces missing Age with the average Age.
Example: [25, NaN, 30, 35] → [25, 30, 30, 35]
"""

# df["Score"] = df["Score"].interpolate()
"""
Interpolates missing Score values.
Example: [85, 90, NaN, 88] → [85, 90, 89, 88]
"""

# df = df.rename(columns={"Name":"Student_Name", "Score": "Exam:Score"})
"""
Renames columns: Name → Student_Name, Score → Exam:Score
"""

# print(df)


################################################# Exercise 2 Merge datasets and perform Data Transformation #################################################3
# import pandas as pd
# import numpy as np

# data1 = pd.DataFrame({
#     "ID": [1, 2, 3],
#     "Score": [85, 90, 88]
# })
# data2 = pd.DataFrame({
#     "ID": [1, 2, 3],
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 35],
# })

# merged = pd.merge(data1, data2, how="inner", on="ID")
# print(merged)
"""
Merges two DataFrames using 'ID' as key.
"""

# merged["Score_Percentage"] = (merged["Score"]/ 100) * 100
"""
Adds new column Score_Percentage.
Example: Score=85 → Score_Percentage=85
"""

# print(merged)
