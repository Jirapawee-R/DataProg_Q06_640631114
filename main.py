# %%
import pandas as pd

df = pd.read_csv("~/Desktop/MsD/DataProg/Salaries.csv")

print(df.head())

# HANDS-ON EXERCISES (QUIZ 1)
# Read first 10, 20, 50 records
print(df.head(10))
print(df.head(20))
print(df.head(50))

# How to view the last few records
print(df.tail())

# %%
# Check type for all columns
print(df.dtypes)

# Check a particular column
print(df['salary'].dtype)

# %%
# 1) Group data using rank
df_rank = df.groupby(['rank'])
print(df_rank)

# 2) Calculate mean for each numeric column per each group
print(df_rank.mean())

# 3) Calculate mean salary for each professor rank
print(df.groupby(['rank'])[['salary']].mean())

# 4) Calculate mean salary for each professor rank
print(df.groupby(['rank'], sort=False)[['salary']].mean())

# %%
# 5) Subset the rows in which salary > $120K
df_sub = df[df['salary'] > 120000]
print(df_sub)

# 6) Select only those rows that contain female professors
df_f = df[df['sex'] == 'Female']
print(df_f)

# %%
# 7) Select column salary
print(df['salary'])

# 8) Select column rank and column Salary
print(df[['rank', 'salary']])

# %%
# 9) Select rows by their position
print(df[10:20])

# %%
# 10) Select rows by their labels:
print(df_sub.loc[10:20, ['rank', 'sex', 'salary']])

# %%
# 11) Select range of rows using position use method iloc
print(df_sub.iloc[10:20, [0,3,4,5]])

# %%
# 12) Create a new dataframe from orinal one sorted by service
df_sort = df.sort_values(by='service')
print(df_sort.head())

# %%
# 13) Sort the data using 2 or more column
df_sorted =  df.sort_values(by=['service', 'salary'], ascending= [True, False])
print(df_sorted.head(10))
