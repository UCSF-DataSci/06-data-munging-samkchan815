import pandas as pd
import numpy as np
import argparse as args
import tqdm
import seaborn as sns
import matplotlib.pyplot as plt

def remove_duplicates(df):
    # check duplicates
    print('Before cleaning duplicate count:', df.duplicated().sum())
    duplicated_rows = df[df.duplicated(keep=False)]  # keep=False to mark all duplicates

    # Print duplicated rows
    print("Duplicated Rows:")
    print(duplicated_rows)
    df_clean = df.drop_duplicates() # remove duplicates
    print('After cleaning duplicate count:', df_clean.duplicated().sum())
    return df_clean

def remove_missing(df_clean):
    # check nulls and missing data
    print('Before cleaning null count:', df_clean.isnull().sum())
    df_clean = df_clean.dropna() # remove rows with null
    print('After cleaning null count:', df_clean.isnull().sum())
    return df_clean

def clean_outliers(df_clean):
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

    return df_clean

def plot_diff(df, df_clean):
    # Boxplots for population
    plt.figure(figsize=(10, 5))

    # before cleaning boxplot
    plt.subplot(1, 2, 1) # create plot on left
    sns.boxplot(y=df['population'], 
                color='orchid', 
                linecolor='black',
                linewidth=0.75
                )
    plt.title('Population Distribution Before Cleaning') # add title to plot

    # after cleaning boxplot
    plt.subplot(1, 2, 2) #plot on right
    sns.boxplot(y=df_clean['population'], 
                color='orchid', 
                linecolor='black',
                linewidth=0.75
                )
    plt.title('Population Distribution After Cleaning') # add title to plot

    plt.tight_layout() # frame margins even on all sides
    plt.savefig('populationPlot.png')# save image as png

def fix_types(df_clean):
    # Gender: float -> categorical
    gender_mapping = {1: 'Male', 2: 'Female', 3: 'Non-binary'} # Map to gender labels
    df_clean['gender'] = df_clean['gender'].map(gender_mapping)
    df_clean['gender'] = df_clean['gender'].astype('category') # convert to categorical

    # Population: float -> int
    df_clean['population'] = df_clean['population'].astype(int)

    # Year: float -> int
    df_clean['year'] = df_clean['year'].astype(int)

    # Age: float -> int
    df_clean['age'] = df_clean['age'].astype(int)

    # Income_groups: object -> categorical
    df_clean['income_groups'] = df_clean['income_groups'].astype('category') # convert to categorical

    print('Data types after cleaning: ') # check output
    print(df_clean.info())

    return df_clean

def main():
    # Read in csv file
    df = pd.read_csv('messy_population_data.csv')

    # data overview
    print(df.describe())
    print(df.info())
    print('Shape:', df.shape)

    unique_counts = df.nunique()
    print(unique_counts)

    df_clean = remove_duplicates(df)
    df_clean = remove_missing(df_clean)
    df_clean = clean_outliers(df_clean)
    df_clean = fix_types(df_clean)

    # clean data overview
    print(df_clean.describe())
    print(df_clean.info())
    print('Shape:', df_clean.shape)

    unique_counts = df_clean.nunique()
    print(unique_counts)

    # save csv
    df_clean.to_csv('cleaned_population_data.csv')

main()







