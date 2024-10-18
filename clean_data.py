import pandas as pd
import numpy as np
import argparse as args
import tqdm

# Read in csv file
df = pd.read_csv('messy_population_data.csv')

# data overview
print(df.describe())
print(df.info())
print(df.shape)

# check duplicates
print(df.duplicated().sum())
df_clean = df.drop_duplicates() # remove duplicates
print(df_clean.duplicated().sum())

# check nulls and missing data
print(df_clean.isnull().sum())
df_clean = df_clean.dropna() # remove rows with null
print(df_clean.isnull().sum())

# Using IQR
col = 'population'
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
print(Q1, Q3)
IQR = Q3 - Q1

# Define lower and upper bounds for detecting outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find all outliers
outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

# Print the outlier values
print(f"Outliers in column '{col}':")
print(outliers)
#df_clean = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]




