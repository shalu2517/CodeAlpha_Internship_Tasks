#Step 1: Import Required Libraries

import pandas as pd      
import numpy as np       
import matplotlib.pyplot as plt   
import seaborn as sns

#Step 2: Load the CSV File

data = pd.read_csv("C://Users//user//Downloads//EDA//student_performance.csv")  

#Step 3: Check Basic Structure

print(data.head())  
print(data.shape)       
print(data.info())      
print(data.describe())

# Step 4: Asking meaningful questions and validating using Pandas

# Q1: How many students passed and failed?
data['Result'] = np.where(data['total_score'] >= 40, 'Pass', 'Fail')
print(data['Result'].value_counts())
# Q2: What is the average total score?
print("Average Total Score:", data['total_score'].mean())
# Q3: Relationship between attendance and total score
print(data[['attendance_percentage', 'total_score']].corr())
# Q4: Relationship between study hours and total score
print(data[['weekly_self_study_hours', 'total_score']].corr())
# Q5: Average score for each grade
print(data.groupby('grade')['total_score'].mean())

# Step 5: Check for missing values
print(data.isnull().sum())

#STEP 6: Simple Visualization 

# Histogram for total score
plt.hist(data['total_score'], bins=20)
plt.xlabel('Total Score')
plt.ylabel('Number of Students')
plt.title('Distribution of Total Scores')
plt.show()

# Boxplot for outliers
sns.boxplot(y='total_score', data=data)
plt.title('Outliers in Total Score')
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,6))
numeric_data = data.select_dtypes(include=['int64', 'float64'])
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Numerical Features')
plt.show()

