import pandas as pd

# Assuming df1 contains the forest area data and df2 contains the wind energy data

# Sample DataFrame for forest area data (df1)
df1 = pd.DataFrame({
    'Country': ['USA', 'Canada', 'Mexico'],
    'Year_2019': [1000, 1500, 800],
    'Year_2020': [1100, 1600, 820],
    'Year_2021': [1200, 1700, 840]
})

# Sample DataFrame for wind energy data (df2)
df2 = pd.DataFrame({
    'Country': ['USA', 'Canada', 'USA'],
    'Year': [2019, 2019, 2020],
    'Wind_Energy_kJ': [500, 600, 550]
})

# Merge the two DataFrames based on 'Country' and 'Year'
merged_df = pd.merge(df1, df2, left_on=['Country', 'Year_2019'], right_on=['Country', 'Year'], how='left')

# Rename columns as needed
merged_df.rename(columns={'Year_2019': 'Year'}, inplace=True)

# Drop the redundant 'Year' column from the merge
merged_df.drop(columns=['Year'], inplace=True)

# Print the merged DataFrame
print(merged_df)