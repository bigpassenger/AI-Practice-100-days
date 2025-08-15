# import pandas as pd

# s = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(s)

# data = {"Name": ["Alice", "Bob"],
#         "Age": [25, 30]
#         }
# df = pd.DataFrame(data)
# print(df)
# ######################################################
# print(df.head())
# print(df.tail(3))

# print(df.info())
# print(df.describe())

# print(df["Name"])
# print(df[["Name", "Age"]])

# print(df[df["Age"] > 25])

# print(df.iloc[0])
# print(df.iloc[:, 0])

# print(df.loc[0])
# print(df.loc[:, "Name"])
# ######################################################

# df = pd.read_csv("data.csv")
# df.to_csv("data.csv", index = False)
# df = pd.read_excel("data.xlsx")
# df.to_excel("data.xlsx", index = False)

############################ Exersize 1: Load and Explore a Sample Dataset ##########################
# from pathlib import Path
# import pandas as pd

# base_dir = Path(__file__).parent  
# path2 = base_dir / "data" / "iris.csv"
#     # df = pd.read_csv(file)
#     # print(df.head())
#     # print(df.iloc[0])
#     # print(df.iloc[:, 0])
#     # print(df.iloc[-1])
# with open(path2, 'r+') as file:
#     df = pd.read_csv(file)
#     print(df.head())
#     print(df.tail())
#     print(df.iloc[0])
#     print(df.iloc[:, 0])
#     print(df.iloc[-1])
#     print(df.info())
#     print(df.describe())

############################ Exersize 1: Load and Select Specific Columns and Filter Rows ##########################
# from pathlib import Path
# import pandas as pd

# base_dir = Path(__file__).parent  
# path2 = base_dir / "data" / "iris.csv"
# df = pd.read_csv(path2)
# print(df.head())
# print(df[df["sepal_length"] > 5])
