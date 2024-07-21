import pandas as pd

# Load the data from the CSV file
data = pd.read_csv("C:/Users/KRISHNA/OneDrive/Documents/relevant_sample_data.csv")
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())

# Display the last few rows of the DataFrame
print(df.tail())

# Display information about the DataFrame (e.g., column types, non-null counts)
print(df.info())

# Display statistical summary of the DataFrame
print(df.describe())

# Check for null values in the DataFrame
print(df.isnull())
print(df.isnull().sum())

# Fill missing values in 'Age' and 'Salary' columns with their mean values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Backfill any remaining missing values
df = df.bfill()

# Add a new column 'Bonus' which is 20% of the 'Salary'
df['Bonus'] = (df['Salary'] / 100) * 20

# Convert 'Bonus' column values to integer type
df['Bonus'] = df['Bonus'].astype(int)

# Print the modified DataFrame
print(df)
