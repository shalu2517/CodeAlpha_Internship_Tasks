import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_performance.csv")

print(df.head())
print(df.shape)
print(df.columns)
df.info()

print(df.isnull().sum())
df.drop_duplicates(inplace=True)

# Distribution
plt.hist(df['total_score'])
plt.title("Total Score Distribution")
plt.xlabel("Score")
plt.ylabel("Students")
plt.show()

# Comparison
sns.barplot(x='grade', y='total_score', data=df)
plt.title("Grade vs Total Score")
plt.show()

# Correlation
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Feature Correlation Heatmap")
plt.show()
