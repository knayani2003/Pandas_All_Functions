import pandas as pd

# Sample data for the DataFrame
data = {
    "keys": ["k1", "k2", "k1", "k2"],
    "Names": ["John", "Ben", "David", "Peter"],
    "House": ["Red", "Blue", "Green", "Red"],
    "Grades": ["3rd", "8th", "9th", "7th"]
}
df = pd.DataFrame(data)

# Pivot the DataFrame: index is 'keys', columns are 'Names', values are 'House' and 'Grades'
pivot_df = df.pivot(index="keys", columns="Names", values=["House", "Grades"])
print(pivot_df)
