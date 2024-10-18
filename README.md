# Assignment 6: Data Cleaning Project

## 1. Initial State Analysis

### Data Overview
- **Names**: messy_population_data.csv
- **Rows**: 125718
- **Columns**: 5

### Column Details
| Column Name   | Data Type | Non-Null Count | Unique Values |  Mean   |
|---------------|-----------|----------------|---------------|---------|
| income_groups | object    | 119412         | 8             | -       |
| age           | float64   | 119495         | 101           | 50.007  |
| gender        | float64   | 119811         | 3             | 1.579   |
| year          | float64   | 119518         | 169           | 2025.068|
| population    | float64   | 119378         | 114925        | 1.113e8 |

### Identified Issues

1. **Missing Values**
- Description: There are missing values in all of the columns, where their values are null. 
- Affected Columns: All columns are affected
- Example: high_income,0.0,1.0,1979.0,nan
- Potential Impact: may result in incorrect summary statistics and analysis of the data

2. **Incorrect Data Types**
- Description: Variables are listed as the incorrect data type in the dataset.
- Affected Columns: Population, Age, Gender, Year
- Example: Age is listed as a float when it should be a categorical variable
- Potential Impact: may result in incorrect analysis and summary statistics, along with calculations that do not make sense. 

3. **Duplicated Data**
- Description: Some rows of the dataset are duplicates.
- Affected Columns: All columns are affected
- Example: high_income,0.0,2.0,2095.0,5353296.0
- Potential Impact: May lead to skewed data, for some of the information will have multiple inputs when calculating summary statistics.

4. **Outliers**
- Description: Columns may have outliers, which should be removed from the dataset
- Affected: Population Column
- Example: high_income,,1.0,1995.0,6780019000.0
- Potential Impact: may lead to skewed data and not properly represent the population.

## 2. Data Cleaning Process

### Issue 1: Missing Values
- **Approach**: Removal
- **Implementation**
```
df_clean = df_clean.dropna() # remove rows with null
```
- **Justification**: By removing missing data, one can maintain a more consistent dataset without inaccuracies or biased results. If this dataset were to be used for a machine learning model, missing data can also cause difficulties when training, leading to inaccurate predictions.

- **Impact**: 

| Column Name    | Number of Nulls Removed |
| ---------------- | ------------------------ |
| income_groups  |  6117                  |
| age            |  6053                  |
| gender         |  5759                  |
| year           |  6026                  |
| population     |  6143                  |


### Issue 2: Incorrect Data Types
- **Approach**: correction of data types
- **Implementation**:
```
# Fixing data types
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
```
- **Justification**: By correcting the incorrect data types, this allows for correct interpretation of the results, which therefore leads to sensible summary statistics. If we were to leave the data types as they are, we would get results that do not make sense (i.e. the average of gender)
- **Impact**: Gender no longer has a mean, standard deviation, other statistical summary results. Gender and income groups may now be used to sort data into groups. Finally, proper data type selection allows aggregation of data tables.

### Issue 3: Duplicated Data
- **Approach**: Removal
- **Implementation**:
```
df_clean = df.drop_duplicates() # remove duplicates
```
- **Justification**: Removing duplicates allows for proper representation of unique data instances. Leaving them in may result in inaccurate or skewed data, therefore resulting in results that does not properly represent the population.

- **Impact**:  2,950 total duplicate data rows removed

### Issue 4: Outliers
- **Approach**: Removal
- **Implementation**
```
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
```
- **Justification**: Removal of the outliers allows not only readability, but also to prevent distorted or skewed results. Outliers can sometimes greatly impact results highly positively or negatively. This therefore leads to more readable data and more accurate results and summary statistics.
- **Impact**: As illustrated by the box plot below, by removing outliers, it allows the plot to be more readable and illustrate the data more cleanly.

![Population Outliers Boxplot](/populationPlot.png)

## 3. Final State Analysis
I cleaned this dataset by removing missing values, removing outliers, removing, removing duplicates, and setting proper data types. Although after all of these actions the dataset is much smaller, it is now a dataset that is representative of the population and free from any data that may skew or the data. Therefore, any results found with the dataset will be more accurate and unbiased.

When cleaning, I found it difficult to determine where to start because there were so many different steps that needed to be done. It was very helpful to start by looking at the data summary using the pandas ```describe()``` and ```info()``` functions.




