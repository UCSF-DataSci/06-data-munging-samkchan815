# Assignment 6: Data Cleaning Project

## 1. Initial State Analysis

### Data Overview
- **Names**: messy_population_data.csv
- **Rows**: 125718
- **Columns**: 5

### Column Details
| Column Name   | Data Type | Non-Null Count | Unique Values |  Mean   |
|---------------|-----------|----------------|---------------|---------|
| income_groups | object    | 119412         | ...           | ...     |
| age           | float64   | 119495         | ...           | 50.007  |
| gender        | float64   | 119811         | ...           | 1.579   |
| year          | float64   | 119518         | ...           | 2025.068|
| population    | float64   | 119378         | ...           | 1.113   |

### Identified Issues

1. **[Missing Values]**
- Description: There are missing values in all of the columns, where their values are null. 
- Affected Columns: All columns are affected
- Example: high_income,0.0,1.0,1979.0,nan
- Potential Impact: may result in incorrect summary statistics and analysis of the data

2. **[Incorrect Data Types]**
- Description: Variables are listed as the incorrect data type in the dataset.
- Affected Columns: All columns are affected
- Example: age is listed as a float when it should be a categorical variable
- Potential Impact: may result in incorrect analysis and summary statistics, along with calculations that do not make sense. 

3. **[Duplicated Data]**
- Description: Some rows of the dataset are duplicates.
- Affected Columns: All columns are affected
- Example: 
- Potential Impact: May lead to skewed data, for some of the information will have multiple inputs when calculating summary statistics.

4. **[Outliers**]
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
| Column Name    | Number of Nulls Removed|
|----------------|------------------------|
| income_groups  |  6117                  |
| age            |  6053                  |
| gender         |  5759                  |
| year           |  6026                  |
| population     |  6143                  |


### Issue 2: Incorrect Data Types
- **Approach**: correction of data types
- **Implementation**:
```
```
- **Justification**: By correcting the incorrect data types, this allows for correct interpretation of the results, which therefore leads to sensible summary statistics. If we were to leave the data types as they are, we would get results that do not make sense (i.e. the average of gender)
- **Impact**:

### Issue 3: Duplicated Data
- **Approach**: Removal
- **Implementation**:
```
df_clean = df.drop_duplicates() # remove duplicates
```


