"""Exploratory Data Analysis (EDA) is a critical initial phase in data science workflows. It involves summarizing, visualizing, and understanding the structure, patterns, and anomalies in datasets before formal modeling. The image highlights core aspects of EDA:

Applying Data Manipulation and Visualization for EDA:

Data Manipulation: Using libraries like Pandas and NumPy to reshape, transform, and clean data.

Data Visualization: Using Matplotlib, Seaborn, and Plotly to create visualizations that reveal patterns and relationships.

What is EDA?:

EDA is an approach to analyze datasets to summarize their main characteristics, often using visual methods.

Steps in EDA:

Data Cleaning: Identifying and resolving issues in the data.

Data Transformation: Modifying variables for better analysis.

Aggregation and Filtering: Summarizing data and focusing on specific subsets.

Here are comprehensive Python code examples for each step:

Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder

###########Create sample data for demonstration
np.random.seed(42)
data = {
'age': np.random.randint(18, 65, 100),
'income': np.random.normal(50000, 15000, 100),
'department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing'], 100),
'performance_score': np.random.uniform(1, 10, 100),
'years_experience': np.random.randint(0, 20, 100)
}

##############################################Introduce some missing values and outliers for demonstration
data['income'][10:15] = np.nan
data['age'][95:100] = [120, 150, 180, 200, 250] # Outliers

df = pd.DataFrame(data)

print("Initial Data Overview:")
print(df.head())
print("\nData Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

##############################################DATA CLEANING EXAMPLES
1. Handling Missing Values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

##############################################Fill missing values with mean
df['income'].fillna(df['income'].mean(), inplace=True)

##############################################Alternative: Drop rows with missing values
df.dropna(inplace=True)
print("\nMissing values after cleaning:")
print(df.isnull().sum())

2. Handling Outliers
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1

##############################################Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

##############################################Cap outliers
df['age'] = np.where(df['age'] > upper_bound, upper_bound,
np.where(df['age'] < lower_bound, lower_bound, df['age']))

3. Removing Duplicates
df = df.drop_duplicates()

##############################################DATA TRANSFORMATION EXAMPLES
1. Normalization/Scaling
scaler = StandardScaler()
df['income_scaled'] = scaler.fit_transform(df[['income']])

2. Log Transformation (for skewed data)
df['log_income'] = np.log1p(df['income'])

3. Encoding Categorical Variables
label_encoder = LabelEncoder()
df['department_encoded'] = label_encoder.fit_transform(df['department'])

4. Creating New Features
df['income_per_year'] = df['income'] / (df['years_experience'] + 1) # +1 to avoid division by zero

print("\nAfter Transformation:")
print(df[['income', 'income_scaled', 'log_income', 'department', 'department_encoded']].head())

##############################################AGGREGATION AND FILTERING EXAMPLES
1. Basic Filtering
high_income = df[df['income'] > 70000]
it_department = df[df['department'] == 'IT']

2. Multi-condition Filtering
senior_it = df[(df['department'] == 'IT') & (df['years_experience'] > 10)]

3. GroupBy Aggregation
department_stats = df.groupby('department').agg({
'income': ['mean', 'median', 'std'],
'age': 'mean',
'performance_score': 'count'
}).round(2)

print("\nDepartment-wise Statistics:")
print(department_stats)

4. Pivot Tables
pivot_table = pd.pivot_table(df,
values='income',
index='department',
columns=pd.cut(df['years_experience'], bins=3),
aggfunc='mean')

print("\nPivot Table:")
print(pivot_table)

##############################################DATA VISUALIZATION EXAMPLES
Set up the visualization style
sns.set_style("whitegrid")
plt.figure(figsize=(15, 10))

1. Distribution Plot
plt.subplot(2, 3, 1)
sns.histplot(df['income'], kde=True)
plt.title('Income Distribution')

2. Box Plot
plt.subplot(2, 3, 2)
sns.boxplot(x='department', y='income', data=df)
plt.title('Income by Department')

3. Scatter Plot
plt.subplot(2, 3, 3)
plt.scatter(df['years_experience'], df['income'])
plt.xlabel('Years of Experience')
plt.ylabel('Income')
plt.title('Experience vs Income')

4. Bar Plot
plt.subplot(2, 3, 4)
department_counts = df['department'].value_counts()
sns.barplot(x=department_counts.index, y=department_counts.values)
plt.title('Employee Count by Department')

5. Correlation Heatmap
plt.subplot(2, 3, 5)
numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')

6. Pair Plot (commented out as it can be heavy for large datasets)
sns.pairplot(df[['age', 'income', 'years_experience', 'performance_score']])
plt.title('Pair Plot of Numerical Variables')
plt.tight_layout()
plt.show()

##############################################Additional Advanced Analysis
1. Outlier Detection using Z-score
from scipy import stats
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
outliers = (z_scores > 3).sum(axis=0)
print("\nOutliers detected (Z-score > 3):")
print(outliers)

2. Advanced Visualization with Seaborn
plt.figure(figsize=(12, 6))

Violin plot
plt.subplot(1, 2, 1)
sns.violinplot(x='department', y='income', data=df)
plt.title('Income Distribution by Department')
"""

import pandas as pd
import requests
import os
from pathlib import Path

################################Task 1: Perform Data Cleaning, Aggregation, and Filtering
# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
current_dir = Path(os.getcwd())
path = current_dir / "dataset" / "titanic_dataset.csv"
if not path.exists():
    with open(path, "w", encoding="utf-8") as f:
        data = requests.get(url)
        f.write(data.text)
df = pd.read_csv(path)
data = pd.DataFrame(df)
# print(data)

# Inspect Data
print(df.info())
print(df.describe())


# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

# Filter data; Paasengers in first class
first_class = df[df["Pclass"] == 1]
print("First Class Passengers: \n", first_class.head())

################################Task 2: Generate Visualizations to illustrate Key Insights
import matplotlib.pyplot as plt
import seaborn as sns

#Bar chart: Survival rate by class
survival_counts = {
    1: df[(df["Pclass"] == 1) & (df["Survived"] == 1)].shape[0],
    2: df[(df["Pclass"] == 2) & (df["Survived"] == 1)].shape[0],
    3: df[(df["Pclass"] == 3) & (df["Survived"] == 1)].shape[0],
}
print(survival_counts)

survival_rate = df.groupby("Pclass")["Survived"].mean()
print("Survival rate by class:\n", survival_rate)
survival_rate.plot(kind="bar", color="skyblue")
plt.title("Survival Rate")
plt.ylabel("survival Rate")
plt.show()

#Histogram for age distribution
sns.histplot(df["Age"], kde = True, bins = 20, color="purple")
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("frequency")
plt.show()
# Scatter Plot: Age vs Fare
plt.scatter(df["Age"], df["Fare"], alpha = 0.5, color = "green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()






###########################A Note to myself###############################
"""
Additional Practice

Use another dataset and apply the same EDA steps
Explore advanced visualizations like boxplots or pairplots in Seaborn
Create a dashboard for your findings using Plotly or Dash.
"""
##########################################################################