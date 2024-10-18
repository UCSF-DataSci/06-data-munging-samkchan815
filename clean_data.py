import pandas as pd
import numpy as np
import argparse as args
import tqdm
import seaborn as sns
import matplotlib.pyplot as plt

# Read in csv file
df = pd.read_csv('messy_population_data.csv')

# data overview
print(df.describe())
print(df.info())
print('Shape:', df.shape)

# check duplicates
print('Before cleaning duplicate count:', df.duplicated().sum())
df_clean = df.drop_duplicates() # remove duplicates
print('After cleaning duplicate count:', df_clean.duplicated().sum())


# check nulls and missing data
print('Before cleaning null count:', df_clean.isnull().sum())
df_clean = df_clean.dropna() # remove rows with null
print('After cleaning null count:', df_clean.isnull().sum())


# Find IQR 
col = 'population'
Q1 = df_clean[col].quantile(0.25)
Q3 = df_clean[col].quantile(0.75)

IQR = Q3 - Q1

# Define lower and upper bounds for detecting outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find all outliers
outliers = df_clean[(df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)]

# Print the outlier values
print(f"Outliers in column '{col}':")
print(outliers)

# Remove outliers in clean dataset
df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)] 

# Find all outliers
outliers = df_clean[(df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)]

# Print the outlier values
print(f"Outliers in column '{col}':")
print(outliers)

# Boxplots for 'age' column before and after cleaning
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['population'], 
            color='orchid', 
            linecolor='black',
            linewidth=0.75
            )
plt.title('Population Distribution Before Cleaning')

plt.subplot(1, 2, 2)
sns.boxplot(y=df_clean['population'], 
            color='orchid', 
            linecolor='black',
            linewidth=0.75
            )
plt.title('Population Distribution After Cleaning')

plt.tight_layout()
plt.savefig('populationPlot.png')







