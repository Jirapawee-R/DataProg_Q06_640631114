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

