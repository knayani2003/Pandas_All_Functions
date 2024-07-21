import pandas as pd

# Sample data for the DataFrame
data = {
    "Names": ["John", "Ben", "David", "Peter"],
    "Houses": ["Red", "Blue", "Green", "Red"],
    "Grades": ["3rd", "8th", "9th", "7th"]
}
df = pd.DataFrame(data)

# Melt the DataFrame: 'Names' is the id variable, 'Houses' and 'Grades' are the value variables
melted_df = pd.melt(df, id_vars=["Names"], value_vars=["Houses", "Grades"], var_name="Houses & Grades")
print(melted_df)
