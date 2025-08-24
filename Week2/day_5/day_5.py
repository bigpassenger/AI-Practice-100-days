import pandas as pd
from pathlib import Path

"""Explanation:
Here we import the necessary libraries:
- pandas: for data manipulation and analysis
- pathlib.Path: for handling file paths in an OS-independent way
"""

base_dir = Path(__file__).parent  
"""Explanation:
Path(__file__).parent gives the directory of the current Python file.
This is used to construct a relative path to the CSV file.
"""

path2 = base_dir / "iris.csv"
"""Explanation:
We create the full path to 'iris.csv' inside the same folder as the script.
"""

df = pd.read_csv(path2)
"""Explanation:
pd.read_csv() reads the CSV file into a DataFrame.
At this point, 'df' contains the iris dataset.
"""

data = {
    "team": ["A", "A", "B", "B", "C"],
    "score": [10, 15, 20, 25, 30]
}
"""Explanation:
Here we define a dictionary with two keys:
- 'team' represents the team labels
- 'score' represents the scores of each team member
"""

df = pd.DataFrame(data)
"""Explanation:
We overwrite 'df' with a new DataFrame created from the dictionary 'data'.
Now 'df' has 5 rows and 2 columns: team and score.
"""

columns = df.head()
"""Explanation:
df.head() returns the first 5 rows of the DataFrame.
Here we store it in 'columns', but usually it's just used for inspection.
"""

grouped = df.groupby("team")
"""Explanation:
df.groupby("team") groups the data by the 'team' column.
The result is a GroupBy object, which can be used for aggregation or iteration.
"""

# print(grouped)
# for name,group in grouped:
#     print(name)
#     print(group)

"""Explanation:
If you uncomment this loop, it will print each group separately:
- 'name' is the team label (A, B, C)
- 'group' is the subset of the DataFrame belonging to that team
"""

pivot = df.pivot_table(
    values = "score",
    index = "team",
    aggfunc="mean"
)
"""Explanation:
df.pivot_table() creates a summary table.
Here we calculate the mean score for each team.
- values="score": the column we want to aggregate
- index="team": the column we group by
- aggfunc="mean": the function applied to values
"""

def range_func(x):
    return x.max() - x.min()

"""Explanation:
We define a custom aggregation function 'range_func'.
It calculates the difference between the maximum and minimum value in a group.
"""

df.groupby("team")["score"].agg(range_func)
"""Explanation:
We apply 'range_func' to the 'score' column for each team.
This shows the score range within each team.
"""

print(df.groupby("team")["score"].agg(range_func))
"""Explanation:
This prints the computed range for each team's scores.
"""

print(df.groupby("team")["score"])
"""Explanation:
This prints the GroupBy object itself, not the values.
It shows that the 'score' column is grouped by 'team'.
"""

df.groupby("team").agg(
    {"score": ["mean","max","min"]}
)
"""Explanation:
Here we use multiple aggregations for 'score':
- mean: average score per team
- max: maximum score per team
- min: minimum score per team
"""

#################################### Exercise 1 ####################################

# import pandas as pd
#
# data = {
#     "Class": ["A", "B", "A", "B", "C", "C"],
#     "Score": [85, 90, 88, 72, 95, 80],
#     "Age": [15, 16, 15, 17, 16, 15],
# }
#
# df = pd.DataFrame(data)
# print("Original Dataset \n",df)
#
# print(df.pivot_table(
#     values="Score",
#     index="Class",
#     aggfunc= "mean"
# )
# )
# grouped = df.groupby("Class").mean()
# print(grouped)

"""Exercise 1:
1. Create a DataFrame with Class, Score, and Age as given.
2. Use pivot_table() to find the average score of each Class.
3. Use groupby() to find the mean values of all numeric columns for each Class.
4. Compare the results from pivot_table() and groupby().
"""

#################################### Exercise 2 ####################################

import pandas as pd

data = {
    "Class": ["A", "B", "A", "B", "C", "C"],
    "Score": [85, 90, 88, 72, 95, 80],
    "Age": [15, 16, 15, 17, 16, 15],
}

df = pd.DataFrame(data)

stats = df.groupby("Class").agg(
    {"Score": ["mean", "max", "min"],
     "Age": ["mean", "max", "min"]
    }
)

print(stats)

"""Explanation:
In Exercise 2:
- We group the data by 'Class'.
- For 'Score', we calculate mean, max, and min.
- For 'Age', we also calculate mean, max, and min.
The result is a DataFrame with multi-level column names.
"""

"""Exercise 2:
1. Create a DataFrame with Class, Score, and Age.
2. Group the data by 'Class'.
3. For each Class:
   - Calculate mean, max, and min of 'Score'.
   - Calculate mean, max, and min of 'Age'.
4. Print the result to analyze class performance and age distribution.
"""
