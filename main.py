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

