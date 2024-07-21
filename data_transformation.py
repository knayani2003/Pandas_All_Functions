import pandas as pd

# Sample data for the first DataFrame
data1 = {
    "Emp Id": ["E01", "E02", "E03", "E04"],
    "Name": ["A", "B", "C", "D"],
    "Age": [34, 56, 23, 44]
}
df1 = pd.DataFrame(data1)

# Sample data for the second DataFrame
data2 = {
    "Emp Id": ["E01", "E02", "E03", "E04"],
    "Gender": ["M", "F", "F", "M"],
    "Salary": [10000, 15000, 8000, 5000]
}
df2 = pd.DataFrame(data2)

# Merge df1 and df2 on 'Emp Id' using a left join
merged_df = pd.merge(df1, df2, on="Emp Id", how="left")
print(merged_df)

# Sample data for the third DataFrame
data3 = {"Emp Id": ["E01", "E02", "E03", "E04"], "Name": ["A", "B", "C", "D"], "Age": [34, 56, 23, 44]}
data4 = {"Emp Id": ["E05", "E06", "E07", "E08"], "Name": ["E", "F", "G", "H"], "Age": [34, 56, 23, 44]}
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)

# Concatenate df3 and df4
concat_df = pd.concat([df3, df4])
print(concat_df)
