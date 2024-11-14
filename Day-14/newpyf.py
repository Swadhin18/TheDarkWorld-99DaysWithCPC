# Step 1: Import Libraries
import numpy as np
import pandas as pd

# Step 2: Load Data
titanic = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Step 3: Data Exploration
print(titanic.info())
print(titanic.describe())
print(titanic.isnull().sum())  # Check for missing values

# Step 4: Data Cleaning
# Fill missing Age values with median age
titanic['Age'].fillna(titanic['Age'].median(), inplace=True)
# Drop rows with missing 'Embarked' (or use a different strategy)
titanic.dropna(subset=['Embarked'], inplace=True)
# Convert 'Sex' to numeric
titanic['Sex'] = titanic['Sex'].map({'male': 0, 'female': 1})

# Step 5: Exploratory Data Analysis
# Survival rate
overall_survival_rate = titanic['Survived'].mean()
print(f"Overall Survival Rate: {overall_survival_rate:.2f}")

# Survival by Gender
gender_survival_rate = titanic.groupby('Sex')['Survived'].mean()
print("Survival Rate by Gender:\n", gender_survival_rate)

# Survival by Passenger Class
class_survival_rate = titanic.groupby('Pclass')['Survived'].mean()
print("Survival Rate by Class:\n", class_survival_rate)

# Age Groups
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
titanic['AgeGroup'] = pd.cut(titanic['Age'], bins)
age_survival_rate = titanic.groupby('AgeGroup')['Survived'].mean()
print("Survival Rate by Age Group:\n", age_survival_rate)

# Step 6: Further Analysis (Optional)
# Correlation
print("Correlation Matrix:\n", titanic.corr())

# Step 7: Conclusion
# Summarize key findings
